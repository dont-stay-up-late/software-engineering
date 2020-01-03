import pygame
import sys
from pygame.locals import *
from src.path import path
from src.bgm import playBgm

# 选择角色
# modeID为游戏模式编号，mapID为地图编号
def selectCharacters(screen, clock, modeID, mapID):
    background = (255, 255, 255)
    breakflag = 0
    infoflag = 0
    # playBgm(1)
    # 编队
    CharID = []     #存储选中的角色编号，传入到战斗界面
    totalNum = 9    #可选中角色总数
    chooseNum = 0   #选中的角色数量
    characterFlamePos = []   #人物框的位置
    characterPic0 = []   #未上锁的人物图片
    characterPic = []    #当前人物栏的人物状态图
    loadpathNotLocked = []  #未上锁人物图路径
    loadpathLocked = [] #上锁人物图路径
    charInfoList = []   # 人物信息
    charactersInTeam = [1, 1, 1, 1, 1, 1, 1, 1, 1]    #人物状态，是否编入队伍，是为0,否为1
    modeIntroAddress = path("res/pic/modeintro" + str(modeID) + ".png")

    # 图片及位置
    if modeID == 1 or modeID == 3:
        background = pygame.image.load(path("res/bg/bg_character_att.png")).convert()
        stringc = "r"
    else:
        background = pygame.image.load(path("res/bg/bg_character_def.png")).convert()
        stringc = "b"

    backButton = pygame.image.load(path("res/button/back.png")).convert_alpha()
    backPos = (0, 0)
    homeButton = pygame.image.load(path("res/button/home.png")).convert_alpha()
    homePos = (150, 0)
    startButton = pygame.image.load(path("res/button/sure.png")).convert_alpha()
    startPos = (1080, 653)
    characterTitle = pygame.image.load(path("res/pic/chartitle.png")).convert_alpha()
    characterTitlePos = (340, 0)
    modeIntro = pygame.image.load(modeIntroAddress).convert_alpha()
    modeIntroPos = (980, 0)
    #   人物框
    characterFlame = pygame.image.load(path("res/character/charflame.png")).convert_alpha()
    #   编队框
    teamFlame = pygame.image.load(path("res/character/teamflame.png")).convert_alpha()
    teamFlamePos = (255, 520)
    characterInfoPos = (0,100)
    # 人物框加载路径
    if modeID == 2:
        side = 'b' # single defend
    elif modeID == 1:
        side = 'r' # single attack
    loadpathNotLocked.append(path("res/character/pingmin{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/gongtou{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/gansidui{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/pangdun{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/yaojishi{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/bomb{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/scientist{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/bully{}.png".format(side)))
    loadpathNotLocked.append(path("res/character/fully{}.png".format(side)))
    loadpathLocked.append(path("res/character/pingmin{}s.png".format(side)))
    loadpathLocked.append(path("res/character/gongtou{}s.png".format(side)))
    loadpathLocked.append(path("res/character/gansidui{}s.png".format(side)))
    loadpathLocked.append(path("res/character/pangdun{}s.png".format(side)))
    loadpathLocked.append(path("res/character/yaojishi{}s.png".format(side)))
    loadpathLocked.append(path("res/character/bomb{}s.png".format(side)))
    loadpathLocked.append(path("res/character/scientist{}s.png".format(side)))
    loadpathLocked.append(path("res/character/bully{}s.png".format(side)))
    loadpathLocked.append(path("res/character/fully{}s.png".format(side)))

    charInfoList.append(pygame.image.load(path("res/charinfo/pingmin{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/gongtou{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/gansidui{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/pangdun{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/yaojishi{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/bomb{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/scientist{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/bully{}.png".format(side))).convert_alpha())
    charInfoList.append(pygame.image.load(path("res/charinfo/fully{}.png".format(side))).convert_alpha())

    for i in range(0, totalNum):
        characterPic0.append(pygame.image.load(loadpathNotLocked[i]).convert_alpha())
        characterPic.append(pygame.image.load(loadpathNotLocked[i]).convert_alpha())
        characterFlamePos.append((255 + i * 100, 250))
    while True:
        x, y = pygame.mouse.get_pos()
        # 根据鼠标悬停显示对应的角色信息
        # 不悬停则不显示
        infoflag = 0
        for i in range (0, totalNum):
            if x > characterFlamePos[i][0] and x < characterFlamePos[i][0] + characterFlame.get_width() \
                and y > characterFlamePos[i][1] and y < characterFlamePos[i][1] + characterFlame.get_height():
                Charinfo = charInfoList[i]
                infoflag = 1
        for i in range (0, chooseNum):
            if x > 255 + 100 * i and x < 255 + 100 * i + characterFlame.get_width() \
                and y > 520 and y < 520 + characterFlame.get_height():
                Charinfo = charInfoList[CharID[i]]
                infoflag = 1

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
                breakflag = 1

            if event.type == MOUSEBUTTONDOWN:
                if x > backPos[0] and x < backPos[0] + backButton.get_width() \
                        and y > backPos[1] and y < backPos[1] + backButton.get_height():
                    from src.selectMap import selectMap
                    selectMap(screen, clock, modeID)
                    breakflag = 1
                    # here to come back

                if x > homePos[0] and x < homePos[0] + homeButton.get_width() \
                        and y > homePos[1] and y < homePos[1] + homeButton.get_height():
                    from src.initialMenu import initialMenu
                    initialMenu(screen, clock)
                    breakflag = 1
                    # here to come back home

                if x > startPos[0] and x < startPos[0] + startButton.get_width() \
                        and y > startPos[1] and y < startPos[1] + startButton.get_height():
                    from src.fighting import startFight
                    startFight(screen, clock, modeID, mapID, CharID)
                    breakflag = 1
                    # here to start the game

                for i in range (0, totalNum):
                    if x > characterFlamePos[i][0] and x < characterFlamePos[i][0] + characterFlame.get_width() \
                            and y > characterFlamePos[i][1] and y < characterFlamePos[i][1] + characterFlame.get_height():
                        charactersInTeam[i] = -charactersInTeam[i]
                        # Charinfo = charInfoList[i]
                        # infoflag = 1
                        if charactersInTeam[i] == 1:
                            characterPic[i] = pygame.image.load(loadpathNotLocked[i]).convert_alpha()
                            CharID.remove(i)
                            chooseNum = chooseNum - 1
                        else:
                            if chooseNum <= 7:
                                characterPic[i] = pygame.image.load(loadpathLocked[i]).convert_alpha()
                                CharID.append(i)
                                chooseNum = chooseNum + 1
                            else:
                                charactersInTeam[i] = 1

                for i in range (0, chooseNum):
                    if x > 255 + 100 * i and x < 255 + 100 * i + characterFlame.get_width() \
                            and y > 520 and y < 520 + characterFlame.get_height():
                        charactersInTeam[CharID[i]] = - charactersInTeam[CharID[i]]
                        # Charinfo = pygame.image.load(path("res/charinfo/Charinfo.png")).convert_alpha()
                        if charactersInTeam[CharID[i]] == 1:
                            characterPic[CharID[i]] = pygame.image.load(loadpathNotLocked[CharID[i]]).convert_alpha()
                            del CharID[i]
                            chooseNum = chooseNum - 1

        # 填充背景和内容
        screen.blit(background, (0, 0))
        screen.blit(backButton, backPos)
        screen.blit(homeButton, homePos)
        if chooseNum > 0:
            screen.blit(startButton, startPos)
        screen.blit(characterTitle, characterTitlePos)
        screen.blit(modeIntro, modeIntroPos)
        screen.blit(teamFlame, teamFlamePos)
        if infoflag == 1:
            screen.blit(Charinfo, characterInfoPos)
        for i in range(0, totalNum):
            screen.blit(characterFlame, characterFlamePos[i])
            screen.blit(characterPic[i], characterFlamePos[i])
        for i in range(0, chooseNum):
            screen.blit(characterPic0[CharID[i]], (255 + 100 * i, 520))
        # 更新画面
        pygame.display.update()
        # 帧率
        clock.tick(40)
        if breakflag == 1:
            break

