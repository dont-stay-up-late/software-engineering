import pygame
import sys
from pygame.locals import *
from selectMap import *
from path import path
# 模式选择
def selectMode(screen, clock):
    background = (255, 255, 255)
    breakflag = 0
    # 图片及位置
    background = pygame.image.load(path("res/bg/bg_mode.png")).convert()
    title = pygame.image.load(path("res/pic/title.png")).convert_alpha()
    titlePos = titlePos = (340, 100)
    modePic = pygame.image.load(path("res/pic/modeselect.png")).convert_alpha()
    modePos = (540, 345)
    #   四种模式
    singleAttackButton = pygame.image.load(path("res/button/single_attack.png")).convert_alpha()
    singleAttackPos0 = (400, 445)
    singleAttackPos1 = (400, 440)
    singleDefendButton = pygame.image.load(path("res/button/single_defend.png")).convert_alpha()
    singleDefendPos0 = (400, 545)
    singleDefendPos1 = (400, 540)
    onlineAttackButton = pygame.image.load(path("res/button/online_attack.png")).convert_alpha()
    onlineAttackPos0 = (680, 445)
    onlineAttackPos1 = (680, 440)
    onlineDefendButton = pygame.image.load(path("res/button/online_defend.png")).convert_alpha()
    onlineDefendPos0 = (680, 545)
    onlineDefendPos1 = (680, 540)

    # 返回
    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    #返回主菜单
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)
    singleAttackPos = singleAttackPos0
    singleDefendPos = singleDefendPos0
    onlineAttackPos = onlineAttackPos0
    onlineDefendPos = onlineDefendPos0

    while True:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if x > singleAttackPos[0] and x < singleAttackPos[0] + singleAttackButton.get_width() \
                    and y > singleAttackPos0[1] and y < singleAttackPos0[1] + singleAttackButton.get_height():
                singleAttackPos = singleAttackPos1
            else:
                singleAttackPos = singleAttackPos0

            if x > singleDefendPos[0] and x < singleDefendPos[0] + singleDefendButton.get_width() \
                    and y > singleDefendPos0[1] and y < singleDefendPos0[1] + singleDefendButton.get_height():
                singleDefendPos = singleDefendPos1
            else:
                singleDefendPos = singleDefendPos0

            if x > onlineAttackPos[0] and x < onlineAttackPos[0] + onlineAttackButton.get_width() \
                    and y > onlineAttackPos0[1] and y < onlineAttackPos0[1] + onlineAttackButton.get_height():
                onlineAttackPos = onlineAttackPos1
            else:
                onlineAttackPos = onlineAttackPos0

            if x > onlineDefendPos[0] and x < onlineDefendPos[0] + onlineDefendButton.get_width() \
                    and y > onlineDefendPos0[1] and y < onlineDefendPos0[1] + onlineDefendButton.get_height():
                onlineDefendPos = onlineDefendPos1
            else:
                onlineDefendPos = onlineDefendPos0

            if event.type == pygame.QUIT:
                try:
                    sys.exit()
                except:
                    pass
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > singleAttackPos0[0] and x < singleAttackPos0[0] + singleAttackButton.get_width() \
                        and y > singleAttackPos0[1] and y < singleAttackPos0[1] + singleAttackButton.get_height():
                    selectMap(screen,clock,1)
                    break
                    # here to start the game single attack function

                if x > singleDefendPos0[0] and x < singleDefendPos0[0] + singleDefendButton.get_width() \
                        and y > singleDefendPos0[1] and y < singleDefendPos0[1] + singleDefendButton.get_height():
                    selectMap(screen,clock,2)
                    breakflag = 1
                    # here to start the game single defend function

                if x > onlineAttackPos0[0] and x < onlineAttackPos0[0] + onlineAttackButton.get_width() \
                        and y > onlineAttackPos0[1] and y < onlineAttackPos0[1] + onlineAttackButton.get_height():
                    selectMap(screen,clock,3)
                    breakflag = 1
                    # here to start the game online attack function

                if x > onlineDefendPos0[0] and x < onlineDefendPos0[0] + onlineDefendButton.get_width() \
                        and y > onlineDefendPos0[1] and y < onlineDefendPos0[1] + onlineDefendButton.get_height():
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
                    from initialMenu import initialMenu
                    initialMenu(screen, clock)
                    breakflag = 1
                    # here to come back home
        # 填充背景和内容
        screen.blit(background, (0, 0))
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        screen.blit(title, titlePos)
        screen.blit(modePic, modePos)
        screen.blit(singleAttackButton, singleAttackPos)
        screen.blit(singleDefendButton, singleDefendPos)
        screen.blit(onlineAttackButton, onlineAttackPos)
        screen.blit(onlineDefendButton, onlineDefendPos)

        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break


