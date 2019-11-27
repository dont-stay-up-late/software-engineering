import pygame
import sys
from pygame.locals import *
from path import path

# 选择角色
# modeID为游戏模式编号，mapID为地图编号
def selectCharacters(screen, clock, modeID, mapID):
    bg = (255, 255, 255)
    breakflag = 0
    infoflag = 0
    # 编队
    CharID = []
    Totalnum = 5
    Choosenum = 0
    CharflamePos = []
    CharPic0 = []
    CharPic = []
    loadpathb = []
    loadpathbs = []
    Charstatus = [1, 1, 1, 1, 1]
    modeintroadd = path("res/pic/modeintro" + str(modeID) + ".png")

    # 图片及位置
    if modeID == 1 or modeID == 3:
        bg = pygame.image.load(path("res/bg/bg_character_att.png")).convert()
        stringc = "r"
    else:
        bg = pygame.image.load(path("res/bg/bg_character_def.png")).convert()
        stringc = "b"

    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)
    startButton = pygame.image.load(path("res/button/sure.png")).convert_alpha()
    startPos = (1080, 653)
    CharTitle = pygame.image.load(path("res/pic/chartitle.png")).convert_alpha()
    CharTitlePos = (340, 0)
    modeIntro = pygame.image.load(modeintroadd).convert_alpha()
    modeintroPos = (980, 0)
    Charflame = pygame.image.load(path("res/character/charflame.png")).convert_alpha()
    Teamflame = pygame.image.load(path("res/character/teamflame.png")).convert_alpha()
    TeamflamePos = (255, 520)
    CharinfoPos = (0,150)
    loadpathb.append(path("res/character/pingminb.png"))
    loadpathb.append(path("res/character/gongtoub.png"))
    loadpathb.append(path("res/character/gansiduib.png"))
    loadpathb.append(path("res/character/pangdunb.png"))
    loadpathb.append(path("res/character/yaojishib.png"))
    loadpathbs.append(path("res/character/pingminbs.png"))
    loadpathbs.append(path("res/character/gongtoubs.png"))
    loadpathbs.append(path("res/character/gansiduibs.png"))
    loadpathbs.append(path("res/character/pangdunbs.png"))
    loadpathbs.append(path("res/character/yaojishibs.png"))
    for i in range (0, Totalnum):
        CharPic0.append(pygame.image.load(loadpathb[i]).convert_alpha())
        CharPic.append(pygame.image.load(loadpathb[i]).convert_alpha())
        CharflamePos.append((255 + i * 100, 250))
    while True:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > backPos[0] and x < backPos[0] + backButton.get_width() \
                        and y > backPos[1] and y < backPos[1] + backButton.get_height():
                    from selectMap import selectMap
                    selectMap(screen, clock, modeID)
                    breakflag = 1
                    # here to come back

                if x > homePos[0] and x < homePos[0] + homeButton.get_width() \
                        and y > homePos[1] and y < homePos[1] + homeButton.get_height():
                    from initMenu import initialMenu
                    initialMenu(screen, clock)
                    breakflag = 1
                    # here to come back home

                if x > startPos[0] and x < startPos[0] + startButton.get_width() \
                        and y > startPos[1] and y < startPos[1] + startButton.get_height():
                    from fighting import startFight
                    startFight(screen, clock, modeID, mapID, CharID)
                    breakflag = 1
                    # here to start the game

                for i in range (0, Totalnum):
                    if x > CharflamePos[i][0] and x < CharflamePos[i][0] + Charflame.get_width() \
                            and y > CharflamePos[i][1] and y < CharflamePos[i][1] + Charflame.get_height():
                        Charstatus[i] = -Charstatus[i]
                        Charinfo = pygame.image.load(path("res/charinfo/Charinfo.png")).convert_alpha()
                        infoflag = 1
                        if Charstatus[i] == 1:
                            CharPic[i] = pygame.image.load(loadpathb[i]).convert_alpha()
                            CharID.remove(i)
                            Choosenum = Choosenum - 1
                        else:
                            CharPic[i] = pygame.image.load(loadpathbs[i]).convert_alpha()
                            CharID.append(i)
                            Choosenum = Choosenum + 1

                for i in range (0, Choosenum):
                    if x > 255 + 100 * i and x < 255 + 100 * i + Charflame.get_width() \
                            and y > 520 and y < 520 + Charflame.get_height():
                        Charstatus[CharID[i]] = - Charstatus[CharID[i]]
                        Charinfo = pygame.image.load(path("res/charinfo/Charinfo.png")).convert_alpha()
                        if Charstatus[CharID[i]] == 1:
                            CharPic[CharID[i]] = pygame.image.load(loadpathb[CharID[i]]).convert_alpha()
                            del CharID[i]
                            Choosenum = Choosenum - 1

        # 填充背景和内容
        screen.blit(bg, (0, 0))
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        screen.blit(startButton, startPos)
        screen.blit(CharTitle, CharTitlePos)
        screen.blit(modeIntro, modeintroPos)
        screen.blit(Teamflame, TeamflamePos)
        if infoflag == 1:
            screen.blit(Charinfo, CharinfoPos)
        for i in range(0, Totalnum):
            screen.blit(Charflame, CharflamePos[i])
            screen.blit(CharPic[i], CharflamePos[i])
        for i in range(0, Choosenum):
            screen.blit(CharPic0[CharID[i]], (255 + 100 * i, 520))
        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.flip()
        # 帧率
        clock.tick(30)
        if breakflag == 1:
            break


