import pygame
import sys
from pygame.locals import *
from initMenu import *

# 系统初始化
def initialSystem():
    pygame.init()
    global screen,clock
    size = (width, height) = (750, 500)

    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    fullscreen = False
    fullsize = pygame.display.list_modes()[0]

    # 计时器
    clock = pygame.time.Clock()

    # 创建窗口及标题
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("末日之战")

# main exe
if __name__ == '__main__':
    initialSystem()
    initialMenu(screen, clock)