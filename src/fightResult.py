import pygame,sys,time
from pygame.locals import *
from path import path

def endFight(screen, clock, modeID, flag_mapinfo, isWin):
    resultPad = pygame.image.load(path("res/battle/fightResultPad.png")).convert_alpha()
    if isWin:
        title = pygame.image.load(path("res/battle/victory.png")).convert_alpha()
    else:
        title = pygame.image.load(path("res/battle/lose.png")).convert_alpha()
    tryAgainButton = pygame.image.load(path("res/battle/tryAgain.png")).convert_alpha()
    returnHomeButton = pygame.image.load(path("res/battle/backToMenu.png")).convert_alpha()

    padPos = (240, 60)
    titlePos = (440, 80)
    tryAgainButtonPos0 = (540, 430)
    tryAgainButtonPos1 = (540, 425)
    returnHomeButtonPos0 = (540, 510)
    returnHomeButtonPos1 = (540, 505)

    breakflag = 0

    while True:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if x > tryAgainButtonPos0[0] and x < tryAgainButtonPos0[0] + tryAgainButton.get_width() \
                    and y > tryAgainButtonPos0[1] and y < tryAgainButtonPos0[1] + tryAgainButton.get_height():
                tryAgainButtonPos = tryAgainButtonPos1
            else:
                tryAgainButtonPos = tryAgainButtonPos0

            if x > returnHomeButtonPos0[0] and x < returnHomeButtonPos0[0] + returnHomeButton.get_width() \
                    and y > returnHomeButtonPos0[1] and y < returnHomeButtonPos0[1] + returnHomeButton.get_height():
                returnHomeButtonPos = returnHomeButtonPos1
            else:
                returnHomeButtonPos = returnHomeButtonPos0

            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > tryAgainButtonPos0[0] and x < tryAgainButtonPos0[0] + tryAgainButton.get_width() \
                        and y > tryAgainButtonPos0[1] and y < tryAgainButtonPos0[1] + tryAgainButton.get_height():
                    from selectCharacters import selectCharacters
                    selectCharacters(screen, clock, modeID, flag_mapinfo)
                    breakflag = 1
                    # here to start the game function

                if x > returnHomeButtonPos0[0] and x < returnHomeButtonPos0[0] + returnHomeButton.get_width() \
                        and y > returnHomeButtonPos0[1] and y < returnHomeButtonPos0[1] + returnHomeButton.get_height():
                    from initMenu import initialMenu
                    initialMenu(screen, clock)
                    # here to get back to home

        # 填充背景和内容
        screen.blit(resultPad, padPos)
        screen.blit(title, titlePos)
        screen.blit(tryAgainButton, tryAgainButtonPos)
        screen.blit(returnHomeButton, returnHomeButtonPos)

        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break

# unit test
if __name__ == '__main__':
    import pygame
    import sys
    from path import path
    from pygame.locals import *

    pygame.init()
    global screen,clock
    size = (width, height) = (1280, 720)

    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    fullscreen = False
    fullsize = pygame.display.list_modes()[0]

    # 计时器
    clock = pygame.time.Clock()

    # 创建窗口及标题
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("末日之战")

    endFight(screen, clock, 1, 0, True)
    
