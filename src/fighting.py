import pygame,sys,time
from pygame.locals import *
from path import path
from map import *
from mapDisplay import *
from models import *
from gamecontroller import *
from levelDefend import *
from defeated import *


# modeID为游戏模式编号，mapID为地图编号, characters为选用的角色的列表
def startFight(screen, clock, modeID, mapID, CharID):
    bg = pygame.image.load(path("res/bg/bg_fighting.png")).convert_alpha()
    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    breakflag = 0
    startTime = pygame.time.get_ticks()
    lastTime = startTime
    # 计时准备(后面要和Time统一）
    COUNT = pygame.USEREVENT + 1
    pygame.time.set_timer(COUNT, 25)  # 每0.025秒发一次
    counts = 0
    attackerorder = 0
    attackerplan = attackerload(mapID)
    # 初始化界面
    infoPic = pygame.image.load(path("res/battle/information.png")).convert_alpha()
    infoPos = (0, 0)
    timePic = pygame.image.load(path("res/battle/time.png")).convert_alpha()
    timePos = (265, 0)
    lifePic = pygame.image.load(path("res/battle/life.png")).convert_alpha()
    lifePos = (515, 0)
    costPic = pygame.image.load(path("res/battle/Cost.png")).convert_alpha()
    costPos = (765, 0)
    Toolflame = pygame.image.load(path("res/battle/tools.png")).convert_alpha()
    ToolflamePos = (1015, 0)
    BattleMap = pygame.image.load(path("res/battle/mapdisplay.png")).convert_alpha()
    BattleMapPos = (265, 70)
    Giveup = pygame.image.load(path("res/battle/giveup.png")).convert_alpha()
    GiveupPos = (1080, 630)
    loadpathb = []
    loadpathbs = []
    loadpathb.append(path("res/battle/pingminb.png"))
    loadpathb.append(path("res/battle/gongtoub.png"))
    loadpathb.append(path("res/battle/gansiduib.png"))
    loadpathb.append(path("res/battle/pangdunb.png"))
    loadpathb.append(path("res/battle/yaojishib.png"))
    loadpathbs.append(path("res/battle/pingminbs.png"))
    loadpathbs.append(path("res/battle/gongtoubs.png"))
    loadpathbs.append(path("res/battle/gansiduibs.png"))
    loadpathbs.append(path("res/battle/pangdunbs.png"))
    loadpathbs.append(path("res/battle/yaojishibs.png"))
    Charflame = pygame.image.load(path("res/battle/charflame.png")).convert_alpha()
    Charnum = len(CharID)
    CharPos = []
    CharPic = []
    defendcd = []
    defendlastcd = []
    defendcost =[]
    defendneedcd =[]
    costall = [10,15,18,20,80]
    cdall = [15,15,25,60,80]
    for i in range(0, Charnum):
        CharPic.append(pygame.image.load(loadpathbs[CharID[i]]).convert_alpha())
        CharPos.append((640 - 37.5 * Charnum + i * 75, 550))
        defendcd.append(0)
        defendcost.append(costall[CharID[i]])
        defendneedcd.append(cdall[CharID[i]])
        defendlastcd.append(startTime - defendneedcd[i])
    # 地图准备
    mapload = levelLoad(mapID)
    if modeID == 2:
        controller = GameController(mapID, mapload, 'Single', 'Defend')
    else:
        # need to be change
        controller = GameController(mapID, mapload)

    # 角色准备，测试
    attackers = []
    deffenders = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > GiveupPos[0] and x < GiveupPos[0] + Giveup.get_width() \
                    and y > GiveupPos[1] and y < GiveupPos[1] + Giveup.get_height():
                    # defeated(screen, clock, modeID, mapID)
                    breakflag = 1
                # here to come back home

            if event.type == COUNT:
                counts = counts + 1
                # clock
                curTime = pygame.time.get_ticks()
                timePast = (curTime - startTime) / 1000
                timeLeft = mapload.time_limit - int(timePast)
                # 记录上一帧时间
                lastTime = curTime
                life = map.fortress_HP


                while attackerplan[0][attackerorder] <= timePast:
                    if attackerplan[1][attackerorder] == 1:
                        attackers.append(CivilianAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                       (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                    if attackerplan[1][attackerorder] == 2:
                        attackers.append(KamikazeAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                       (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                    if attackerplan[1][attackerorder] == 3:
                        attackers.append(AuraAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                       (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                    if attackerplan[1][attackerorder] == 4:
                        attackers.append(FattyAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                       (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                    elif attackerplan[1][attackerorder] == 5:
                        attackers.append(PharmacistAttacker(controller, [(mapload.bornPoints[attackerplan[2][attackerorder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                       (mapload.bornPoints[attackerplan[2][attackerorder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                    attackerorder += 1

                # 防守方攻击，攻击方死亡判定
                if counts % 10 == 0:
                    for i in range(len(deffenders)):
                        deffenders[i].attack()
                for attacker in attackers:
                    if attacker.hp <= 0:
                        attackers.remove(attacker)
                # 攻击方移动，攻击，防守方死亡判定
                for i, attacker in enumerate(attackers):
                    if i == 1 and counts < 200:
                        break
                    if i == 2 and counts < 400:
                        break
                    # print("attackers[%d].position:%f,%f"%(1,attackers[1].position[0],attackers[1].position[1]))
                    attacker.move()
                    if update_direction(attacker, mapload):
                        attackers.remove(attacker)
                        if map.fortress_HP <= 0:
                            # defeated(screen, clock, modeID, mapID)
                            breakflag = 1

                    if counts % 10 == 0:
                        attacker.attack()
                for deffender in deffenders:
                    if deffender.hp <= 0:
                        deffenders.remove(deffender)

                for i in range(0, Charnum):
                    if controller.money['Defend'] > defendcost[i] and curTime - defendlastcd[i] > defendneedcd[i]:
                        CharPic[i] = pygame.image.load(loadpathb[CharID[i]]).convert_alpha()

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
                    screen.blit(CharPic[i], CharPos[i])


                for attackeri in attackers:
                        x = attackeri.position[0] - 0.5 * mapload.blockSize
                        y = attackeri.position[1] - 0.5 * mapload.blockSize
                        attackerImage = pygame.image.load(path(attackeri.filename)).convert_alpha()
                        attackerImage = pygame.transform.scale(attackerImage,(75,75))
                        screen.blit(attackerImage, (x, y))
                        # print("The image location is : %f,%f"%(x,y))
                        # print("The attacks[%d]'s HP is : %d" % (i, attackers[i].hp))
                controller.update()

        # 更新画面
        pygame.display.update()

        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break