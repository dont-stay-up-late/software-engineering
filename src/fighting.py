import pygame
import sys
from pygame.locals import *
from path import path

# modeID为游戏模式编号，mapID为地图编号, characters为选用的角色的列表
def startFight(screen, clock, modeID, mapID, CharID):
    bg = pygame.image.load(path("res/bg/bg_fighting.png")).convert_alpha()
    breakflag = 0
    cost = 0

    infoPic = pygame.image.load(path("res/battle/information.png")).convert_alpha()
    infoPos = (0,0)
    timePic = pygame.image.load(path("res/battle/time.png")).convert_alpha()
    timePos = (265,0)
    lifePic = pygame.image.load(path("res/battle/life.png")).convert_alpha()
    lifePos = (515,0)
    costPic = pygame.image.load(path("res/battle/Cost.png")).convert_alpha()
    costPos = (765,0)
    Toolflame = pygame.image.load(path("res/battle/tools.png")).convert_alpha()
    ToolflamePos = (1015, 0)
    BattleMap = pygame.image.load(path("res/battle/mapdisplay.png")).convert_alpha()
    BattleMapPos = (265, 70)
    Giveup = pygame.image.load(path("res/battle/giveup.png")).convert_alpha()
    GiveupPos = (1015, 570)
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
    for i in range (0,Charnum):
        CharPic.append(pygame.image.load(loadpathbs[CharID[i]]).convert_alpha())
        CharPos.append((640 - 37.5 * Charnum + i * 75, 570))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            # cost increase

            # for i in range (0,Charnum):
                # if cost > Char[CharID[i]].cost :
                    # CharPic[i] = pygame.image.load(loadpathb[CharID[i]]).convert_alpha()

            # clock


            # life




        screen.blit(bg, (0, 0))
        screen.blit(infoPic, infoPos)
        screen.blit(timePic, timePos)
        screen.blit(lifePic, lifePos)
        screen.blit(costPic, costPos)
        screen.blit(Toolflame, ToolflamePos)
        screen.blit(BattleMap, BattleMapPos)
        screen.blit(Giveup, GiveupPos)
        for i in range(0, Charnum):
            screen.blit(Charflame, CharPos[i])
            screen.blit(CharPic[i], CharPos[i])
        # 更新画面
        pygame.display.flip()
        # 帧率
        clock.tick(30)
        if breakflag == 1:
            break