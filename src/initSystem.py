import pygame
import sys
from pygame.locals import *


# 初始化
def initialSystem():
    pygame.init()

    size = (width, height) = (750, 500)

    bg = (255, 255, 255)
    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    fullscreen = False
    fullsize = pygame.display.list_modes()[0]

    # 计时器
    clock = pygame.time.Clock()



