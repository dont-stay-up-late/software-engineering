import pygame
import sys
from pygame.locals import *
from modeSelect import *
from path import path


# 主菜单初始化
def initialMenu(screen, clock):
    bg = (255, 255, 255)
    breakflag = 0

    # 图片及位置
    bg = pygame.image.load(path("res/bg/bg_main.png")).convert()
    title = pygame.image.load(path("res/pic/title.png")).convert_alpha()
    titlePos = (340, 100)
    startButton = pygame.image.load(path("res/button/start.png")).convert_alpha()
    startPos0 = (540, 345)
    startPos1 = (540, 340)
    handbookButton = pygame.image.load(path("res/button/handbook.png")).convert_alpha()
    handbookPos0 = (400, 445)
    handbookPos1 = (400, 440)
    helpButton = pygame.image.load(path("res/button/help.png")).convert_alpha()
    helpPos0 = (400, 545)
    helpPos1 = (400, 540)
    settingButton = pygame.image.load(path("res/button/setting.png")).convert_alpha()
    settingPos0 = (680, 445)
    settingPos1 = (680, 440)
    quitButton = pygame.image.load(path("res/button/quit.png")).convert_alpha()
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

            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > startPos0[0] and x < startPos0[0] + startButton.get_width() \
                        and y > startPos0[1] and y < startPos0[1] + startButton.get_height():
                    modeSelect(screen,clock)
                    breakflag = 1
                    # here to start the game function

                if x > handbookPos0[0] and x < handbookPos0[0] + handbookButton.get_width() \
                        and y > handbookPos0[1] and y < handbookPos0[1] + handbookButton.get_height():
                    print('game handbook!')
                    # here to the handbook function

                if x > helpPos0[0] and x < helpPos0[0] + helpButton.get_width() \
                        and y > helpPos0[1] and y < helpPos0[1] + helpButton.get_height():
                    print('game help!')
                    # here to start the help function

                if x > settingPos0[0] and x < settingPos0[0] + settingButton.get_width() \
                        and y > settingPos0[1] and y < settingPos0[1] + settingButton.get_height():
                    print('game setting!')
                    # here to the setting function

                elif x > quitPos0[0] and x < quitPos0[0] + quitButton.get_width() \
                        and y > quitPos0[1] and y < quitPos0[1] + quitButton.get_height():
                    print('game ended!')
                    sys.exit()
        # 填充背景和内容
        screen.blit(bg, (0, 0))
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


