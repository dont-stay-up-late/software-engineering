import pygame
from path import path
pygame.init()
pygame.mixer.init()

bgmNow=-1
bgmNames=['main','select','fighting','handbook','win','lose']
bgmOpen=True

def bgmPath(bgm):
    return path("res/bgm/"+ bgm +"bgm.mp3")

#播放音乐：用这个函数，参数为0，1，2，3代表4个bgm,参数为-1则停止播放。
#0:主界面 1:选模式、选卡界面 2:战斗界面 3:图鉴帮助界面

def playBgm(bgm=-1):
    global bgmNow

    if bgmOpen==False or bgm==-1:
        bgmNow=-1
        pygame.mixer.music.stop()
        return
    if bgm==bgmNow:
        return

    pygame.mixer.music.load(bgmPath(bgmNames[bgm]))
    pygame.mixer.music.play(-1)
    bgmNow=bgm
    return

#游戏结束时胜利或失败调用这两个函数
def winBgm():
    global bgmNow
    if bgmOpen:
        bgmNow=-1
        pygame.mixer.music.load(bgmPath(bgmNames[4]))
        pygame.mixer.music.play(-1)
    return

def loseBgm():
    global bgmNow
    if bgmOpen:
        bgmNow=-1
        pygame.mixer.music.load(bgmPath(bgmNames[5]))
        pygame.mixer.music.play(-1)
    return

#在设置中加一个开关bgm的按键，调用这个函数
def closeBgm():
    global bgmOpen

    bgmOpen= not bgmOpen
    if not bgmOpen:
        playBgm(-1)
    if bgmOpen:
        playBgm(bgmNow)
    return



'''
print ("select bgm")
while True:
    bgm=input()
    playBgm(int(bgm))
'''
