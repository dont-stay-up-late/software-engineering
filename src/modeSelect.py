import pygame
import sys
from pygame.locals import *
from selectMap import *
from path import path
# 模式选择
def modeSelect(screen, clock):
    bg = (255, 255, 255)
    breakflag = 0
    # 图片及位置
    bg = pygame.image.load(path("res/bg/bg_mode.png")).convert()
    title = pygame.image.load(path("res/pic/title.png")).convert_alpha()
    titlePos = titlePos = (340, 100)
    modePic = pygame.image.load(path("res/pic/modeselect.png")).convert_alpha()
    modePos = (540, 345)
    #   四种模式
    singleAttackButton = pygame.image.load(path("res/button/single_attack.png")).convert_alpha()
    single_attackPos0 = (400, 445)
    single_attackPos1 = (400, 440)
    singleDefendButton = pygame.image.load(path("res/button/single_defend.png")).convert_alpha()
    single_defendPos0 = (400, 545)
    single_defendPos1 = (400, 540)
    onlineAttackButton = pygame.image.load(path("res/button/online_attack.png")).convert_alpha()
    online_attackPos0 = (680, 445)
    online_attackPos1 = (680, 440)
    onlineDefendButton = pygame.image.load(path("res/button/online_defend.png")).convert_alpha()
    online_defendPos0 = (680, 545)
    online_defendPos1 = (680, 540)

    # 返回
    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    #返回主菜单
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)
    single_attackPos = single_attackPos0
    single_defendPos = single_defendPos0
    online_attackPos = online_attackPos0
    online_defendPos = online_defendPos0

    while True:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if x > single_attackPos[0] and x < single_attackPos[0] + singleAttackButton.get_width() \
                    and y > single_attackPos0[1] and y < single_attackPos0[1] + singleAttackButton.get_height():
                single_attackPos = single_attackPos1
            else:
                single_attackPos = single_attackPos0

            if x > single_defendPos[0] and x < single_defendPos[0] + singleDefendButton.get_width() \
                    and y > single_defendPos0[1] and y < single_defendPos0[1] + singleDefendButton.get_height():
                single_defendPos = single_defendPos1
            else:
                single_defendPos = single_defendPos0

            if x > online_attackPos[0] and x < online_attackPos[0] + onlineAttackButton.get_width() \
                    and y > online_attackPos0[1] and y < online_attackPos0[1] + onlineAttackButton.get_height():
                online_attackPos = online_attackPos1
            else:
                online_attackPos = online_attackPos0

            if x > online_defendPos[0] and x < online_defendPos[0] + onlineDefendButton.get_width() \
                    and y > online_defendPos0[1] and y < online_defendPos0[1] + onlineDefendButton.get_height():
                online_defendPos = online_defendPos1
            else:
                online_defendPos = online_defendPos0

            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > single_attackPos0[0] and x < single_attackPos0[0] + singleAttackButton.get_width() \
                        and y > single_attackPos0[1] and y < single_attackPos0[1] + singleAttackButton.get_height():
                    selectMap(screen,clock,1)
                    break
                    # here to start the game single attack function

                if x > single_defendPos0[0] and x < single_defendPos0[0] + singleDefendButton.get_width() \
                        and y > single_defendPos0[1] and y < single_defendPos0[1] + singleDefendButton.get_height():
                    selectMap(screen,clock,2)
                    breakflag = 1
                    # here to start the game single defend function

                if x > online_attackPos0[0] and x < online_attackPos0[0] + onlineAttackButton.get_width() \
                        and y > online_attackPos0[1] and y < online_attackPos0[1] + onlineAttackButton.get_height():
                    selectMap(screen,clock,3)
                    breakflag = 1
                    # here to start the game online attack function

                if x > online_defendPos0[0] and x < online_defendPos0[0] + onlineDefendButton.get_width() \
                        and y > online_defendPos0[1] and y < online_defendPos0[1] + onlineDefendButton.get_height():
                    selectMap(screen,clock,4)
                    breakflag = 1
                    # here to start the game online defend function

                if x > backPos[0] and x < backPos[0] + backButton.get_width() \
                        and y > backPos[1] and y < backPos[1] + backButton.get_height():
                    from initMenu import initialMenu
                    initialMenu(screen, clock)
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
        screen.blit(title, titlePos)
        screen.blit(modePic, modePos)
        screen.blit(singleAttackButton, single_attackPos)
        screen.blit(singleDefendButton, single_defendPos)
        screen.blit(onlineAttackButton, online_attackPos)
        screen.blit(onlineDefendButton, online_defendPos)

        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break


