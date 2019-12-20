import pygame
import sys
from pygame.locals import *
from selectMode import *
from path import path
from bgm import playBgm
from help import help
from settings import *

# 主菜单初始化
def initialMenu(screen, clock):
    background = (255, 255, 255)
    breakflag = 0
    playBgm(0)
    
    # 图片及位置
    background = pygame.image.load(path("res/bg/bg_main.png")).convert()    #背景图
    title = pygame.image.load(path("res/pic/title.png")).convert_alpha()    #标题
    titlePos = (340, 100)
    startButton = pygame.image.load(path("res/button/start.png")).convert_alpha()   #开始游戏
    startPos0 = (540, 345)
    startPos1 = (540, 340)
    handbookButton = pygame.image.load(path("res/button/handbook.png")).convert_alpha()     #图鉴
    handbookPos0 = (400, 445)
    handbookPos1 = (400, 440)
    helpButton = pygame.image.load(path("res/button/help.png")).convert_alpha()         #帮助文档
    helpPos0 = (400, 545)
    helpPos1 = (400, 540)
    settingButton = pygame.image.load(path("res/button/setting.png")).convert_alpha()       #设置
    settingPos0 = (680, 445)
    settingPos1 = (680, 440)
    quitButton = pygame.image.load(path("res/button/quit.png")).convert_alpha()         #退出游戏
    quitPos0 = (680, 545)
    quitPos1 = (680, 540)
    startPos = startPos0
    handbookPos = handbookPos0
    helpPos = helpPos0
    settingPos = settingPos0
    quitPos = quitPos0

    while True:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            #   按键位置移动
            if x > startPos0[0] and x < startPos0[0] + startButton.get_width() \
                    and y > startPos0[1] and y < startPos0[1] + startButton.get_height():
                startPos = startPos1
            else:
                startPos = startPos0

            if x > handbookPos0[0] and x < handbookPos0[0] + handbookButton.get_width() \
                    and y > handbookPos0[1] and y < handbookPos0[1] + handbookButton.get_height():
                handbookPos = handbookPos1
            else:
                handbookPos = handbookPos0

            if x > helpPos0[0] and x < helpPos0[0] + helpButton.get_width() \
                    and y > helpPos0[1] and y < helpPos0[1] + helpButton.get_height():
                helpPos = helpPos1
            else:
                helpPos = helpPos0

            if x > settingPos0[0] and x < settingPos0[0] + settingButton.get_width() \
                    and y > settingPos0[1] and y < settingPos0[1] + settingButton.get_height():
                settingPos = settingPos1
            else:
                settingPos = settingPos0

            if x > quitPos0[0] and x < quitPos0[0] + quitButton.get_width() \
                    and y > quitPos0[1] and y < quitPos0[1] + quitButton.get_height():
                quitPos = quitPos1
            else:
                quitPos = quitPos0

            #   退出游戏
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > startPos0[0] and x < startPos0[0] + startButton.get_width() \
                        and y > startPos0[1] and y < startPos0[1] + startButton.get_height():
                    selectMode(screen,clock)
                    breakflag = 1
                    # here to start the game function

                if x > handbookPos0[0] and x < handbookPos0[0] + handbookButton.get_width() \
                        and y > handbookPos0[1] and y < handbookPos0[1] + handbookButton.get_height():
                    from handbook import handbook
                    handbook(screen, clock)
                    # here to the handbook function

                if x > helpPos0[0] and x < helpPos0[0] + helpButton.get_width() \
                        and y > helpPos0[1] and y < helpPos0[1] + helpButton.get_height():
                    from help import help
                    help(screen, clock)
                    # here to start the help function

                if x > settingPos0[0] and x < settingPos0[0] + settingButton.get_width() \
                        and y > settingPos0[1] and y < settingPos0[1] + settingButton.get_height():
                    from settings import settings
                    screen, isBgmOn = settings(screen, clock, False)
                    settings(screen, clock, True)
                    # here to the setting function

                elif x > quitPos0[0] and x < quitPos0[0] + quitButton.get_width() \
                        and y > quitPos0[1] and y < quitPos0[1] + quitButton.get_height():
                    print('game ended!')
                    sys.exit()
        # 填充背景和内容
        screen.blit(background, (0, 0))
        screen.blit(title, titlePos)
        screen.blit(startButton, startPos)
        screen.blit(handbookButton, handbookPos)
        screen.blit(helpButton, helpPos)
        screen.blit(settingButton, settingPos)
        screen.blit(quitButton, quitPos)
        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break


