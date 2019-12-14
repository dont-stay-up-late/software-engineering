import pygame
import sys
from pygame.locals import *
from selectCharacters import *

# 选择地图
# modeID为游戏模式编号
def selectMap(screen, clock, modeID):
    background = (255, 255, 255)
    breakflag = 0
    # 地图编号
    # 判定是否要展示地图信息
    flagMapInfo = 0
    # 模式介绍路径，单人还是联机
    modeIntroAddress = path("res/pic/modeintro" + str(modeID) + ".png")

    # 图片及位置
    background = pygame.image.load(path("res/bg/bg_map.png")).convert()
    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)
    mapTitle = pygame.image.load(path("res/pic/mapselecttitle.png")).convert_alpha()
    mapTitlePos = (340, 0)
    #   地图信息
    modeIntro = pygame.image.load(modeIntroAddress).convert_alpha()
    modeIntroPos = (980, 0)
    #   地图编号
    mapNum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
    mapNum1Pos = (365, 250)
    mapNum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
    mapNum2Pos = (565, 250)
    mapNum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
    mapNum3Pos = (765, 250)
    mapNum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
    mapNum4Pos = (365, 450)
    mapNum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
    mapNum5Pos = (565, 450)
    mapNum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
    mapNum6Pos = (765, 450)
    sureButton = pygame.image.load(path("res/button/sure.png")).convert_alpha()
    surePos = (1080, 653)
    mapInfoPos = (0, 100)
    while True:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > mapNum1Pos[0] and x < mapNum1Pos[0] + mapNum1Button.get_width() \
                        and y > mapNum1Pos[1] and y < mapNum1Pos[1] + mapNum1Button.get_height():

                    #   地图选中特效
                    mapNum1Button = pygame.image.load(path("res/mapnum/Mapnum1_1.png")).convert_alpha()
                    mapNum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapNum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapNum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapNum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapNum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    # 地图信息
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_1info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    mapInfoPos = (0,150)
                    flagMapInfo = 1
                # shift picture

                if x > mapNum2Pos[0] and x < mapNum2Pos[0] + mapNum2Button.get_width() \
                        and y > mapNum2Pos[1] and y < mapNum2Pos[1] + mapNum2Button.get_height():
                    mapNum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapNum2Button = pygame.image.load(path("res/mapnum/Mapnum2_1.png")).convert_alpha()
                    mapNum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapNum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapNum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapNum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_2info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flagMapInfo = 2
                # shift picture

                if x > mapNum3Pos[0] and x < mapNum3Pos[0] + mapNum3Button.get_width() \
                        and y > mapNum3Pos[1] and y < mapNum3Pos[1] + mapNum3Button.get_height():
                    mapNum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapNum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapNum3Button = pygame.image.load(path("res/mapnum/Mapnum3_1.png")).convert_alpha()
                    mapNum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapNum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapNum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_3info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flagMapInfo = 3
                # shift picture

                if x > mapNum4Pos[0] and x < mapNum4Pos[0] + mapNum4Button.get_width() \
                        and y > mapNum4Pos[1] and y < mapNum4Pos[1] + mapNum4Button.get_height():
                    mapNum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapNum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapNum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapNum4Button = pygame.image.load(path("res/mapnum/Mapnum4_1.png")).convert_alpha()
                    mapNum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapNum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_4info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flagMapInfo = 4
                # shift picture

                if x > mapNum5Pos[0] and x < mapNum5Pos[0] + mapNum5Button.get_width() \
                        and y > mapNum5Pos[1] and y < mapNum5Pos[1] + mapNum5Button.get_height():
                    mapNum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapNum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapNum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapNum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapNum5Button = pygame.image.load(path("res/mapnum/Mapnum5_1.png")).convert_alpha()
                    mapNum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_5info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flagMapInfo = 5
                # shift picture

                if x > mapNum6Pos[0] and x < mapNum6Pos[0] + mapNum6Button.get_width() \
                        and y > mapNum6Pos[1] and y < mapNum6Pos[1] + mapNum6Button.get_height():
                    mapNum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapNum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapNum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapNum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapNum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapNum6Button = pygame.image.load(path("res/mapnum/Mapnum6_1.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_6info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flagMapInfo = 6
                # shift picture

                if x > surePos[0] and x < surePos[0] + sureButton.get_width() \
                        and y > surePos[1] and y < surePos[1] + sureButton.get_height() \
                        and flagMapInfo > 0:
                    selectCharacters(screen, clock, modeID, flagMapInfo)
                    breakflag = 1
                    # load game

                if x > backPos[0] and x < backPos[0] + backButton.get_width() \
                        and y > backPos[1] and y < backPos[1] + backButton.get_height():
                    from modeSelect import modeSelect
                    selectMode(screen, clock)
                    breakflag = 1
                    # here to come back

                elif x > homePos[0] and x < homePos[0] + homeButton.get_width() \
                        and y > homePos[1] and y < homePos[1] + homeButton.get_height():
                    from initMenu import initialMenu
                    initialMenu(screen, clock)
                    breakflag = 1
                    # here to come back home

        # 填充背景和内容
        screen.blit(background, (0, 0))
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        screen.blit(mapTitle, mapTitlePos)
        screen.blit(modeIntro, modeIntroPos)
        screen.blit(mapNum1Button,mapNum1Pos)
        screen.blit(mapNum2Button, mapNum2Pos)
        screen.blit(mapNum3Button, mapNum3Pos)
        screen.blit(mapNum4Button, mapNum4Pos)
        screen.blit(mapNum5Button, mapNum5Pos)
        screen.blit(mapNum6Button, mapNum6Pos)
        if flagMapInfo > 0:
            screen.blit(mapinfo, mapInfoPos)
            screen.blit(sureButton, surePos)
        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break


