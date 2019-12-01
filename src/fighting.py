import pygame,sys,time
from pygame.locals import *
from path import path
from map import *
from mapDisplay import *
from models import *
from gamecontroller import *
from levelDefend import *
from defeated import *
from fightResult import endFight

# modeID为游戏模式编号，mapID为地图编号, charID为选用的角色的列表编号
def startFight(screen, clock, modeID, mapID, CharID):
    #背景图
    bg = pygame.image.load(path("res/bg/bg_fighting.png")).convert_alpha()
    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    breakflag = 0
    startTime = pygame.time.get_ticks()
    lastTime = startTime
    # 计时准备(后面要和Time统一）
    COUNT = pygame.USEREVENT + 1
    pygame.time.set_timer(COUNT, 25)  # 每0.025秒发一次
    counts = 0
    # 读取进攻计划文档并存储在对应的元组中
    attackerorder = 0
    attackerplan = attackerload(mapID)
    # 初始化界面
    infoPic = pygame.image.load(path("res/battle/information.png")).convert_alpha()     #信息
    infoPos = (0, 0)
    timePic = pygame.image.load(path("res/battle/time.png")).convert_alpha()            #倒计时
    timePos = (265, 0)
    lifePic = pygame.image.load(path("res/battle/life.png")).convert_alpha()            #防守方生命值
    lifePos = (515, 0)
    costPic = pygame.image.load(path("res/battle/Cost.png")).convert_alpha()            #防守方金钱
    costPos = (765, 0)
    Toolflame = pygame.image.load(path("res/battle/tools.png")).convert_alpha()         #道具
    ToolflamePos = (1015, 0)
    BattleMap = pygame.image.load(path("res/battle/mapdisplay.png")).convert_alpha()    #地图
    BattleMapPos = (265, 70)
    Giveup = pygame.image.load(path("res/battle/giveup.png")).convert_alpha()           #弃权
    cancelPic = pygame.image.load(path("res/battle/cancel.png")).convert_alpha()        #取消选择
    cancelPic = pygame.transform.scale(cancelPic,(140,50))
    cancelPos = (85, 520)
    GiveupPos = (1080, 630)
    Direction = []                                                                      #选择人物朝向
    DirectionPos = []
    # 依次为上左下右，点击按键确定朝向
    for i in range(4):
        Direction.append(pygame.image.load(path("res/battle/arrow"+str(i)+".png")).convert_alpha())
        Direction[i] = pygame.transform.scale(Direction[i],(50,50))
    DirectionPos.append((130,350))
    DirectionPos.append((85, 400))
    DirectionPos.append((130, 450))
    DirectionPos.append((175, 400))

    # 不同角色的路径关键词缀
    str_char = ["pingmin","gongtou","gansidui","pangdun","yaojishi"]
    Charflame = pygame.image.load(path("res/battle/charflame.png")).convert_alpha()
    # 人物框
    Charnum = len(CharID)
    CharPos = []
    # 上锁图与未上锁图
    CharPic = []
    CharPics = []
    # 防守方人物在地图中的图片
    DefendPic = []
    # 进攻方人物在地图中的图片
    AttackPic = []
    # 对应防守方人物最后放置的时间，单位为ms，下标为已选择的人物的编号
    defendlastcd = []
    # 防守方人物所需要的费用
    defendcost =[]
    # 防守方人物所需要的冷却
    defendneedcd =[]
    # 按人物编号所依次需要的费用和冷却
    costall = [10,20,15,18,20]
    cdall = [15,80,15,25,60]
    # 选取的角色编号（为CharID列表中的下标，如果为-1，表示未选取）
    Charsel = -1
    # 选取的坐标编号（取整数），[-1，-1]为未选取
    Coorsel = [-1, -1]
    # 上次选取的坐标编号，用于回退
    Coorselold = [-1, -1]
    # 选取的方向，-1或者False表示未选取，0-3依次为上左下右
    Dirsel = [-1]
    Dirselstatus = False
    for i in range(0, Charnum):
        # 编队框人物解锁与未解锁图
        CharPic.append(pygame.image.load(path("res/battle/"+str_char[CharID[i]]+"b.png")).convert_alpha())
        CharPics.append(pygame.image.load(path("res/battle/"+str_char[CharID[i]]+"bs.png")).convert_alpha())
        CharPos.append((640 - 37.5 * Charnum + i * 75, 550))
        defendcost.append(costall[CharID[i]])
        defendneedcd.append(cdall[CharID[i]])
        defendlastcd.append(startTime - defendneedcd[i] * 1000)
    for i in range(5):
        # 进攻与防守方人物贴图
        DefendPic.append(pygame.image.load(path("res/character/" + str_char[i] + "b0.png")).convert_alpha())
        DefendPic[i] = pygame.transform.scale(DefendPic[i], (75, 75))
        AttackPic.append(pygame.image.load(path("res/character/" + str_char[i] + "r0.png")).convert_alpha())
        AttackPic[i] = pygame.transform.scale(AttackPic[i], (75, 75))

    # 地图准备
    mapload = levelLoad(mapID)
    if modeID == 2:
        controller = GameController(mapID, mapload, 'Single', 'Defend')
    else:
        # need to be change
        controller = GameController(mapID, mapload)

    # 角色准备，分别存储地图上的进攻与防守单位，ID为该单位所对应的人物编号，同时维护
    attackers = []
    attackersID =[]
    deffenders = []
    deffendersID = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                #   放弃，失败
                if x > GiveupPos[0] and x < GiveupPos[0] + Giveup.get_width() \
                    and y > GiveupPos[1] and y < GiveupPos[1] + Giveup.get_height():
                    endFight(screen, clock, modeID, mapID, False)
                    breakflag = 1

                for i in range(Charnum):
                    #   选取人物，或者切换选取人物，都需要对坐标朝向等重置
                    if x > CharPos[i][0] and x < CharPos[i][0] + CharPic[i].get_width() \
                        and y > CharPos[i][1] and y < CharPos[i][1] + CharPic[i].get_height() \
                        and controller.money['Defend'] >= defendcost[i] and (curTime - defendlastcd[i])/1000 >= defendneedcd[i]:
                        if Charsel == i:
                            Charsel = -1
                        else:
                            Charsel = i
                        Coorsel = [-1, -1]
                        Coorselold = [-1, -1]
                        Dirselstatus = False

                # 选取地图中的格子
                if x > mapload.xBegin and x < mapload.xBegin + mapload.columnNumber * mapload.blockSize \
                    and y > mapload.yBegin and y < mapload.yBegin + mapload.rowNumber * mapload.blockSize \
                    and Charsel >= 0:
                    Coorsel = mapload.positionToBlock([x,y])
                    if mapload.maps[Coorsel[0]][Coorsel[1]].canPlantOn and mapload.maps[Coorsel[0]][Coorsel[1]].isPlantOn == False:
                        Coorselold = Coorsel
                    else:
                        Coorsel = Coorselold

                # 选择朝向后放置防守角色
                for i in range(4):
                    if x > DirectionPos[i][0] and x < DirectionPos[i][0] + Direction[i].get_width() \
                            and y > DirectionPos[i][1] and y < DirectionPos[i][1] + Direction[i].get_height() \
                            and Dirselstatus:
                        if CharID[Charsel] == 0:
                            deffenders.append(CivilianDefender(controller,[(Coorsel[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (Coorsel[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            deffendersID.append(0)
                        if CharID[Charsel] == 1:
                            deffenders.append(AuraDefender(controller,[(Coorsel[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (Coorsel[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            deffendersID.append(1)
                        if CharID[Charsel] == 2:
                            deffenders.append(KamikazeDefender(controller,[(Coorsel[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (Coorsel[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            deffendersID.append(2)
                        if CharID[Charsel] == 3:
                            deffenders.append(FattyDefender(controller,[(Coorsel[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (Coorsel[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            deffendersID.append(3)
                        if CharID[Charsel] == 4:
                            deffenders.append(PharmacistDefender(controller,[(Coorsel[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (Coorsel[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            deffendersID.append(4)
                        controller.money['Defend'] -= defendcost[Charsel];
                        defendlastcd[Charsel] = curTime
                        Charsel = -1
                        Coorsel = [-1, -1]
                        Coorselold = [-1, -1]
                        Dirselstatus = False

            if event.type == COUNT:
                counts = counts + 1
                # clock
                curTime = pygame.time.get_ticks()
                timePast = (curTime - startTime) / 1000     # 计算过去的时间
                timeLeft = mapload.time_limit - int(timePast)
                # 记录上一帧时间
                lastTime = curTime
                life = mapload.fortress_HP      #家的生命值

                #   时间耗尽即可获胜
                if timeLeft <= 0:
                    endFight(screen, clock, modeID, mapID, True)
                    breakflag = 1

                if attackerorder < len(attackerplan[0]):
                    # 根据时间依次出怪
                    while attackerplan[0][attackerorder] <= timePast:
                        if attackerplan[1][attackerorder] == 1:
                            attackers.append(CivilianAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(0)
                        if attackerplan[1][attackerorder] == 2:
                            attackers.append(KamikazeAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(2)
                        if attackerplan[1][attackerorder] == 3:
                            attackers.append(AuraAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(1)
                        if attackerplan[1][attackerorder] == 4:
                            attackers.append(FattyAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(3)
                        elif attackerplan[1][attackerorder] == 5:
                            attackers.append(PharmacistAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(4)
                        attackerorder += 1
                        if attackerorder >= len(attackerplan[0]):
                            break
                        #if attackerorder >= len(attackerplan[0]):

                # 防守方攻击，攻击方死亡判定，每10帧攻击一次
                if counts % 10 == 0:
                    for i in range(len(deffenders)):
                        deffenders[i].attack()
                for attacker in attackers:
                    if attacker.hp <= 0:
                        # 角色死亡，将角色及对应编号移出列表
                        k = attackers.index(attacker)
                        attackers.remove(attacker)
                        del attackersID[k]
                # 攻击方移动，攻击，防守方死亡判定
                for i, attacker in enumerate(attackers):
                    # print("attackers[%d].position:%f,%f"%(1,attackers[1].position[0],attackers[1].position[1]))
                    attacker.move()
                    #   判定是否到家了
                    if update_direction(attacker, mapload):
                        k = attackers.index(attacker)
                        attackers.remove(attacker)
                        del attackersID[k]
                        if mapload.fortress_HP <= 0:
                            endFight(screen, clock, modeID, mapID, False)
                            breakflag = 1

                    if counts % 10 == 0:
                        attacker.attack()
                # 防守方死亡
                for deffender in deffenders:
                    if deffender.hp <= 0:
                        k = deffenders.index(deffender)
                        deffenders.remove(deffender)
                        del deffendersID[k]

                #   更新静态图
                # life = mapID.fortress_HP
                screen.blit(bg, (0, 0))
                screen.blit(infoPic, infoPos)
                screen.blit(timePic, timePos)
                screen.blit(lifePic, lifePos)
                screen.blit(costPic, costPos)
                screen.blit(Toolflame, ToolflamePos)
                # screen.blit(BattleMap, BattleMapPos)
                mapDisplay(mapload, screen)
                screen.blit(Giveup, GiveupPos)

                # the numbers
                screen.blit(font.render(str(timeLeft), True, (0, 0, 0)), (415, 20))
                screen.blit(font.render(str(mapload.fortress_HP), True, (0, 0, 0)), (665, 20))
                screen.blit(font.render(str(int(controller.money[controller.player_side])), True, (0, 0, 0)), (915, 20))

                for i in range(0, Charnum):
                    screen.blit(Charflame, CharPos[i])
                    if controller.money['Defend'] >= defendcost[i] and (curTime - defendlastcd[i])/1000 >= defendneedcd[i]:
                        screen.blit(CharPic[i], CharPos[i])
                    else:
                        screen.blit(CharPics[i], CharPos[i])
                # 更新防守方图片
                for deffender in deffenders:
                        x = deffender.position[0] - 0.5 * mapload.blockSize
                        y = deffender.position[1] - 0.5 * mapload.blockSize
                        k = deffenders.index(deffender)
                        screen.blit(DefendPic[deffendersID[k]], (x, y))
                        # print("The image location is : %f,%f"%(x,y))
                        # print("The attacks[%d]'s HP is : %d" % (i, attackers[i].hp))
                # 更新进攻方图片
                for attacker in attackers:
                        x = attacker.position[0] - 0.5 * mapload.blockSize
                        y = attacker.position[1] - 0.5 * mapload.blockSize
                        k = attackers.index(attacker)
                        screen.blit(AttackPic[attackersID[k]], (x, y))
                        # print("The image location is : %f,%f"%(x,y))
                        # print("The attacks[%d]'s HP is : %d" % (i, attackers[i].hp))

                # 更新朝向按键
                if Charsel >= 0 and Coorsel[0] >= 0 and Coorsel[1]>=0:
                    for i in range(4):
                        screen.blit(Direction[i], DirectionPos[i])
                    screen.blit(cancelPic, cancelPos)
                    Dirselstatus = True

                controller.update()

        # 更新画面
        pygame.display.update()

        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break