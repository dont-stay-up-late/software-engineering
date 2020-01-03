import pygame
import sys
from pygame.locals import *
from src.path import path

def handbook(screen, clock):
    breakflag = 0
    showSurvivorOrZombie = 0    # 0 for survivor and 1 for zombie
    charID = 0      # from 0 to totalNum-1
    totalNum = 7    #可选中角色总数
    characterPicb = [] # 存储人类的列表
    characterPicr = [] # 存储僵尸图片的列表
    characterStoryb = []
    characterStoryr = []
    characterInfob = []
    characterInfor = []

    background = pygame.image.load(path("res/bg/bg_main.png")).convert()    #背景图
    title = pygame.image.load(path("res/pic/handbookTitle.png")).convert_alpha()    #标题
    titlePos = (340, 20)
    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)

    survivorButton = pygame.image.load(path("res/button/survivor.png")).convert_alpha()     #生存者
    survivorPos0 = (0, 245)
    survivorPos1 = (0, 240)
    zombieButton = pygame.image.load(path("res/button/zombie.png")).convert_alpha()         #感染者
    zombiePos0 = (200, 245)
    zombiePos1 = (200, 240)
    leftButton = pygame.image.load(path("res/button/left.png")).convert_alpha()     #左箭头
    leftPos0 = (55, 415)
    leftPos1 = (55, 410)
    rightButton = pygame.image.load(path("res/button/right.png")).convert_alpha()         #右箭头
    rightPos0 = (275, 415)
    rightPos1 = (275, 410)

    charbg = pygame.image.load(path("res/character/charflame.png")).convert_alpha()
    charbgPos = (150, 350)
    charPos = charbgPos
    storyPos = (440, 250)
    infoPos = (1020, 100)

    side = 'b'
    characterPicb.append(pygame.image.load(path("res/character/pingmin{}.png").format(side)))
    characterPicb.append(pygame.image.load(path("res/character/gongtou{}.png").format(side)))
    characterPicb.append(pygame.image.load(path("res/character/gansidui{}.png").format(side)))
    characterPicb.append(pygame.image.load(path("res/character/pangdun{}.png").format(side)))
    characterPicb.append(pygame.image.load(path("res/character/yaojishi{}.png").format(side)))
    characterPicb.append(pygame.image.load(path("res/character/bomb{}.png").format(side)))
    characterPicb.append(pygame.image.load(path("res/character/scientist{}.png").format(side)))
    side = 'r'
    characterPicr.append(pygame.image.load(path("res/character/pingmin{}.png").format(side)))
    characterPicr.append(pygame.image.load(path("res/character/gongtou{}.png").format(side)))
    characterPicr.append(pygame.image.load(path("res/character/gansidui{}.png").format(side)))
    characterPicr.append(pygame.image.load(path("res/character/pangdun{}.png").format(side)))
    characterPicr.append(pygame.image.load(path("res/character/yaojishi{}.png").format(side)))
    characterPicr.append(pygame.image.load(path("res/character/bomb{}.png").format(side)))
    characterPicr.append(pygame.image.load(path("res/character/scientist{}.png").format(side)))

    side = 'b'
    characterStoryb.append(pygame.image.load(path("res/characterStory/pingmin{}.png").format(side)))
    characterStoryb.append(pygame.image.load(path("res/characterStory/gongtou{}.png").format(side)))
    characterStoryb.append(pygame.image.load(path("res/characterStory/gansidui{}.png").format(side)))
    characterStoryb.append(pygame.image.load(path("res/characterStory/pangdun{}.png").format(side)))
    characterStoryb.append(pygame.image.load(path("res/characterStory/yaojishi{}.png").format(side)))
    characterStoryb.append(pygame.image.load(path("res/characterStory/bomb{}.png").format(side)))
    characterStoryb.append(pygame.image.load(path("res/characterStory/scientist{}.png").format(side)))
    side = 'r'
    characterStoryr.append(pygame.image.load(path("res/characterStory/pingmin{}.png").format(side)))
    characterStoryr.append(pygame.image.load(path("res/characterStory/gongtou{}.png").format(side)))
    characterStoryr.append(pygame.image.load(path("res/characterStory/gansidui{}.png").format(side)))
    characterStoryr.append(pygame.image.load(path("res/characterStory/pangdun{}.png").format(side)))
    characterStoryr.append(pygame.image.load(path("res/characterStory/yaojishi{}.png").format(side)))
    characterStoryr.append(pygame.image.load(path("res/characterStory/bomb{}.png").format(side)))
    characterStoryr.append(pygame.image.load(path("res/characterStory/scientist{}.png").format(side)))

    side = 'b'
    characterInfob.append(pygame.image.load(path("res/charinfo/pingmin{}.png").format(side)))
    characterInfob.append(pygame.image.load(path("res/charinfo/gongtou{}.png").format(side)))
    characterInfob.append(pygame.image.load(path("res/charinfo/gansidui{}.png").format(side)))
    characterInfob.append(pygame.image.load(path("res/charinfo/pangdun{}.png").format(side)))
    characterInfob.append(pygame.image.load(path("res/charinfo/yaojishi{}.png").format(side)))
    characterInfob.append(pygame.image.load(path("res/charinfo/bomb{}.png").format(side)))
    characterInfob.append(pygame.image.load(path("res/charinfo/scientist{}.png").format(side)))
    side = 'r'
    characterInfor.append(pygame.image.load(path("res/charinfo/pingmin{}.png").format(side)))
    characterInfor.append(pygame.image.load(path("res/charinfo/gongtou{}.png").format(side)))
    characterInfor.append(pygame.image.load(path("res/charinfo/gansidui{}.png").format(side)))
    characterInfor.append(pygame.image.load(path("res/charinfo/pangdun{}.png").format(side)))
    characterInfor.append(pygame.image.load(path("res/charinfo/yaojishi{}.png").format(side)))
    characterInfor.append(pygame.image.load(path("res/charinfo/bomb{}.png").format(side)))
    characterInfor.append(pygame.image.load(path("res/charinfo/scientist{}.png").format(side)))
    
    while True:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

            # 浮动效果
            if x > survivorPos0[0] and x < survivorPos0[0] + survivorButton.get_width() \
                    and y > survivorPos0[1] and y < survivorPos0[1] + survivorButton.get_height():
                survivorPos = survivorPos1
            else:
                survivorPos = survivorPos0

            if x > zombiePos0[0] and x < zombiePos0[0] + zombieButton.get_width() \
                    and y > zombiePos0[1] and y < zombiePos0[1] + zombieButton.get_height():
                zombiePos = zombiePos1
            else:
                zombiePos = zombiePos0

            if x > leftPos0[0] and x < leftPos0[0] + leftButton.get_width() \
                    and y > leftPos0[1] and y < leftPos0[1] + leftButton.get_height():
                leftPos = leftPos1
            else:
                leftPos = leftPos0

            if x > rightPos0[0] and x < rightPos0[0] + rightButton.get_width() \
                    and y > rightPos0[1] and y < rightPos0[1] + rightButton.get_height():
                rightPos = rightPos1
            else:
                rightPos = rightPos0

            
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
                if x > survivorPos0[0] and x < survivorPos0[0] + survivorButton.get_width() \
                    and y > survivorPos0[1] and y < survivorPos0[1] + survivorButton.get_height():
                    showSurvivorOrZombie = 0
                
                if x > zombiePos0[0] and x < zombiePos0[0] + zombieButton.get_width() \
                    and y > zombiePos0[1] and y < zombiePos0[1] + zombieButton.get_height():
                    showSurvivorOrZombie = 1
                
                if x > leftPos0[0] and x < leftPos0[0] + leftButton.get_width() \
                    and y > leftPos0[1] and y < leftPos0[1] + leftButton.get_height():
                    charID = charID - 1
                    if charID < 0:
                        charID = charID + totalNum
                
                if x > rightPos0[0] and x < rightPos0[0] + rightButton.get_width() \
                    and y > rightPos0[1] and y < rightPos0[1] + rightButton.get_height():
                    charID = charID + 1
                    if charID == totalNum:
                        charID = 0

        # 更新显示内容    
        if showSurvivorOrZombie == 0:
            CharList = characterPicb
            StoryList = characterStoryb
            InfoList = characterInfob
        else:
            CharList = characterPicr
            StoryList = characterStoryr
            InfoList = characterInfor
        
        charPic = CharList[charID]
        storyPic = StoryList[charID]
        infoPic = InfoList[charID]

        # 填充背景和内容
        screen.blit(background, (0, 0))
        screen.blit(title, titlePos)
        screen.blit(charbg, charbgPos)
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        screen.blit(survivorButton, survivorPos)
        screen.blit(zombieButton, zombiePos)
        screen.blit(leftButton, leftPos)
        screen.blit(rightButton, rightPos)
        screen.blit(charPic, charPos)
        screen.blit(storyPic, storyPos)
        screen.blit(infoPic, infoPos)

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
    from src.path import path
    from pygame.locals import *

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

    handbook(screen, clock)
   