import pygame
import sys
from pygame.locals import *
from modeSelect import *


# 主菜单初始化
def initialMenu(screen, clock):
    bg = (255, 255, 255)

    # 图片及位置
    bg = pygame.image.load("res/menu_bg.png").convert()
    title = pygame.image.load("res/title.png").convert_alpha()
    titlePos = (150, 40)
    startButton = pygame.image.load("res/start.png").convert_alpha()
    startPos0 = (275, 275)
    startPos1 = (275, 270)
    handbookButton = pygame.image.load("res/handbook.png").convert_alpha()
    handbookPos0 = (25, 275)
    handbookPos1 = (25, 270)
    helpButton = pygame.image.load("res/help.png").convert_alpha()
    helpPos0 = (25, 400)
    helpPos1 = (25, 395)
    settingButton = pygame.image.load("res/setting.png").convert_alpha()
    settingPos0 = (525, 275)
    settingPos1 = (525, 270)
    quitButton = pygame.image.load("res/quit.png").convert_alpha()
    quitPos0 = (525, 400)
    quitPos1 = (525, 395)
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

            if event.type == MOUSEBUTTONDOWN:
                if x > startPos0[0] and x < startPos0[0] + startButton.get_width() \
                        and y > startPos0[1] and y < startPos0[1] + startButton.get_height():
                    modeSelect(screen,clock)
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
        pygame.display.flip()
        # 帧率
        clock.tick(30)


