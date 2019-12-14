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
    background = pygame.image.load(path("res/bg/bg_fighting.png")).convert_alpha()
    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    breakflag = 0
    startTime = pygame.time.get_ticks()
    lastTime = startTime
    # 计时准备(后面要和Time统一）
    COUNT = pygame.USEREVENT + 1
    pygame.time.set_timer(COUNT, 25)  # 每0.025秒发一次
    counts = 0
    # 读取进攻计划文档并存储在对应的元组中
    attackerOrder = 0
    attackerPlan = attackerload(mapID)
    # 初始化界面
    infoPic = pygame.image.load(path("res/battle/information.png")).convert_alpha()     #信息
    infoPos = (0, 0)
    timePic = pygame.image.load(path("res/battle/time.png")).convert_alpha()            #倒计时
    timePos = (265, 0)
    lifePic = pygame.image.load(path("res/battle/life.png")).convert_alpha()            #防守方生命值
    lifePos = (515, 0)
    costPic = pygame.image.load(path("res/battle/Cost.png")).convert_alpha()            #防守方金钱
    costPos = (765, 0)
    toolFlame = pygame.image.load(path("res/battle/tools.png")).convert_alpha()         #道具
    toolFlamePos = (1015, 0)
    battleMap = pygame.image.load(path("res/battle/mapdisplay.png")).convert_alpha()    #地图
    battleMapPos = (265, 70)
    giveupButton = pygame.image.load(path("res/battle/giveup.png")).convert_alpha()           #弃权
    cancelPic = pygame.image.load(path("res/battle/cancel.png")).convert_alpha()        #取消选择
    cancelPic = pygame.transform.scale(cancelPic,(140,50))
    cancelPos = (85, 520)
    giveupPos = (1080, 630)
    direction = []                                                                      #选择人物朝向
    directionPos = []
    # 依次为上左下右，点击按键确定朝向
    for i in range(4):
        direction.append(pygame.image.load(path("res/battle/arrow"+str(i)+".png")).convert_alpha())
        direction[i] = pygame.transform.scale(direction[i],(50,50))
    directionPos.append((130,350))
    directionPos.append((85, 400))
    directionPos.append((130, 450))
    directionPos.append((175, 400))

    # 不同角色的路径关键词缀
    stringOfCharacters = ["pingmin","gongtou","gansidui","pangdun","yaojishi"]
    characterFlame = pygame.image.load(path("res/battle/charflame.png")).convert_alpha()
    # 人物框
    characterNum = len(CharID)
    characterPos = []
    # 上锁图与未上锁图
    characterUnlockedPic = []
    characterLockedPic = []
    # 防守方人物在地图中的图片
    defenderPic = []
    # 防守方人物准备攻击的图片
    defenderDetectPic = []
    # 防守方人物攻击的图片
    defenderAttackPic = []
    # 进攻方人物在地图中的图片
    attackerPic = []
    # 进攻方人物准备攻击的图片
    attackerDetectPic = []
    # 进攻方人物攻击的图片
    attackerAttackPic = []
    # 对应防守方人物最后放置的时间，单位为ms，下标为已选择的人物的编号
    defenderLastCD = []
    # 防守方人物所需要的费用
    defenderCost =[]
    # 防守方人物所需要的冷却
    defenderNeededCD =[]
    # 按人物编号所依次需要的费用和冷却
    costOfAll = [10,20,15,18,20]
    cdOfAll = [15,80,15,25,60]
    # 选取的角色编号（为CharID列表中的下标，如果为-1，表示未选取）
    characterSelectedID = -1
    # 选取的坐标编号（取整数），[-1，-1]为未选取
    coordinateSelected = [-1, -1]
    # 上次选取的坐标编号，用于回退
    coordinateSelectedOld = [-1, -1]
    # 选取的方向，-1或者False表示未选取，0-3依次为上左下右
    directionSelected = [-1]
    directionSelectedStatus = False
    # 血量条
    hpPic = []
    for i in range(10):
        hpPic.append(pygame.image.load(path("res/hp/hp"+str(i)+".png")).convert_alpha())

    for i in range(0, characterNum):
        # 编队框人物解锁与未解锁图
        characterUnlockedPic.append(pygame.image.load(path("res/battle/"+stringOfCharacters[CharID[i]]+"b.png")).convert_alpha())
        characterLockedPic.append(pygame.image.load(path("res/battle/"+stringOfCharacters[CharID[i]]+"bs.png")).convert_alpha())
        characterPos.append((640 - 37.5 * characterNum + i * 75, 550))
        defenderCost.append(costOfAll[CharID[i]])
        defenderNeededCD.append(cdOfAll[CharID[i]])
        defenderLastCD.append(startTime - defenderNeededCD[i] * 1000)
    for i in range(5):
        # 进攻与防守方人物贴图
        defenderPic.append(pygame.image.load(path("res/character/" + stringOfCharacters[i] + "b0.png")).convert_alpha())
        defenderDetectPic.append(pygame.image.load(path("res/character/" + stringOfCharacters[i] + "b1.png")).convert_alpha())
        defenderAttackPic.append(pygame.image.load(path("res/character/" + stringOfCharacters[i] + "b2.png")).convert_alpha())
        defenderPic[i] = pygame.transform.scale(defenderPic[i], (55, 55))
        defenderDetectPic[i] = pygame.transform.scale(defenderDetectPic[i], (55, 55))
        defenderAttackPic[i] = pygame.transform.scale(defenderAttackPic[i], (55, 55))
        attackerPic.append(pygame.image.load(path("res/character/" + stringOfCharacters[i] + "r0.png")).convert_alpha())
        attackerDetectPic.append(pygame.image.load(path("res/character/" + stringOfCharacters[i] + "r1.png")).convert_alpha())
        attackerAttackPic.append(pygame.image.load(path("res/character/" + stringOfCharacters[i] + "r2.png")).convert_alpha())
        attackerPic[i] = pygame.transform.scale(attackerPic[i], (55, 55))
        attackerDetectPic[i] = pygame.transform.scale(attackerDetectPic[i], (55, 55))
        attackerAttackPic[i] = pygame.transform.scale(attackerAttackPic[i], (55, 55))
    # 为了逻辑的合理性，所有角色默认朝向为左，朝右则进行翻转

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
    defenders = []
    defendersID = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                #   放弃，失败
                if x > giveupPos[0] and x < giveupPos[0] + giveupButton.get_width() \
                    and y > giveupPos[1] and y < giveupPos[1] + giveupButton.get_height():
                    endFight(screen, clock, modeID, mapID, False)
                    breakflag = 1

                for i in range(characterNum):
                    #   选取人物，或者切换选取人物，都需要对坐标朝向等重置
                    if x > characterPos[i][0] and x < characterPos[i][0] + characterUnlockedPic[i].get_width() \
                        and y > characterPos[i][1] and y < characterPos[i][1] + characterUnlockedPic[i].get_height() \
                        and controller.money['Defend'] >= defenderCost[i] and (curTime - defenderLastCD[i])/1000 >= defenderNeededCD[i]:
                        if characterSelectedID == i:
                            characterSelectedID = -1
                        else:
                            characterSelectedID = i
                        coordinateSelected = [-1, -1]
                        coordinateSelectedOld = [-1, -1]
                        directionSelectedStatus = False

                # 选取地图中的格子
                if x > mapload.xBegin and x < mapload.xBegin + mapload.rowNumber * mapload.blockSize \
                    and y > mapload.yBegin and y < mapload.yBegin + mapload.columnNumber * mapload.blockSize \
                    and characterSelectedID >= 0:
                    coordinateSelected = mapload.positionToBlock([x,y])
                    #if True:
                    if mapload.maps[coordinateSelected[1]][coordinateSelected[0]].canPlantOn and mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isPlantOn == False:
                        coordinateSelectedOld = coordinateSelected
                    else:
                        coordinateSelected = coordinateSelectedOld

                # 选择朝向后放置防守角色
                for i in range(4):
                    if x > directionPos[i][0] and x < directionPos[i][0] + direction[i].get_width() \
                            and y > directionPos[i][1] and y < directionPos[i][1] + direction[i].get_height() \
                            and directionSelectedStatus:
                        if CharID[characterSelectedID] == 0:
                            defenders.append(CivilianDefender(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            defendersID.append(0)
                        if CharID[characterSelectedID] == 1:
                            defenders.append(AuraDefender(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            defendersID.append(1)
                        if CharID[characterSelectedID] == 2:
                            defenders.append(KamikazeDefender(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            defendersID.append(2)
                        if CharID[characterSelectedID] == 3:
                            defenders.append(FattyDefender(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            defendersID.append(3)
                        if CharID[characterSelectedID] == 4:
                            defenders.append(PharmacistDefender(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                            defendersID.append(4)
                        controller.money['Defend'] -= defenderCost[characterSelectedID];
                        defenderLastCD[characterSelectedID] = curTime
                        characterSelectedID = -1
                        coordinateSelected = [-1, -1]
                        coordinateSelectedOld = [-1, -1]
                        directionSelectedStatus = False

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

                if attackerOrder < len(attackerPlan[0]):
                    # 根据时间依次出怪
                    while attackerPlan[0][attackerOrder] <= timePast:
                        if attackerPlan[1][attackerOrder] == 0:
                            attackers.append(CivilianAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(0)
                        if attackerPlan[1][attackerOrder] == 1:
                            attackers.append(AuraAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(1)
                        if attackerPlan[1][attackerOrder] == 2:
                            attackers.append(KamikazeAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(2)
                        if attackerPlan[1][attackerOrder] == 3:
                            attackers.append(FattyAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(3)
                        elif attackerPlan[1][attackerOrder] == 4:
                            attackers.append(PharmacistAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(4)
                        attackerOrder += 1
                        if attackerOrder >= len(attackerPlan[0]):
                            break
                        #if attackerorder >= len(attackerplan[0]):

                # 防守方攻击，攻击方死亡判定，每10帧攻击一次
                for i in range(len(defenders)):
                    defenders[i].attack()

                # 攻击方移动，攻击，防守方死亡判定
                for i, attacker in enumerate(attackers):
                    # print("attackers[%d].position:%f,%f"%(1,attackers[1].position[0],attackers[1].position[1]))
                    attacker.move()
                    #   判定是否到家了
                    if update_direction(attacker, mapload):
                        k = attackers.index(attacker)
                        attackers.remove(attacker)
                        attacker.die()
                        del attackersID[k]
                        if mapload.fortress_HP <= 0:
                            endFight(screen, clock, modeID, mapID, False)
                            breakflag = 1

                    attacker.attack()
                # 在判断死亡前，先update以发动技能
                for attacker in attackers:
                    attacker.update()
                for defender in defenders:
                    defender.update()
                # 攻击方死亡
                for attacker in attackers:
                    if attacker.hp <= 0:
                        # 角色死亡，将角色及对应编号移出列表
                        k = attackers.index(attacker)
                        attackers.remove(attacker)
                        attacker.die()
                        del attackersID[k]
                # 防守方死亡
                for defender in defenders:
                    if defender.hp <= 0:
                        k = defenders.index(defender)
                        defenders.remove(defender)
                        defender.die()
                        del defendersID[k]

                #   更新静态图
                # life = mapID.fortress_HP
                screen.blit(background, (0, 0))
                screen.blit(infoPic, infoPos)
                screen.blit(timePic, timePos)
                screen.blit(lifePic, lifePos)
                screen.blit(costPic, costPos)
                screen.blit(toolFlame, toolFlamePos)
                # screen.blit(BattleMap, BattleMapPos)
                mapDisplay(mapload, screen)
                screen.blit(giveupButton, giveupPos)

                # the numbers
                screen.blit(font.render(str(timeLeft), True, (0, 0, 0)), (415, 20))
                screen.blit(font.render(str(mapload.fortress_HP), True, (0, 0, 0)), (665, 20))
                screen.blit(font.render(str(int(controller.money[controller.player_side])), True, (0, 0, 0)), (915, 20))

                for i in range(0, characterNum):
                    screen.blit(characterFlame, characterPos[i])
                    if controller.money['Defend'] >= defenderCost[i] and (curTime - defenderLastCD[i])/1000 >= defenderNeededCD[i]:
                        screen.blit(characterUnlockedPic[i], characterPos[i])
                    else:
                        screen.blit(characterLockedPic[i], characterPos[i])
                # 更新防守方图片
                for defender in defenders:
                        x = defender.position[0] - 0.5 * mapload.blockSize
                        y = defender.position[1] - 0.5 * mapload.blockSize
                        k = defenders.index(defender)
                        if defender.attacking_flag == False:
                            if counts % 20 <= 9:
                                screen.blit(defenderPic[defendersID[k]], (x - 2 + 10, y + 10))
                                screen.blit(hpPic[min(int((defender.hp - 1) // (defender.HP * 0.1)), 9)], (x + 2, y - 6))
                            else:
                                screen.blit(defenderPic[defendersID[k]], (x + 2 + 10, y + 10))
                                screen.blit(hpPic[min(int((defender.hp - 1) // (defender.HP * 0.1)), 9)], (x + 6, y - 6))
                        else:
                            if counts % 20 <= 9:
                                screen.blit(defenderDetectPic[defendersID[k]], (x + 10, y + 10))
                                screen.blit(hpPic[min(int((defender.hp - 1) // (defender.HP * 0.1)), 9)], (x + 4, y - 6))
                            else:
                                screen.blit(defenderAttackPic[defendersID[k]], (x + 10, y + 10))
                                screen.blit(hpPic[min(int((defender.hp - 1) // (defender.HP * 0.1)), 9)], (x + 4, y - 6))

                        # print("The image location is : %f,%f"%(x,y))
                        # print("The attacks[%d]'s HP is : %d" % (i, attackers[i].hp))
                # 更新进攻方图片
                for attacker in attackers:
                        x = attacker.position[0] - 0.5 * mapload.blockSize
                        y = attacker.position[1] - 0.5 * mapload.blockSize
                        k = attackers.index(attacker)
                        if attacker.attacking_flag == False:
                            if counts % 20 <= 12:
                                screen.blit(attackerPic[attackersID[k]], (x + 10, y + 10))
                                screen.blit(hpPic[min(int((attacker.hp - 1) // (attacker.HP * 0.1)), 9)], (x + 4, y - 6))
                            else:
                                screen.blit(attackerPic[attackersID[k]], (x + 10, y - 4 + 10))
                                screen.blit(hpPic[min(int((attacker.hp - 1) // (attacker.HP * 0.1)), 9)], (x + 4, y - 9))
                        else:
                            if counts % 20 <= 9:
                                screen.blit(attackerDetectPic[attackersID[k]], (x + 10, y + 10))
                                screen.blit(hpPic[min(int((attacker.hp - 1) // (attacker.HP * 0.1)), 9)], (x + 4, y - 6))
                            else:
                                screen.blit(attackerAttackPic[attackersID[k]], (x + 10, y + 10))
                                screen.blit(hpPic[min(int((attacker.hp - 1) // (attacker.HP * 0.1)), 9)], (x + 4, y - 6))
                        # print("The image location is : %f,%f"%(x,y))
                        # print("The attackers's HP is : %d" % (attacker.hp))

                # 更新朝向按键
                if characterSelectedID >= 0 and coordinateSelected[0] >= 0 and coordinateSelected[1]>=0:
                    for i in range(4):
                        screen.blit(direction[i], directionPos[i])
                    screen.blit(cancelPic, cancelPos)
                    directionSelectedStatus = True

                controller.update()

        # 更新画面
        pygame.display.update()

        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break