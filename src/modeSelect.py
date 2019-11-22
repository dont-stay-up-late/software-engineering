import pygame
import sys
from pygame.locals import *
from selectMap import *
from pathlib import Path

# 模式选择
def modeSelect(screen, clock):
    bg = (255, 255, 255)

    # 图片及位置
    path = Path.cwd()
    if path.parts[len(path.parts) - 1] == 'src':
        path = path.parent
    path = path.joinpath('res').joinpath('UIimage')
    bg = pygame.image.load(str(path.joinpath("menu_bg.png"))).convert()
    title = pygame.image.load(str(path.joinpath("title.png"))).convert_alpha()
    titlePos = (150, 40)
    modePic = pygame.image.load(str(path.joinpath("modeselect.png"))).convert_alpha()
    modePos = (275, 180)
    singleAttackButton = pygame.image.load(str(path.joinpath("single_attack.png"))).convert_alpha()
    single_attackPos0 = (155, 265)
    single_attackPos1 = (155, 260)
    singleDefendButton = pygame.image.load(str(path.joinpath("single_defend.png"))).convert_alpha()
    single_defendPos0 = (395, 265)
    single_defendPos1 = (395, 260)
    onlineAttackButton = pygame.image.load(str(path.joinpath("online_attack.png"))).convert_alpha()
    online_attackPos0 = (155, 350)
    online_attackPos1 = (155, 345)
    onlineDefendButton = pygame.image.load(str(path.joinpath("online_defend.png"))).convert_alpha()
    online_defendPos0 = (395, 350)
    online_defendPos1 = (395, 345)
    backMenuButton = pygame.image.load(str(path.joinpath("backmenu.png"))).convert_alpha()
    backmenuPos0 = (275, 435)
    backmenuPos1 = (275, 430)
    single_attackPos = single_attackPos0
    single_defendPos = single_defendPos0
    online_attackPos = online_attackPos0
    online_defendPos = online_defendPos0
    backmenuPos = backmenuPos0

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

            if x > backmenuPos0[0] and x < backmenuPos0[0] + backMenuButton.get_width() \
                    and y > backmenuPos0[1] and y < backmenuPos0[1] + backMenuButton.get_height():
                backmenuPos = backmenuPos1
            else:
                backmenuPos = backmenuPos0

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if x > single_attackPos0[0] and x < single_attackPos0[0] + singleAttackButton.get_width() \
                        and y > single_attackPos0[1] and y < single_attackPos0[1] + singleAttackButton.get_height():
                    selectMap(screen,clock,1)
                    # here to start the game single attack function

                if x > single_defendPos0[0] and x < single_defendPos0[0] + singleDefendButton.get_width() \
                        and y > single_defendPos0[1] and y < single_defendPos0[1] + singleDefendButton.get_height():
                    selectMap(screen,clock,2)
                    # here to start the game single defend function

                if x > online_attackPos0[0] and x < online_attackPos0[0] + onlineAttackButton.get_width() \
                        and y > online_attackPos0[1] and y < online_attackPos0[1] + onlineAttackButton.get_height():
                    selectMap(screen,clock,3)
                    # here to start the game online attack function

                if x > online_defendPos0[0] and x < online_defendPos0[0] + onlineDefendButton.get_width() \
                        and y > online_defendPos0[1] and y < online_defendPos0[1] + onlineDefendButton.get_height():
                    selectMap(screen,clock,4)
                    # here to start the game online defend function

                elif backmenuPos0[0] < x < backmenuPos0[0] + backMenuButton.get_width() \
                        and y > backmenuPos0[1] and y < backmenuPos0[1] + backMenuButton.get_height():
                    from initMenu import initialMenu
                    initialMenu(screen, clock)

        # 填充背景和内容
        screen.blit(bg, (0, 0))
        screen.blit(title, titlePos)
        screen.blit(modePic, modePos)
        screen.blit(singleAttackButton, single_attackPos)
        screen.blit(singleDefendButton, single_defendPos)
        screen.blit(onlineAttackButton, online_attackPos)
        screen.blit(onlineDefendButton, online_defendPos)
        screen.blit(backMenuButton, backmenuPos)
        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.flip()
        # 帧率
        clock.tick(30)


