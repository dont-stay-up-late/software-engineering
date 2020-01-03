import pygame
import sys
from pygame.locals import *
from src.path import path
from src.bgm import *

def settings(screen, clock, isBgmOn):       
    # isBgmOn是一个bool量用来告诉函数是否播放背景音乐
    # isFullscreen则以bool量形式告诉函数当前是否是全屏的
    # 需要在这里设置一下背景音乐

    size = (width, height) = (1280, 720)
    
    bgmFlag = isBgmOn
    breakflag = 0
    background = pygame.image.load(path("res/bg/bg_main.png")).convert()    #背景图
    title = pygame.image.load(path("res/pic/settingTitle.png")).convert_alpha()    #标题
    titlePos = (340, 20)
    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)

    fullscreenButton = pygame.image.load(path("res/button/fullscreen.png")).convert_alpha()     # 全屏
    fullscreenPos = (420, 250)
    bgmButton = pygame.image.load(path("res/button/bgm.png")).convert_alpha()         # 背景音乐
    bgmPos = (420, 350)

    onButton = pygame.image.load(path("res/button/on.png")).convert_alpha()     
    offButton = pygame.image.load(path("res/button/off.png")).convert_alpha()        
    fullscreenOnPos0 = (660, 250)
    fullscreenOnPos1 = (660, 245)
    fullscreenOffPos0 = (727, 250)
    fullscreenOffPos1 = (727, 245)
    bgmOnPos0 = (660, 350)
    bgmOnPos1 = (660, 345)
    bgmOffPos0 = (727, 350)
    bgmOffPos1 = (727, 345)
    fullscreenOnPos = fullscreenOnPos0
    fullscreenOffPos = fullscreenOffPos0
    bgmOnPos = bgmOnPos0
    bgmOffPos = bgmOffPos0

    while True:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

            # 浮动效果
            if x > fullscreenOnPos0[0] and x < fullscreenOnPos0[0] + onButton.get_width() \
                    and y > fullscreenOnPos0[1] and y < fullscreenOnPos0[1] + onButton.get_height():
                fullscreenOnPos = fullscreenOnPos1
            else:
                fullscreenOnPos = fullscreenOnPos0
            
            if x > fullscreenOffPos0[0] and x < fullscreenOffPos0[0] + offButton.get_width() \
                    and y > fullscreenOffPos0[1] and y < fullscreenOffPos0[1] + offButton.get_height():
                fullscreenOffPos = fullscreenOffPos1
            else:
                fullscreenOffPos = fullscreenOffPos0

            if x > bgmOnPos0[0] and x < bgmOnPos0[0] + onButton.get_width() \
                    and y > bgmOnPos0[1] and y < bgmOnPos0[1] + onButton.get_height():
                bgmOnPos = bgmOnPos1
            else:
                bgmOnPos = bgmOnPos0
            
            if x > bgmOffPos0[0] and x < bgmOffPos0[0] + offButton.get_width() \
                    and y > bgmOffPos0[1] and y < bgmOffPos0[1] + offButton.get_height():
                bgmOffPos = bgmOffPos1
            else:
                bgmOffPos = bgmOffPos0

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
                if x > fullscreenOnPos0[0] and x < fullscreenOnPos0[0] + onButton.get_width() \
                    and y > fullscreenOnPos0[1] and y < fullscreenOnPos0[1] + onButton.get_height():
                    # here to set fullscreen on
                    screen = pygame.display.set_mode(size, FULLSCREEN)

                if x > fullscreenOffPos0[0] and x < fullscreenOffPos0[0] + offButton.get_width() \
                    and y > fullscreenOffPos0[1] and y < fullscreenOffPos0[1] + offButton.get_height():
                    # here to set fullscreen off
                    screen = pygame.display.set_mode(size, 0)
                
                if x > bgmOnPos0[0] and x < bgmOnPos0[0] + onButton.get_width() \
                    and y > bgmOnPos0[1] and y < bgmOnPos0[1] + onButton.get_height():
                    # here to turn on bgm
                    # 这里要加上对应的逻辑
                    if bgmFlag:
                        bgmFlag = False
                        # closeBgm()


                if x > bgmOffPos0[0] and x < bgmOffPos0[0] + offButton.get_width() \
                    and y > bgmOffPos0[1] and y < bgmOffPos0[1] + offButton.get_height():
                    # here to turn off bgm
                    #需要加上对应逻辑
                    if not bgmFlag:
                        bgmFlag = True
                        # closeBgm()


        screen.blit(background, (0, 0))
        screen.blit(title, titlePos)
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        screen.blit(fullscreenButton, fullscreenPos)
        screen.blit(bgmButton, bgmPos)
        screen.blit(onButton, fullscreenOnPos)
        screen.blit(offButton, fullscreenOffPos)
        screen.blit(onButton, bgmOnPos)
        screen.blit(offButton, bgmOffPos)

# 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            return (screen, bgmFlag)

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

    settings(screen, clock, False)