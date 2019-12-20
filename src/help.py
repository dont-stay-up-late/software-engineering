import pygame
import sys
from pygame.locals import *
from path import path

def help(screen, clock):
    breakflag = 0
    helpID = 0  # 0 for basic; 1 for attacker; 2 for defender
    HelpList = []

    background = pygame.image.load(path("res/bg/bg_main.png")).convert()    #背景图
    title = pygame.image.load(path("res/pic/helpTitle.png")).convert_alpha()    #标题
    titlePos = (340, 20)
    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)

    basicButton = pygame.image.load(path("res/button/basic.png")).convert_alpha()     # 基本设定
    basicPos0 = (50, 245)
    basicPos1 = (50, 240)
    attackerButton = pygame.image.load(path("res/button/attacker.png")).convert_alpha()         #感染者
    attackerPos0 = (50, 312)
    attackerPos1 = (50, 307)
    defenderButton = pygame.image.load(path("res/button/defender.png")).convert_alpha()     #生还者
    defenderPos0 = (50, 379)
    defenderPos1 = (50, 374)

    helpPos = (300, 250)

    HelpList.append(pygame.image.load(path("res/help/basic.png")).convert_alpha())
    HelpList.append(pygame.image.load(path("res/help/attacker.png")).convert_alpha())
    HelpList.append(pygame.image.load(path("res/help/defender.png")).convert_alpha())

    while True:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

            # 浮动效果
            if x > basicPos0[0] and x < basicPos0[0] + basicButton.get_width() \
                    and y > basicPos0[1] and y < basicPos0[1] + basicButton.get_height():
                basicPos = basicPos1
            else:
                basicPos = basicPos0

            if x > attackerPos0[0] and x < attackerPos0[0] + attackerButton.get_width() \
                    and y > attackerPos0[1] and y < attackerPos0[1] + attackerButton.get_height():
                attackerPos = attackerPos1
            else:
                attackerPos = attackerPos0

            if x > defenderPos0[0] and x < defenderPos0[0] + defenderButton.get_width() \
                    and y > defenderPos0[1] and y < defenderPos0[1] + defenderButton.get_height():
                defenderPos = defenderPos1
            else:
                defenderPos = defenderPos0

            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > backPos[0] and x < backPos[0] + backButton.get_width() \
                        and y > backPos[1] and y < backPos[1] + backButton.get_height():
                    breakflag = 1
                    # here to come back

                if x > homePos[0] and x < homePos[0] + homeButton.get_width() \
                        and y > homePos[1] and y < homePos[1] + homeButton.get_height():
                    breakflag = 1
                    # here to come back home
                
                # touch logic
                if x > basicPos0[0] and x < basicPos0[0] + basicButton.get_width() \
                    and y > basicPos0[1] and y < basicPos0[1] + basicButton.get_height():
                    helpID = 0
                
                if x > attackerPos0[0] and x < attackerPos0[0] + attackerButton.get_width() \
                    and y > attackerPos0[1] and y < attackerPos0[1] + attackerButton.get_height():
                    helpID = 1
                
                if x > defenderPos0[0] and x < defenderPos0[0] + defenderButton.get_width() \
                    and y > defenderPos0[1] and y < defenderPos0[1] + defenderButton.get_height():
                    helpID = 2
    
        helpPic = HelpList[helpID]

        screen.blit(background, (0, 0))
        screen.blit(title, titlePos)
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        screen.blit(basicButton, basicPos)
        screen.blit(attackerButton, attackerPos)
        screen.blit(defenderButton, defenderPos)
        screen.blit(helpPic, helpPos)


        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break

# unit test
if __name__ == '__main__':

    pygame.init()
    global screen,clock
    size = (width, height) = (1280, 720)

    # font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    fullscreen = False
    fullsize = pygame.display.list_modes()[0]

    # 计时器
    clock = pygame.time.Clock()

    # 创建窗口及标题
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("末日之战")

    help(screen, clock)
   
