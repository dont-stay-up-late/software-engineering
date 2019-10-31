import pygame
import sys
from pygame.locals import *

# 初始化
def initialMenu():
    pygame.init()

    size = (width, height) = (750,500)

    bg = (255, 255, 255)
    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    fullscreen = False
    fullsize = pygame.display.list_modes()[0]

    # 计时器
    clock = pygame.time.Clock()

    # 创建窗口及标题
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("末日之战")

    # 图片及位置
    bg = pygame.image.load("res/menu_bg.png").convert()
    title = pygame.image.load("res/title.png").convert_alpha()
    titlePos = (150, 40)
    startButton = pygame.image.load("res/start.png").convert_alpha()
    startPos0 = (275, 200)
    startPos1 = (275, 195)
    loadButton = pygame.image.load("res/load_map.png").convert_alpha()
    loadPos0 = (275, 275)
    loadPos1 = (275, 270)
    quitButton = pygame.image.load("res/quit.png").convert_alpha()
    quitPos0 = (275, 350)
    quitPos1 = (275, 345)
    
    startPos = startPos0
    loadPos = loadPos0
    quitPos = quitPos0

    while True:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if x > startPos0[0] and x < startPos0[0] + startButton.get_width()\
                and y > startPos0[1] and y < startPos0[1] + startButton.get_height():
                startPos = startPos1
            else:
                startPos = startPos0
                
            if x > loadPos0[0] and x < loadPos0[0] + loadButton.get_width()\
                and y > loadPos0[1] and y < loadPos0[1] + loadButton.get_height():
                loadPos = loadPos1
            else:
                loadPos = loadPos0

            if x > quitPos0[0] and x < quitPos0[0] + quitButton.get_width()\
                and y > quitPos0[1] and y < quitPos0[1] + quitButton.get_height():
                quitPos = quitPos1
            else:
                quitPos = quitPos0
            
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if x > startPos0[0] and x < startPos0[0] + startButton.get_width()\
                    and y > startPos0[1] and y < startPos0[1] + startButton.get_height():
                    print('game start!')
                    # here to start the game function

                if x > loadPos0[0] and x < loadPos0[0] + loadButton.get_width()\
                    and y > loadPos0[1] and y < loadPos0[1] + loadButton.get_height():
                    print('game load!')
                    # here to the map-loading function
                    
                elif x > quitPos0[0] and x < quitPos0[0] + quitButton.get_width()\
                    and y > quitPos0[1] and y < quitPos0[1] + quitButton.get_height():
                    print('game ended!')
                    sys.exit()


        # 填充背景和内容
        screen.blit(bg, (0, 0))
        screen.blit(title, titlePos)
        screen.blit(startButton, startPos)
        screen.blit(loadButton, loadPos)
        screen.blit(quitButton, quitPos)
        # 说明文字
        # screen.blit(font.render("用上下左右键来控制", True, (166, 100, 30)), (300, 50))
        # 更新画面
        pygame.display.flip()
        # 帧率
        clock.tick(10)

if __name__=='__main__':
    initialMenu()
