import pygame
import sys
from pygame.locals import *
from selectCharacters import *

# 选择地图
# modeID为游戏模式编号
def selectMap(screen, clock, modeID):
    bg = (255, 255, 255)
    breakflag = 0
    # 地图编号
    flag_mapinfo = 0
    modeintroadd = path("res/pic/modeintro" + str(modeID) + ".png")

    # 图片及位置
    bg = pygame.image.load(path("res/bg/bg_map.png")).convert()
    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)
    mapTitle = pygame.image.load(path("res/pic/mapselecttitle.png")).convert_alpha()
    mapTitlePos = (340, 0)
    modeIntro = pygame.image.load(modeintroadd).convert_alpha()
    modeintroPos = (980, 0)
    mapnum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
    mapnum1Pos = (365, 250)
    mapnum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
    mapnum2Pos = (565, 250)
    mapnum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
    mapnum3Pos = (765, 250)
    mapnum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
    mapnum4Pos = (365, 450)
    mapnum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
    mapnum5Pos = (565, 450)
    mapnum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
    mapnum6Pos = (765, 450)
    sureButton = pygame.image.load(path("res/button/sure.png")).convert_alpha()
    surePos = (1080, 653)
    mapinfoPos = (0, 100)
    while True:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > mapnum1Pos[0] and x < mapnum1Pos[0] + mapnum1Button.get_width() \
                        and y > mapnum1Pos[1] and y < mapnum1Pos[1] + mapnum1Button.get_height():
                    mapnum1Button = pygame.image.load(path("res/mapnum/Mapnum1_1.png")).convert_alpha()
                    mapnum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapnum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapnum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapnum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapnum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    # 地图信息
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_1info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    mapinfoPos = (0,150)
                    flag_mapinfo = 1
                # shift picture

                if x > mapnum2Pos[0] and x < mapnum2Pos[0] + mapnum2Button.get_width() \
                        and y > mapnum2Pos[1] and y < mapnum2Pos[1] + mapnum2Button.get_height():
                    mapnum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapnum2Button = pygame.image.load(path("res/mapnum/Mapnum2_1.png")).convert_alpha()
                    mapnum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapnum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapnum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapnum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_2info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flag_mapinfo = 2
                # shift picture

                if x > mapnum3Pos[0] and x < mapnum3Pos[0] + mapnum3Button.get_width() \
                        and y > mapnum3Pos[1] and y < mapnum3Pos[1] + mapnum3Button.get_height():
                    mapnum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapnum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapnum3Button = pygame.image.load(path("res/mapnum/Mapnum3_1.png")).convert_alpha()
                    mapnum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapnum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapnum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_3info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flag_mapinfo = 3
                # shift picture

                if x > mapnum4Pos[0] and x < mapnum4Pos[0] + mapnum4Button.get_width() \
                        and y > mapnum4Pos[1] and y < mapnum4Pos[1] + mapnum4Button.get_height():
                    mapnum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapnum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapnum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapnum4Button = pygame.image.load(path("res/mapnum/Mapnum4_1.png")).convert_alpha()
                    mapnum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapnum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = "res/mapinfo/Map" + str(modeID) + "_4info.png"
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flag_mapinfo = 4
                # shift picture

                if x > mapnum5Pos[0] and x < mapnum5Pos[0] + mapnum5Button.get_width() \
                        and y > mapnum5Pos[1] and y < mapnum5Pos[1] + mapnum5Button.get_height():
                    mapnum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapnum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapnum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapnum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapnum5Button = pygame.image.load(path("res/mapnum/Mapnum5_1.png")).convert_alpha()
                    mapnum6Button = pygame.image.load(path("res/mapnum/Mapnum6_0.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_5info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flag_mapinfo = 5
                # shift picture

                if x > mapnum6Pos[0] and x < mapnum6Pos[0] + mapnum6Button.get_width() \
                        and y > mapnum6Pos[1] and y < mapnum6Pos[1] + mapnum6Button.get_height():
                    mapnum1Button = pygame.image.load(path("res/mapnum/Mapnum1_0.png")).convert_alpha()
                    mapnum2Button = pygame.image.load(path("res/mapnum/Mapnum2_0.png")).convert_alpha()
                    mapnum3Button = pygame.image.load(path("res/mapnum/Mapnum3_0.png")).convert_alpha()
                    mapnum4Button = pygame.image.load(path("res/mapnum/Mapnum4_0.png")).convert_alpha()
                    mapnum5Button = pygame.image.load(path("res/mapnum/Mapnum5_0.png")).convert_alpha()
                    mapnum6Button = pygame.image.load(path("res/mapnum/Mapnum6_1.png")).convert_alpha()
                    mapinfoID = path("res/mapinfo/Map" + str(modeID) + "_6info.png")
                    mapinfo = pygame.image.load(mapinfoID).convert_alpha()
                    flag_mapinfo = 6
                # shift picture

                if x > surePos[0] and x < surePos[0] + sureButton.get_width() \
                        and y > surePos[1] and y < surePos[1] + sureButton.get_height() \
                        and flag_mapinfo > 0:
                    selectCharacters(screen, clock, modeID, flag_mapinfo)
                    breakflag = 1
                    # load game

                if x > backPos[0] and x < backPos[0] + backButton.get_width() \
                        and y > backPos[1] and y < backPos[1] + backButton.get_height():
                    from modeSelect import modeSelect
                    modeSelect(screen, clock)
                    breakflag = 1
                    # here to come back

                elif x > homePos[0] and x < homePos[0] + homeButton.get_width() \
                        and y > homePos[1] and y < homePos[1] + homeButton.get_height():
                    from initMenu import initialMenu
                    initialMenu(screen, clock)
                    breakflag = 1
                    # here to come back home

        # 填充背景和内容
        screen.blit(bg, (0, 0))
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        screen.blit(mapTitle, mapTitlePos)
        screen.blit(modeIntro, modeintroPos)
        screen.blit(mapnum1Button,mapnum1Pos)
        screen.blit(mapnum2Button, mapnum2Pos)
        screen.blit(mapnum3Button, mapnum3Pos)
        screen.blit(mapnum4Button, mapnum4Pos)
        screen.blit(mapnum5Button, mapnum5Pos)
        screen.blit(mapnum6Button, mapnum6Pos)
        if flag_mapinfo > 0:
            screen.blit(mapinfo, mapinfoPos)
            screen.blit(sureButton, surePos)
        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break


