import pygame,sys,time
import math
from pygame.locals import *
from path import path
from map import *
from mapDisplay import *
from mapDisplayInitial import *
from models import *
from gamecontroller import *
from levelDefend import *
from levelAttack import *
from defeated import *
from fightResult import endFight
from bgm import playBgm
from equipments import *

# modeID为游戏模式编号，mapID为地图编号, charID为选用的角色的列表编号
def startFight(screen, clock, modeID, mapID, CharID):
    playBgm(2)
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
    PathwayOrder = 0
    attackerPlan = None
    attackerPlan2 = None
    try:
        attackerPlan = attackerload(mapID)[0]
        attackerPlan2 = attackerload(mapID)[1]
    except:
        pass
    # 读取防守计划文档并存储在对应的元组中
    defenderOrder = 0
    defenderPlan = None
    try:
        defenderPlan = defenderload(mapID)
    except:
        pass
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
    surePic = pygame.image.load(path("res/battle/sure.png")).convert_alpha()        #确认选择
    surePic = pygame.transform.scale(surePic,(130,50))
    surePos = (120, 540)
    cancelPic = pygame.image.load(path("res/battle/cancel.png")).convert_alpha()        #取消选择
    cancelPic = pygame.transform.scale(cancelPic,(130,50))
    cancelPos = (120, 630)
    giveupPos = (1080, 590)
    direction = []                                                                      #选择人物朝向
    directionPos = []
    directionPic = []                               #地图中的人物朝向
    directionPic.append(pygame.image.load(path("res/battle/up.png")).convert_alpha())
    directionPic.append(pygame.image.load(path("res/battle/left.png")).convert_alpha())
    directionPic.append(pygame.image.load(path("res/battle/down.png")).convert_alpha())
    directionPic.append(pygame.image.load(path("res/battle/right.png")).convert_alpha())
    # 选择框
    selectblock = pygame.image.load(path("res/battle/selectflameblock.png")).convert_alpha()
    selectcharacter = pygame.image.load(path("res/battle/selectflamechar.png")).convert_alpha()
    # 依次为上左下右，点击按键确定朝向
    for i in range(4):
        direction.append(pygame.image.load(path("res/battle/arrow"+str(i)+".png")).convert_alpha())
        direction[i] = pygame.transform.scale(direction[i],(50,50))
        directionPic[i] = pygame.transform.scale(directionPic[i],(75,75))
    directionPos.append((45, 545))
    directionPos.append((10, 585))
    directionPos.append((45, 625))
    directionPos.append((80, 585))
    # 道具
    tools = []
    toolsPos = []
    if modeID == 1:
        equipments = [
            DopingEquipment,
            IndifferentEquipment,
            SignalEquipment
        ]
    elif modeID == 2:
        equipments = [
            AmbulanceEquipment,
            CanonEquipment,
            ListEquipment
        ]
    canDefenderAttack = True # This can be modified by signal tool
    selectingAmbulanceTarget = False # Used by ambulance tool
    if modeID == 1:
        tools.append(pygame.image.load(path("res/tools/incitant.png")).convert_alpha())
        tools.append(pygame.image.load(path("res/tools/bombing.png")).convert_alpha())
        tools.append(pygame.image.load(path("res/tools/subwoofer.png")).convert_alpha())
    elif modeID == 2:
        tools.append(pygame.image.load(path("res/tools/ambulance.png")).convert_alpha())
        tools.append(pygame.image.load(path("res/tools/cannonry.png")).convert_alpha())
        tools.append(pygame.image.load(path("res/tools/urgentlist.png")).convert_alpha())
    for i in range(3):
        toolsPos.append((1095, 120 + i * 120))
    # 选择的道具ID
    toolselectID = -1
    toolselected = pygame.image.load(path("res/tools/selected.png")).convert_alpha()
    toolssurePos = (1085, 440)
    toolscancelPos = (1085, 500)
    # 不同角色的路径关键词缀
    stringOfCharacters = ["pingmin","gongtou","gansidui","pangdun","yaojishi", "bomb", "scientist", "bully", "fully"]
    characterFlame = pygame.image.load(path("res/battle/charflame.png")).convert_alpha()
    # 人物框
    characterNum = len(CharID)    # 选取的人物数量
    totolNum = 9   #人物总数
    characterPos = []
    # 上锁图与未上锁图
    characterUnlockedPic = []
    characterLockedPic = []
    # 防守方人物在地图中的图片
    defenderPic = []
    defenderPicLeft = []
    # 防守方人物准备攻击的图片
    defenderDetectPic = []
    defenderDetectPicLeft = []
    # 防守方人物攻击的图片
    defenderAttackPic = []
    defenderAttackPicLeft = []
    # 进攻方人物在地图中的图片
    attackerPic = []
    attackerPicLeft = []
    attackerPicOld = []
    # 进攻方人物准备攻击的图片,上下移动维持现状
    attackerDetectPic = []
    attackerDetectPicLeft = []
    attackerDetectPicOld = []
    # 进攻方人物攻击的图片
    attackerAttackPic = []
    attackerAttackPicLeft = []
    attackerAttackPicOld = []
    # 对应防守方人物最后放置的时间，单位为ms，下标为已选择的人物的编号
    defenderLastCD = []
    # 防守方人物所需要的费用
    defenderCost =[]
    # 防守方人物所需要的冷却
    defenderNeededCD =[]
    # 按人物编号所依次需要的费用和冷却
    defenderCostOfAll = [10,20,10,18,25,28, 25,19,22]
    defenderCdOfAll = [15,60,10,25,80,120, 50,28,20]
    # 对应进攻方人物最后放置的时间，单位为ms，下标为已选择的人物的编号
    attackerLastCD = []
    # 进攻方人物所需要的费用
    attackerCost =[]
    # 进攻方人物所需要的冷却
    attackerNeededCD =[]
    # 按人物编号所依次需要的费用和冷却
    attackerCostOfAll = [10,20,15,18,25,28,25,19,22]
    attackerCdOfAll = [10,30,10,25,80,90,50,18,25]
    # 选取的角色编号（为CharID列表中的下标，如果为-1，表示未选取）
    characterSelectedID = -1
    # 选取的坐标编号（取整数），[-1，-1]为未选取
    coordinateSelected = [-1, -1]
    # 上次选取的坐标编号，用于回退, 改进后不再需要
    # coordinateSelectedOld = [-1, -1]
    # 选取的方向，-1或者False表示未选取，0-3依次为上左下右
    directionSelected = [-1]
    directionSelectedStatus = False
    # 血量条
    hpPic = []
    for i in range(10):
        hpPic.append(pygame.image.load(path("res/hp/hp"+str(i)+".png")).convert_alpha())

    modeIDChar = 'r' # Attack by default
    if modeID == 2:
        modeIDChar = 'b'
    for i in range(0, characterNum):
        # 编队框人物解锁与未解锁图
        characterUnlockedPic.append(pygame.image.load(path("res/battle/"+stringOfCharacters[CharID[i]]+"{}.png".format(modeIDChar))).convert_alpha())
        characterLockedPic.append(pygame.image.load(path("res/battle/"+stringOfCharacters[CharID[i]]+"{}s.png".format(modeIDChar))).convert_alpha())
        characterPos.append((640 - 37.5 * characterNum + i * 75, 550))
        defenderCost.append(defenderCostOfAll[CharID[i]])
        defenderNeededCD.append(defenderCdOfAll[CharID[i]])
        defenderLastCD.append(startTime - defenderNeededCD[i] * 1000)
        attackerCost.append(attackerCostOfAll[CharID[i]])
        attackerNeededCD.append(attackerCdOfAll[CharID[i]])
        attackerLastCD.append(startTime - attackerNeededCD[i] * 1000)
    for i in range(totolNum):
        # 进攻与防守方人物贴图,默认朝右
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
    # 为了逻辑的合理性，所有角色默认朝向为右，朝左则进行翻转,只有左右需要进行更新
        defenderPicLeft.append(pygame.transform.flip(defenderPic[i], True, False))
        defenderDetectPicLeft.append(pygame.transform.flip(defenderDetectPic[i], True, False))
        defenderAttackPicLeft.append(pygame.transform.flip(defenderAttackPic[i], True, False))
        attackerPicLeft.append(pygame.transform.flip(attackerPic[i], True, False))
        attackerDetectPicLeft.append(pygame.transform.flip(attackerDetectPic[i], True, False))
        attackerAttackPicLeft.append(pygame.transform.flip(attackerAttackPic[i], True, False))
    # 地图准备
    mapload = levelLoad(mapID)
    # 地图图片
    mapImage = mapDisplayInitial(mapload, screen)
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

    selectmode = 0  # 区分目前的选择模式
    # 角色信息
    defendersInfomation = []
    attackersInfomation = []
    blocksInfomation = []
    for i in range(totolNum):
        defendersInfomation.append(pygame.image.load(path("res/fightinginfo/" + stringOfCharacters[i] + "b.png")).convert_alpha())
        attackersInfomation.append(pygame.image.load(path("res/fightinginfo/" + stringOfCharacters[i] + "r.png")).convert_alpha())
    charactersInfomationPos = (0, 0)

    for i in range(7):
        blocksInfomation.append(pygame.image.load(path("res/fightinginfo/" + str(i) + ".png")).convert_alpha())
    blocksInfomationPos = (0, 400)

    # 用于描述炸弹人状态的量
    # bombbborn = []
    # bombbcoordinate = []
    # bombrdie = []
    # bombrcoordinate = []
    bombbPic = pygame.image.load(path("res/character/bombb3.png")).convert_alpha()
    bombrPic = pygame.image.load(path("res/character/bombr3.png")).convert_alpha()
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
                    endFight(screen, clock, modeID, mapID, False, attackers, defenders, mapload, defendersID, attackersID, attackerPicOld, attackerDetectPicOld, attackerAttackPicOld)
                    breakflag = 1

                for i in range(characterNum):
                    #   选取人物，或者切换选取人物，都需要对坐标朝向等重置
                    if x > characterPos[i][0] and x < characterPos[i][0] + characterUnlockedPic[i].get_width() \
                        and y > characterPos[i][1] and y < characterPos[i][1] + characterUnlockedPic[i].get_height():
                        # if (modeID == 2 and controller.money['Defend'] >= defenderCost[i] and (curTime - defenderLastCD[i])/1000 >= defenderNeededCD[i]) \
                        #    or (modeID == 1 and controller.money['Attack'] >= attackerCost[i] and (curTime - attackerLastCD[i]) / 1000 >= attackerNeededCD[i]):
                        if selectmode == 1:
                            characterSelectedID = i
                        else:
                            if characterSelectedID == i:
                                characterSelectedID = -1
                            else:
                                characterSelectedID = i
                        coordinateSelected = [-1, -1]
                        # coordinateSelectedOld = [-1, -1]
                        directionSelectedStatus = False
                        selectmode = 0
                        selectingAmbulanceTarget = False
                        toolselectID = -1

                # 选取地图中的格子
                if x > mapload.xBegin and x < mapload.xBegin + mapload.rowNumber * mapload.blockSize \
                    and y > mapload.yBegin and y < mapload.yBegin + mapload.columnNumber * mapload.blockSize:
                    coordinateSelected = mapload.positionToBlock([x,y])

                    # Selecting ambulance target...
                    skip = False
                    if selectingAmbulanceTarget:
                        # Judge whether there is a defender on the block
                        target = None
                        target_k = None
                        for defender in defenders:
                            if defender.get_coordinate()[0] == coordinateSelected[0] and defender.get_coordinate()[1] == coordinateSelected[1]:
                                target = defender
                                break
                        if target is not None:
                            controller.money['Defend'] += target.cost // 2
                            target.die()
                            defenders.remove(target)
                            mapload.maps[mapload.positionToBlock([target.position[0], target.position[1]])[1]][
                                mapload.positionToBlock([target.position[0], target.position[1]])[
                                    0]].isPlantOn = False
                            del defendersID[defenders.index(target)]
                            selectingAmbulanceTarget = False
                            skip = True
                            coordinateSelected = [-1, -1]
                            toolselectID = -1

                    #if True:
                    if not skip and modeID == 2: # Defending
                        toolselectID = -1
                        if mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isPlantOn == False:
                            if selectmode == 1:
                                selectmode = 0
                                characterSelectedID = -1
                            # 只能查看地图上防守方角色信息，避免重合
                        else:
                            selectmode = 1
                            characterSelectedID = -1
                            directionSelectedStatus = False
                            for defender in defenders:
                                if defender.get_coordinate()[0] == coordinateSelected[0] and defender.get_coordinate()[1] == coordinateSelected[1]:
                                    characterSelectedID = defendersID[defenders.index(defender)]
                                    break

                    elif not skip and modeID == 1: # Attacking
                        toolselectID = -1
                        if mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isPlantOn == False:
                            if selectmode == 1:
                                selectmode = 0
                                characterSelectedID = -1
                        else:
                            selectmode = 1
                            characterSelectedID = -1
                            directionSelectedStatus = False
                            for defender in defenders:
                                if defender.get_coordinate()[0] == coordinateSelected[0] and defender.get_coordinate()[1] == coordinateSelected[1]:
                                    characterSelectedID = defendersID[defenders.index(defender)]
                                    break

                # 在防守模式下，选择朝向后放置防守角色
                if modeID == 2:
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
                            if CharID[characterSelectedID] == 5:
                                defenders.append(BombDefender(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                                (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                                defendersID.append(5)
                            if CharID[characterSelectedID] == 6:
                                defenders.append(ScientistDefender(controller, [(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                                            (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                                defendersID.append(6)
                            if CharID[characterSelectedID] == 7:
                                defenders.append(BullyDefender(controller, [(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                        (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                                defendersID.append(7)
                            if CharID[characterSelectedID] == 8:
                                defenders.append(IdiotDefender(controller, [(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                        (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], i))
                                defendersID.append(8)
                                # bombbborn.append(time.time())
                                # bombbcoordinate.append((coordinateSelected[0]*mapload.blockSize+mapload.xBegin,coordinateSelected[1]*mapload.blockSize+mapload.yBegin))

                            mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isPlantOn = True
                            controller.money['Defend'] -= defenderCost[characterSelectedID]
                            defenderLastCD[characterSelectedID] = curTime
                            characterSelectedID = -1
                            coordinateSelected = [-1, -1]
                            # coordinateSelectedOld = [-1, -1]
                            directionSelectedStatus = False
                    if x > cancelPos[0] and x < cancelPos[0] + cancelPic.get_width() \
                        and y > cancelPos[1] and y < cancelPos[1] + cancelPic.get_height() \
                        and directionSelectedStatus:
                        characterSelectedID = -1
                        coordinateSelected = [-1, -1]
                        # coordinateSelectedOld = [-1, -1]
                        directionSelectedStatus = False
                elif modeID == 1:
                    if x > surePos[0] and x < surePos[0] + surePic.get_width() \
                        and y > surePos[1] and y < surePos[1] + surePic.get_height():
                        if directionSelectedStatus:
                            if CharID[characterSelectedID] == 0:
                                attackers.append(CivilianAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(0)
                            if CharID[characterSelectedID] == 1:
                                attackers.append(AuraAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(1)
                            if CharID[characterSelectedID] == 2:
                                attackers.append(KamikazeAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(2)
                            if CharID[characterSelectedID] == 3:
                                attackers.append(FattyAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(3)
                            if CharID[characterSelectedID] == 4:
                                attackers.append(PharmacistAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(4)
                            if CharID[characterSelectedID] == 5:
                                attackers.append(BombAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(5)
                            if CharID[characterSelectedID] == 6:
                                attackers.append(ScientistAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(6)
                            if CharID[characterSelectedID] == 7:
                                attackers.append(BullyAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(7)
                            if CharID[characterSelectedID] == 8:
                                attackers.append(IdiotAttacker(controller,[(coordinateSelected[0] + 0.5) * mapload.blockSize + mapload.xBegin, \
                                    (coordinateSelected[1] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                                attackersID.append(8)

                            attackerPicOld.append(attackerPic[CharID[characterSelectedID]])
                            attackerAttackPicOld.append(attackerAttackPic[CharID[characterSelectedID]])
                            attackerDetectPicOld.append(attackerDetectPic[CharID[characterSelectedID]])
                            controller.money['Attack'] -= attackerCost[characterSelectedID]
                            attackerLastCD[characterSelectedID] = curTime
                            characterSelectedID = -1
                            coordinateSelected = [-1, -1]
                            # coordinateSelectedOld = [-1, -1]
                            directionSelectedStatus = False # This is actually necessary.
                        elif coordinateSelected[0] >= 0 and coordinateSelected[1]>=0 and mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isPathway:
                            kk = len(mapload.Pathways)
                            for mm in range(kk):
                                if mapload.Pathways[mm][0] == coordinateSelected[1] and  mapload.Pathways[mm][1] == coordinateSelected[0]:
                                    if timePast - mapload.PathwaysShiftTime[mm] >= mapload.PathwayCD:
                                        mapload.update_Pathway(coordinateSelected, mapload.maps[coordinateSelected[1]][coordinateSelected[0]].blockDirection)
                                        mapload.PathwaysShiftTime[mm] = timePast
                                        characterSelectedID = -1
                                        coordinateSelected = [-1, -1]
                                        # coordinateSelectedOld = [-1, -1]
                                        directionSelectedStatus = False
                                    break

                    if x > cancelPos[0] and x < cancelPos[0] + cancelPic.get_width() \
                        and y > cancelPos[1] and y < cancelPos[1] + cancelPic.get_height():
                        characterSelectedID = -1
                        coordinateSelected = [-1, -1]
                        # coordinateSelectedOld = [-1, -1]
                        directionSelectedStatus = False

                # 使用道具
                for i in range(3):
                    if x > toolsPos[i][0] and x < toolsPos[i][0] + tools[i].get_width() \
                        and y > toolsPos[i][1] and y < toolsPos[i][1] + tools[i].get_height():
                        characterSelectedID = -1
                        toolselectID = i
                        equipment = equipments[i]
                        if equipment == AmbulanceEquipment:
                            selectingAmbulanceTarget = True
                        elif equipment == ListEquipment:
                            _ = equipment(controller, defenderLastCD)
                        else:
                            _ = equipment(controller)
                        break
            if event.type == COUNT:
                counts = counts + 1
                # clock
                curTime = pygame.time.get_ticks()
                timePast = (curTime - startTime) / 1000     # 计算过去的时间
                timeLeft = mapload.time_limit - int(timePast)
                # 记录上一帧时间
                lastTime = curTime
                life = mapload.fortress_HP      #家的生命值

                #   对防守模式而言，时间耗尽即可获胜；对进攻方，则表示失败
                if timeLeft <= 0:
                    if modeID == 2:
                        endFight(screen, clock, modeID, mapID, True, attackers, defenders, mapload, defendersID, attackersID, attackerPicOld, attackerDetectPicOld, attackerAttackPicOld)
                    else:
                        endFight(screen, clock, modeID, mapID, False, attackers, defenders, mapload, defendersID, attackersID, attackerPicOld, attackerDetectPicOld, attackerAttackPicOld)
                    breakflag = 1

                if modeID == 2 and attackerOrder < len(attackerPlan[0]):
                    # 根据时间依次出怪
                    while attackerPlan[0][attackerOrder] <= timePast:
                        if attackerPlan[1][attackerOrder] == 0:
                            attackers.append(CivilianAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(0)
                        elif attackerPlan[1][attackerOrder] == 1:
                            attackers.append(AuraAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(1)
                        elif attackerPlan[1][attackerOrder] == 2:
                            attackers.append(KamikazeAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(2)
                        elif attackerPlan[1][attackerOrder] == 3:
                            attackers.append(FattyAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(3)
                        elif attackerPlan[1][attackerOrder] == 4:
                            attackers.append(PharmacistAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder]-1][1] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (mapload.bornPoints[attackerPlan[2][attackerOrder]-1][0] + 0.5) * mapload.blockSize + mapload.yBegin], 0))
                            attackersID.append(4)
                        elif attackerPlan[1][attackerOrder] == 5:
                            attackers.append(BombAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder] - 1][1] + 0.5) * mapload.blockSize + mapload.xBegin, (mapload.bornPoints[ \
                                                                                  attackerPlan[2][attackerOrder] - 1][0] + 0.5) * mapload.blockSize + mapload.yBegin],0))
                            attackersID.append(5)
                        elif attackerPlan[1][attackerOrder] == 6:
                            attackers.append(ScientistAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder] - 1][1] + 0.5) * mapload.blockSize + mapload.xBegin, (mapload.bornPoints[ \
                                                                                  attackerPlan[2][attackerOrder] - 1][0] + 0.5) * mapload.blockSize + mapload.yBegin],0))
                            attackersID.append(6)
                        elif attackerPlan[1][attackerOrder] == 7:
                            attackers.append(BullyAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder] - 1][1] + 0.5) * mapload.blockSize + mapload.xBegin, (mapload.bornPoints[ \
                                                                                  attackerPlan[2][attackerOrder] - 1][0] + 0.5) * mapload.blockSize + mapload.yBegin],0))
                            attackersID.append(7)
                        elif attackerPlan[1][attackerOrder] == 8:
                            attackers.append(IdiotAttacker(controller, [(mapload.bornPoints[attackerPlan[2][attackerOrder] - 1][1] + 0.5) * mapload.blockSize + mapload.xBegin, (mapload.bornPoints[ \
                                                                                  attackerPlan[2][attackerOrder] - 1][0] + 0.5) * mapload.blockSize + mapload.yBegin],0))
                            attackersID.append(8)
                        attackerPicOld.append(attackerPic[attackerPlan[1][attackerOrder]])
                        attackerAttackPicOld.append(attackerAttackPic[attackerPlan[1][attackerOrder]])
                        attackerDetectPicOld.append(attackerDetectPic[attackerPlan[1][attackerOrder]])
                        attackerOrder += 1
                        if attackerOrder >= len(attackerPlan[0]):
                            break
                        #if attackerorder >= len(attackerplan[0]):
                if modeID == 2 and PathwayOrder < len(attackerPlan2[0]):
                    # 根据时间调整轨道
                    while attackerPlan2[0][PathwayOrder] <= timePast:

                        mapload.update_Pathway((attackerPlan2[2][PathwayOrder],attackerPlan2[1][PathwayOrder]),mapload.maps[attackerPlan2[1][PathwayOrder]][attackerPlan2[2][PathwayOrder]].blockDirection)
                        PathwayOrder += 1
                        if PathwayOrder >= len(attackerPlan2[0]):
                            break
                        # if attackerorder >= len(attackerplan[0]):
                if modeID == 1 and defenderOrder < len(defenderPlan[0]):
                    # 根据时间依次出怪
                    while defenderPlan[0][defenderOrder] <= timePast:
                        # x = defenderPlan[2][defenderOrder]
                        # y = defenderPlan[3][defenderOrder]
                        # flag = False
                        # for defender in defenders:
                        #     if defender.position == [x, y]:
                        #         flag = True
                        #         break
                        # if flag:
                        #     defenderOrder += 1
                        #     continue
                        if defenderPlan[1][defenderOrder] == 0:
                            defenders.append(CivilianDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin], defenderPlan[4][defenderOrder]))
                            defendersID.append(0)
                        elif defenderPlan[1][defenderOrder] == 1:
                            defenders.append(AuraDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin], defenderPlan[4][defenderOrder]))
                            defendersID.append(1)
                        elif defenderPlan[1][defenderOrder] == 2:
                            defenders.append(KamikazeDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin], defenderPlan[4][defenderOrder]))
                            defendersID.append(2)
                        elif defenderPlan[1][defenderOrder] == 3:
                            defenders.append(FattyDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin], defenderPlan[4][defenderOrder]))
                            defendersID.append(3)
                        elif defenderPlan[1][defenderOrder] == 4:
                            defenders.append(PharmacistDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                           (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin], defenderPlan[4][defenderOrder]))
                            defendersID.append(4)
                        elif defenderPlan[1][defenderOrder] == 5:
                            defenders.append(BombDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin], defenderPlan[4][defenderOrder]))
                            defendersID.append(5)

                        elif defenderPlan[1][defenderOrder] == 6:
                            defenders.append(ScientistDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                            (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin],defenderPlan[4][defenderOrder]))
                            defendersID.append(6)
                            # bombbborn.append(time.time())
                            # bombbcoordinate.append((defenderPlan[2][defenderOrder] * mapload.blockSize + mapload.xBegin, defenderPlan[3][defenderOrder] * mapload.blockSize + mapload.yBegin))
                        elif defenderPlan[1][defenderOrder] == 7:
                            defenders.append(BullyDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                            (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin],defenderPlan[4][defenderOrder]))
                            defendersID.append(7)
                        elif defenderPlan[1][defenderOrder] == 8:
                            defenders.append(IdiotDefender(controller, [(defenderPlan[2][defenderOrder] + 0.5) * mapload.blockSize + mapload.xBegin,
                                                                            (defenderPlan[3][defenderOrder] + 0.5) * mapload.blockSize + mapload.yBegin],defenderPlan[4][defenderOrder]))
                            defendersID.append(8)
                        mapload.maps[defenderPlan[3][defenderOrder]][defenderPlan[2][defenderOrder]].isPlantOn = True
                        defenderOrder += 1
                        if defenderOrder >= len(defenderPlan[0]):
                            break

                # 防守方攻击，攻击方死亡判定，每10帧攻击一次
                if SignalEquipment.on:
                    canDefenderAttack = False
                else:
                    canDefenderAttack = True
                for i in range(len(defenders)):
                    if canDefenderAttack:
                        defenders[i].attack()

                # 攻击方移动，攻击，防守方死亡判定
                for i, attacker in enumerate(attackers):
                    # print("attackers[%d].position:%f,%f"%(1,attackers[1].position[0],attackers[1].position[1]))
                    if mapload.maps[mapload.positionToBlock([attacker.position[0],attacker.position[1]])[1]][mapload.positionToBlock([attacker.position[0],attacker.position[1]])[0]].isPlantOn == False:
                        attacker.move()
                    #   判定是否到家了
                    if update_direction(attacker, mapload):
                        k = attackers.index(attacker)
                        attackers.remove(attacker)
                        attacker.die()
                        del attackerPicOld[k]
                        del attackerDetectPicOld[k]
                        del attackerAttackPicOld[k]
                        del attackersID[k]
                        if mapload.fortress_HP <= 0:
                            if modeID == 2:
                                endFight(screen, clock, modeID, mapID, False, attackers, defenders, mapload, defendersID, attackersID, attackerPicOld, attackerDetectPicOld, attackerAttackPicOld)
                            else:
                                endFight(screen, clock, modeID, mapID, True, attackers, defenders, mapload, defendersID, attackersID, attackerPicOld, attackerDetectPicOld, attackerAttackPicOld)
                            breakflag = 1

                    attacker.attack()
                # 在判断死亡前，先update以发动技能
                for attacker in attackers:
                    attacker.update()
                for defender in defenders:
                    defender.update()
                # 同步双方列表
                for attacker in attackers:
                     if attacker not in Attacker.attackers:
                        k = attackers.index(attacker)
                        attackers.remove(attacker)
                        del attackerPicOld[k]
                        del attackerDetectPicOld[k]
                        del attackerAttackPicOld[k]
                        del attackersID[k]
                for defender in defenders:
                    if defender not in Defender.defenders:
                        k = defenders.index(defender)
                        defenders.remove(defender)
                        mapload.maps[mapload.positionToBlock([defender.position[0], defender.position[1]])[1]][mapload.positionToBlock([defender.position[0], defender.position[1]])[0]].isPlantOn = False
                        del defendersID[k]
                # 攻击方死亡
                for attacker in attackers:
                    if attacker.hp <= 0:
                        # 角色死亡，将角色及对应编号移出列表
                        k = attackers.index(attacker)
                        attackers.remove(attacker)
                        del attackerPicOld[k]
                        del attackerDetectPicOld[k]
                        del attackerAttackPicOld[k]
                        attacker.die()
                        del attackersID[k]
                # 防守方死亡
                for defender in defenders:
                    if defender.hp <= 0:
                        k = defenders.index(defender)
                        mapload.maps[mapload.positionToBlock([defender.position[0],defender.position[1]])[1]][mapload.positionToBlock([defender.position[0],defender.position[1]])[0]].isPlantOn = False
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
                mapDisplay(mapload, screen, mapImage)
                screen.blit(giveupButton, giveupPos)

                # the numbers
                screen.blit(font.render(str(timeLeft), True, (0, 0, 0)), (415, 20))
                screen.blit(font.render(str(mapload.fortress_HP), True, (0, 0, 0)), (665, 20))
                screen.blit(font.render(str(int(controller.money[controller.player_side])), True, (0, 0, 0)), (915, 20))

                # 更新道具图
                for i in range(3):
                    if equipments[i].count > 0:
                        screen.blit(tools[i], toolsPos[i])
                if modeID == 2 and toolselectID == 0:
                    screen.blit(toolselected, toolsPos[toolselectID])
                    # screen.blit(surePic, toolssurePos)
                    # screen.blit(cancelPic, toolscancelPos)


                for i in range(0, characterNum):
                    screen.blit(characterFlame, characterPos[i])
                    if (modeID == 2 and controller.money['Defend'] >= defenderCost[i] and (curTime - defenderLastCD[i])/1000 >= defenderNeededCD[i]) \
                        or (modeID == 1 and controller.money['Attack'] >= attackerCost[i] and (curTime - attackerLastCD[i]) / 1000 >= attackerNeededCD[i]):
                        screen.blit(characterUnlockedPic[i], characterPos[i])
                    else:
                        screen.blit(characterLockedPic[i], characterPos[i])
                # 更新防守方图片
                for defender in defenders:
                        x = defender.position[0] - 0.5 * mapload.blockSize
                        y = defender.position[1] - 0.5 * mapload.blockSize
                        k = defenders.index(defender)
                        screen.blit(directionPic[defender.direction], (x, y))
                        hpPicIndex = min(int((defender.hp - 1) // (defender.HP * 0.1)), 9)
                        if hpPicIndex < 0:
                            hpPicIndex = 0
                        if defendersID[k] == 5:     #炸弹人动画需要单独演示
                            if defender.direction == 1:
                                if time.time()-defender.last_created_time >= 1.0 and time.time()-defender.last_created_time <= 1.3:
                                    screen.blit(defenderAttackPicLeft[defendersID[k]],(x+10,y+10))
                                elif time.time()-defender.last_created_time >= 0.5 and time.time()-defender.last_created_time <= 1.0:
                                    screen.blit(defenderDetectPicLeft[defendersID[k]], (x + 10, y + 10))
                                elif time.time()-defender.last_created_time >= 0.0 and defender.last_created_time <= 0.5:
                                    screen.blit(defenderPicLeft[defendersID[k]], (x + 10, y + 10))
                                elif time.time()-defender.last_created_time >= 1.3 and time.time()-defender.last_created_time <= 1.5:
                                    screen.blit(bombbPic, (x, y))
                                screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                            else:
                                if time.time()-defender.last_created_time >= 1.0 and time.time()-defender.last_created_time <= 1.3:
                                    screen.blit(defenderAttackPic[defendersID[k]],(x+10,y+10))
                                elif time.time()-defender.last_created_time >= 0.5 and time.time()-defender.last_created_time <= 1.0:
                                    screen.blit(defenderDetectPic[defendersID[k]], (x + 10, y + 10))
                                elif time.time()-defender.last_created_time >= 0.0 and time.time()-defender.last_created_time <= 0.5:
                                    screen.blit(defenderPic[defendersID[k]], (x + 10, y + 10))
                                elif time.time()-defender.last_created_time >= 1.3 and time.time()-defender.last_created_time <= 1.5:
                                    screen.blit(bombbPic, (x + 20, y + 10))
                                screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))

                        else:
                            if defender.attacking_flag == False:
                                if counts % 20 <= 9:
                                    if defender.direction == 1:
                                        screen.blit(defenderPicLeft[defendersID[k]], (x - 2 + 10, y + 10))
                                    else:
                                        screen.blit(defenderPic[defendersID[k]], (x - 2 + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 2, y - 6))
                                else:
                                    if defender.direction == 1:
                                        screen.blit(defenderPicLeft[defendersID[k]], (x + 2 + 10, y + 10))
                                    else:
                                        screen.blit(defenderPic[defendersID[k]], (x + 2 + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 6, y - 6))
                            else:
                                if counts % (defender.attack_time * 40)  < defender.attack_time * 40 / 2:
                                    if defender.direction == 1:
                                        screen.blit(defenderDetectPicLeft[defendersID[k]], (x + 10, y + 10))
                                    else:
                                        screen.blit(defenderDetectPic[defendersID[k]], (x + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                                else:
                                    if defender.direction == 1:
                                        screen.blit(defenderAttackPicLeft[defendersID[k]], (x + 10, y + 10))
                                    else:
                                        screen.blit(defenderAttackPic[defendersID[k]], (x + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))

                            # print("The image location is : %f,%f"%(x,y))
                            # print("The attacks[%d]'s HP is : %d" % (i, attackers[i].hp))
                # 更新进攻方图片
                for attacker in attackers:
                        x = attacker.position[0] - 0.5 * mapload.blockSize
                        y = attacker.position[1] - 0.5 * mapload.blockSize
                        k = attackers.index(attacker)
                        screen.blit(directionPic[attacker.direction], (x, y))
                        hpPicIndex = min(int((attacker.hp - 1) // (attacker.HP * 0.1)), 9)
                        if hpPicIndex < 0:
                            hpPicIndex = 0
                        if attackersID == 5:
                            if attacker.hp >= 20:
                                if attacker.attacking_flag == False:
                                    if counts % 20 <= 12:
                                        if attacker.direction == 1:
                                            screen.blit(attackerPicLeft[attackersID[k]], (x + 10, y + 10))
                                            attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                        elif attacker.direction == 3:
                                            screen.blit(attackerPic[attackersID[k]], (x + 10, y + 10))
                                            attackerPicOld[k] = attackerPic[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                        else:
                                            screen.blit(attackerPicOld[k], (x + 10, y + 10))
                                        screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                                    else:
                                        if attacker.direction == 1:
                                            screen.blit(attackerPicLeft[attackersID[k]], (x + 10, y - 4 + 10))
                                            attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                        elif attacker.direction == 3:
                                            screen.blit(attackerPic[attackersID[k]], (x + 10, y - 4 + 10))
                                            attackerPicOld[k] = attackerPic[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                        else:
                                            screen.blit(attackerPicOld[k], (x + 10, y - 4 + 10))
                                        screen.blit(hpPic[hpPicIndex], (x + 4, y - 9))
                                else:
                                    if counts % (attacker.attack_time * 40) < attacker.attack_time * 40 / 2:
                                        if attacker.direction == 1:
                                            screen.blit(attackerDetectPicLeft[attackersID[k]], (x + 10, y + 10))
                                            attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                        elif attacker.direction == 3:
                                            screen.blit(attackerDetectPic[attackersID[k]], (x + 10, y + 10))
                                            attackerPicOld[k] = attackerPic[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                        else:
                                            screen.blit(attackerDetectPicOld[k], (x + 10, y + 10))
                                        screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                                    else:
                                        if attacker.direction == 1:
                                            screen.blit(attackerAttackPicLeft[attackersID[k]], (x + 10, y + 10))
                                            attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                        elif attacker.direction == 3:
                                            screen.blit(attackerAttackPic[attackersID[k]], (x + 10, y + 10))
                                            attackerPicOld[k] = attackerPic[attackersID[k]]
                                            attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                            attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                        else:
                                            screen.blit(attackerAttackPicOld[k], (x + 10, y + 10))
                                        screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                            elif attacker.hp >= 15 :
                                if attacker.direction == 1:
                                    screen.blit(attackerPicLeft[attackersID[k]], (x + 10, y + 10))
                                    attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                    attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                    attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                elif attacker.direction == 3:
                                    screen.blit(attackerPic[attackersID[k]], (x + 10, y + 10))
                                    attackerPicOld[k] = attackerPic[attackersID[k]]
                                    attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                    attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                else:
                                    screen.blit(attackerPicOld[k], (x + 10, y + 10))
                                screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                            elif attacker.hp >= 10:
                                if counts % (attacker.attack_time * 40) < attacker.attack_time * 40 / 2:
                                    if attacker.direction == 1:
                                        screen.blit(attackerDetectPicLeft[attackersID[k]], (x + 10, y + 10))
                                        attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                        attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                        attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                    elif attacker.direction == 3:
                                        screen.blit(attackerDetectPic[attackersID[k]], (x + 10, y + 10))
                                        attackerPicOld[k] = attackerPic[attackersID[k]]
                                        attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                        attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                    else:
                                        screen.blit(attackerDetectPicOld[k], (x + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                            elif attacker.hp >= 5:
                                if attacker.direction == 1:
                                    screen.blit(attackerAttackPicLeft[attackersID[k]], (x + 10, y + 10))
                                    attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                    attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                    attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                elif attacker.direction == 3:
                                    screen.blit(attackerAttackPic[attackersID[k]], (x + 10, y + 10))
                                    attackerPicOld[k] = attackerPic[attackersID[k]]
                                    attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                    attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                else:
                                    screen.blit(attackerAttackPicOld[k], (x + 10, y + 10))
                                screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                            elif attacker.hp >= 0:
                                screen.blit(bombrPic, (x + 20 ,y + 10))

                        else:
                            if attacker.attacking_flag == False:
                                if counts % 20 <= 12:
                                    if attacker.direction == 1:
                                        screen.blit(attackerPicLeft[attackersID[k]], (x + 10, y + 10))
                                        attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                    elif attacker.direction == 3:
                                        screen.blit(attackerPic[attackersID[k]], (x + 10, y + 10))
                                        attackerPicOld[k] = attackerPic[attackersID[k]]
                                    else:
                                        screen.blit(attackerPicOld[k], (x + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                                else:
                                    if attacker.direction == 1:
                                        screen.blit(attackerPicLeft[attackersID[k]], (x + 10, y - 4 + 10))
                                        attackerPicOld[k] = attackerPicLeft[attackersID[k]]
                                    elif attacker.direction == 3:
                                        screen.blit(attackerPic[attackersID[k]], (x + 10, y - 4 + 10))
                                        attackerPicOld[k] = attackerPic[attackersID[k]]
                                    else:
                                        screen.blit(attackerPicOld[k], (x + 10, y - 4 + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 4, y - 9))
                            else:
                                if counts % (attacker.attack_time * 40) < attacker.attack_time * 40 / 2:
                                    if attacker.direction == 1:
                                        screen.blit(attackerDetectPicLeft[attackersID[k]], (x + 10, y + 10))
                                        attackerDetectPicOld[k] = attackerDetectPicLeft[attackersID[k]]
                                    elif attacker.direction == 3:
                                        screen.blit(attackerDetectPic[attackersID[k]], (x + 10, y + 10))
                                        attackerDetectPicOld[k] = attackerDetectPic[attackersID[k]]
                                    else:
                                        screen.blit(attackerDetectPicOld[k], (x + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                                else:
                                    if attacker.direction == 1:
                                        screen.blit(attackerAttackPicLeft[attackersID[k]], (x + 10, y + 10))
                                        attackerAttackPicOld[k] = attackerAttackPicLeft[attackersID[k]]
                                    elif attacker.direction == 3:
                                        screen.blit(attackerAttackPic[attackersID[k]], (x + 10, y + 10))
                                        attackerAttackPicOld[k] = attackerAttackPic[attackersID[k]]
                                    else:
                                        screen.blit(attackerAttackPicOld[k], (x + 10, y + 10))
                                    screen.blit(hpPic[hpPicIndex], (x + 4, y - 6))
                        # print("The image location is : %f,%f"%(x,y))
                        # print("The attackers's HP is : %d" % (attacker.hp))
                # 进行轨道切换确认
                if modeID == 1 and coordinateSelected[0] >= 0 and coordinateSelected[1]>=0 and mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isPathway:
                    characterSelectedID = -1
                    selectmode = 0
                    screen.blit(cancelPic, cancelPos)
                    screen.blit(surePic, surePos)
                # 更新左侧信息
                if modeID == 2:
                    if selectmode == 0:
                        if characterSelectedID >= 0:
                            screen.blit(selectcharacter, characterPos[characterSelectedID])
                            screen.blit(defendersInfomation[CharID[characterSelectedID]], charactersInfomationPos)
                            # 更新数值
                            # 选择的人物卡
                            if CharID[characterSelectedID] == 0:
                                screen.blit(font.render(str(CivilianDefender.HP) + "/" + str(CivilianDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(CivilianDefender.ATTACK_POWER), True, (112, 76, 29)), (80, 132))
                                screen.blit(font.render(str(CivilianDefender.DEFEND_POWER), True, (112, 76, 29)), (210, 132))
                                screen.blit(font.render(str(CivilianDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(CivilianDefender.ATTACK_SPEED), True, (112, 76, 29)), (210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0,int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID])/1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s", True, (112, 76, 29)),(130, 222))
                            elif CharID[characterSelectedID] == 1:
                                screen.blit(font.render(str(AuraDefender.HP) + "/" + str(AuraDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(AuraDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(AuraDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(AuraDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(AuraDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 2:
                                screen.blit(font.render(str(KamikazeDefender.HP) + "/" + str(KamikazeDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(KamikazeDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(KamikazeDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(KamikazeDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(KamikazeDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 3:
                                screen.blit(font.render(str(FattyDefender.HP) + "/" + str(FattyDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(FattyDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(FattyDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(FattyDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(FattyDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 4:
                                screen.blit(font.render(str(PharmacistDefender.HP) + "/" + str(PharmacistDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(PharmacistDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(PharmacistDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(PharmacistDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(PharmacistDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                                screen.blit(font.render(str(PharmacistDefender.SPECIAL_INTERVAL) + "/" + str(PharmacistDefender.SPECIAL_INTERVAL), True, (112, 76, 29)), (130, 370))
                            elif CharID[characterSelectedID] == 5:
                                screen.blit(font.render(str(BombDefender.HP) + "/" + str(BombDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(BombDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(BombDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(BombDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(BombDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 6:
                                screen.blit(font.render(str(ScientistDefender.HP) + "/" + str(ScientistDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(ScientistDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(ScientistDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(ScientistDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(ScientistDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                                screen.blit(font.render(str(ScientistDefender.SPECIAL_INTERVAL) + "/" + str(ScientistDefender.SPECIAL_INTERVAL), True, (112, 76, 29)), (130, 370))
                            elif CharID[characterSelectedID] == 7:
                                screen.blit(font.render(str(BullyDefender.HP) + "/" + str(BullyDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(BullyDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(BullyDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(BullyDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(BullyDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 8:
                                screen.blit(font.render(str(IdiotDefender.HP) + "/" + str(IdiotDefender.HP), True, (112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(IdiotDefender.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(IdiotDefender.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(IdiotDefender.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(IdiotDefender.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                    else:
                        # 选择的是地图中的防守方
                        if characterSelectedID >= 0:
                            screen.blit(defendersInfomation[characterSelectedID], charactersInfomationPos)
                            for defender in defenders:
                                if defender.get_coordinate()[0] == coordinateSelected[0] and defender.get_coordinate()[1] == coordinateSelected[1]:
                                    screen.blit(font.render(str(int(defender.hp)) + "/" + str(defender.HP), True,(112, 76, 29)), (80, 102))
                                    screen.blit(font.render(str(int(defender.attack_power)), True, (112, 76, 29)),(80, 132))
                                    screen.blit(font.render(str(int(defender.defend_power)), True, (112, 76, 29)),(210, 132))
                                    screen.blit(font.render(str(int(defender.speed)), True, (112, 76, 29)),(80, 162))
                                    screen.blit(font.render(str(1 / defender.attack_time), True, (112, 76, 29)),(210, 162))
                                    screen.blit(font.render(str(defender.cost), True, (112, 76, 29)),(80, 192))
                                    for kk in range(characterNum):
                                        if CharID[kk] == characterSelectedID:
                                            CDLEFT = max(0, int(math.ceil(defenderNeededCD[kk] - ( curTime - defenderLastCD[kk]) / 1000)))
                                            screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[kk]) + "s", True,(112, 76, 29)), (130, 222))

                                    if characterSelectedID == 4:
                                        CDLEFT = max(0, int(math.ceil(PharmacistDefender.SPECIAL_INTERVAL) - (time.time() - defender.last_special_time)))
                                        screen.blit(font.render(str(CDLEFT) + "/" + str(PharmacistDefender.SPECIAL_INTERVAL), True, (112, 76, 29)), (130, 370))

                                    if characterSelectedID == 6:
                                        CDLEFT = max(0, int(math.ceil(ScientistDefender.SPECIAL_INTERVAL) - (time.time() - defender.last_special_time)))
                                        screen.blit(font.render(str(CDLEFT) + "/" + str(ScientistDefender.SPECIAL_INTERVAL), True, (112, 76, 29)), (130, 370))

                else:
                    if selectmode == 0:
                        #选择的是人物卡
                        if characterSelectedID >= 0:
                            screen.blit(selectcharacter, characterPos[characterSelectedID])
                            screen.blit(attackersInfomation[CharID[characterSelectedID]], charactersInfomationPos)
                            # 更新数值
                            if CharID[characterSelectedID] == 0:
                                screen.blit(font.render(str(CivilianAttacker.HP) + "/" + str(CivilianDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(CivilianAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(CivilianAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(CivilianAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(CivilianAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s", True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 1:
                                screen.blit(font.render(str(AuraAttacker.HP) + "/" + str(AuraDefender.HP), True, (112, 76, 29)),(80, 102))
                                screen.blit(font.render(str(AuraAttacker.ATTACK_POWER), True, (112, 76, 29)), (80, 132))
                                screen.blit(font.render(str(AuraAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(AuraAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(AuraAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 2:
                                screen.blit(font.render(str(KamikazeAttacker.HP) + "/" + str(KamikazeDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(KamikazeAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(KamikazeAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(KamikazeAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(KamikazeAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 3:
                                screen.blit(font.render(str(FattyAttacker.HP) + "/" + str(FattyDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(FattyAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(FattyAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(FattyAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(FattyAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 4:
                                screen.blit(font.render(str(PharmacistAttacker.HP) + "/" + str(PharmacistDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(PharmacistAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(PharmacistAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(PharmacistAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(PharmacistAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                                screen.blit(font.render(str(PharmacistAttacker.SPECIAL_INTERVAL) + "/" + str(PharmacistAttacker.SPECIAL_INTERVAL), True, (112, 76, 29)), (130, 370))
                            elif CharID[characterSelectedID] == 5:
                                screen.blit(font.render(str(BombAttacker.HP) + "/" + str(BombDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(BombAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(BombAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(BombAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(BombAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 6:
                                screen.blit(font.render(str(ScientistAttacker.HP) + "/" + str(ScientistDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(ScientistAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(ScientistAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(ScientistAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(ScientistAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                                screen.blit(font.render(str(ScientistAttacker.SPECIAL_INTERVAL) + "/" + str(ScientistAttacker.SPECIAL_INTERVAL), True, (112, 76, 29)), (130, 370))
                            elif CharID[characterSelectedID] == 7:
                                screen.blit(font.render(str(BullyAttacker.HP) + "/" + str(BullyDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(BullyAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(BullyAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(BullyAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(BullyAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))
                            elif CharID[characterSelectedID] == 8:
                                screen.blit(font.render(str(IdiotAttacker.HP) + "/" + str(IdiotDefender.HP), True,(112, 76, 29)), (80, 102))
                                screen.blit(font.render(str(IdiotAttacker.ATTACK_POWER), True, (112, 76, 29)),(80, 132))
                                screen.blit(font.render(str(IdiotAttacker.DEFEND_POWER), True, (112, 76, 29)),(210, 132))
                                screen.blit(font.render(str(IdiotAttacker.SPEED), True, (112, 76, 29)), (80, 162))
                                screen.blit(font.render(str(IdiotAttacker.ATTACK_SPEED), True, (112, 76, 29)),(210, 162))
                                screen.blit(font.render(str(defenderCost[characterSelectedID]), True, (112, 76, 29)),(80, 192))
                                CDLEFT = max(0, int(math.ceil(defenderNeededCD[characterSelectedID] - (curTime - defenderLastCD[characterSelectedID]) / 1000)))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[characterSelectedID]) + "s",True, (112, 76, 29)), (130, 222))


                    else:
                        # 选择的是地图中的防守方
                        if characterSelectedID >= 0:
                            screen.blit(defendersInfomation[characterSelectedID],charactersInfomationPos)
                            for defender in defenders:
                                if defender.get_coordinate()[0] == coordinateSelected[0] and defender.get_coordinate()[1] == coordinateSelected[1]:
                                    screen.blit(font.render(str(int(defender.hp)) + "/" + str(defender.HP), True,(112, 76, 29)), (80, 102))
                                    screen.blit(font.render(str(int(defender.attack_power)), True, (112, 76, 29)),(80, 132))
                                    screen.blit(font.render(str(int(defender.defend_power)), True, (112, 76, 29)),(210, 132))
                                    screen.blit(font.render(str(int(defender.speed)), True, (112, 76, 29)),(80, 162))
                                    screen.blit(font.render(str(1 / defender.attack_time), True, (112, 76, 29)),(210, 162))
                                    screen.blit(font.render(str(defender.cost), True, (112, 76, 29)),(80, 192))
                                    for kk in range(characterNum):
                                        if CharID[kk] == characterSelectedID:
                                            CDLEFT = max(0, int(math.ceil(defenderNeededCD[kk] - (curTime - defenderLastCD[kk]) / 1000)))
                                            screen.blit(font.render(str(CDLEFT) + "/" + str(defenderNeededCD[kk]) + "s", True,(112, 76, 29)), (130, 222))

                                        if characterSelectedID == 4:
                                            CDLEFT = max(0, int(math.ceil(PharmacistDefender.SPECIAL_INTERVAL) - (time.time() - defender.last_special_time)))
                                            screen.blit(font.render(str(CDLEFT) + "/" + str(PharmacistDefender.SPECIAL_INTERVAL),True, (112, 76, 29)), (130, 370))


                                        if characterSelectedID == 6:
                                            CDLEFT = max(0, int(math.ceil(ScientistDefender.SPECIAL_INTERVAL) - (time.time() - defender.last_special_time)))
                                            screen.blit(font.render(str(CDLEFT) + "/" + str(ScientistDefender.SPECIAL_INTERVAL),True, (112, 76, 29)), (130, 370))

                if coordinateSelected[0] >= 0 and coordinateSelected[1] >= 0:
                    if mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isHome:
                        screen.blit(blocksInfomation[4], blocksInfomationPos)
                    elif mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isBornPoint:
                        screen.blit(blocksInfomation[5], blocksInfomationPos)
                    elif mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isPathway:
                        screen.blit(blocksInfomation[6], blocksInfomationPos)
                        kk = len(mapload.Pathways)
                        for mm in range(kk):
                            if mapload.Pathways[mm][0] == coordinateSelected[1] and mapload.Pathways[mm][1] == coordinateSelected[0]:
                                CDLEFT = max(0, int(math.ceil(mapload.PathwayCD - (timePast-  mapload.PathwaysShiftTime[mm]))))
                                screen.blit(font.render(str(CDLEFT) + "/" + str(mapload.PathwayCD), True,(112, 76, 29)), (192, 464))
                                break

                    elif mapload.maps[coordinateSelected[1]][coordinateSelected[0]].canZombieOn:
                        if mapload.maps[coordinateSelected[1]][coordinateSelected[0]].canPlantOn:
                            screen.blit(blocksInfomation[0], blocksInfomationPos)
                        else:
                            screen.blit(blocksInfomation[1], blocksInfomationPos)
                    else:
                        if mapload.maps[coordinateSelected[1]][coordinateSelected[0]].canPlantOn:
                            screen.blit(blocksInfomation[2], blocksInfomationPos)
                        else:
                            screen.blit(blocksInfomation[3], blocksInfomationPos)
                    screen.blit(selectblock, (mapload.blockToPosition([coordinateSelected[0], coordinateSelected[1]])[0] - 37.5,mapload.blockToPosition([coordinateSelected[0], coordinateSelected[1]])[1] - 37.5))


                if modeID == 2 and characterSelectedID >= 0 and coordinateSelected[0] >= 0 and coordinateSelected[1]>=0 and selectmode == 0 \
                    and mapload.maps[coordinateSelected[1]][coordinateSelected[0]].canPlantOn \
                    and controller.money['Defend'] >= defenderCost[characterSelectedID] and (curTime - defenderLastCD[characterSelectedID]) / 1000 >= defenderNeededCD[characterSelectedID] :

                    for i in range(4):
                        screen.blit(direction[i], directionPos[i])
                    screen.blit(cancelPic, cancelPos)
                    directionSelectedStatus = True

                if modeID == 1 and selectmode == 0 and characterSelectedID >= 0 and coordinateSelected[0] >= 0 and coordinateSelected[1]>=0 \
                    and mapload.maps[coordinateSelected[1]][coordinateSelected[0]].isBornPoint \
                    and controller.money['Attack'] >= attackerCost[characterSelectedID] and (curTime - attackerLastCD[characterSelectedID]) / 1000 >=attackerNeededCD[characterSelectedID]:
                    screen.blit(cancelPic, cancelPos)
                    screen.blit(surePic, surePos)
                    directionSelectedStatus = True
                controller.update()





        # 更新画面
        pygame.display.update()

        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break
