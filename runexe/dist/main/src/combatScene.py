import pygame
from pygame.locals import *
from sys import exit

from src.mapDisplay import *
from src.levelLoad import levelLoad
from src.map import *
from src.path import path
		
		
#进行战斗画面绘制的函数，传入的函数为Map类对象，选定的角色列表，道具列表，窗口句柄
#根据需要，还需要传入攻击方和防守方角色的列表等，可修改
def combatScene(map,selectedRoleList,toolsList,screen):
	#战斗界面时整体的背景图，大小为750×500
	bgImageFile = path('image/combatSceneBg.jpg')
	bgImage_init = pygame.image.load(bgImageFile).convert()
	bgImage = pygame.transform.scale(bgImage_init,(750,500))
	screen.blit(bgImage,(0,0))
	
	#定义一些帮助确定位置的坐标，以地图的位置为参考
	mapLeft = 50
	mapTop = 20
	mapButtom = 420
	mapRight = 700
	
	setMapUI(map,mapLeft,mapTop,50)

	mapAreaDraw(map,screen)
	
	roleInfoAreaDraw(0,mapTop,mapLeft,200)
	
	costAreaDraw(0,mapButtom,mapLeft,500)
	
	cardAreaDraw(mapLeft,mapButtom,mapRight,500,selectedRoleList)
	
	toolAreaDraw(mapRight,mapTop,750,mapButtom,toolsList)
	
#绘制地图区，包括基本地图和各种角色
def mapAreaDraw(map,screen):
    mapDisplay( map , screen )
	#attackersDisplay()
	#defendersDiaplay()

#绘制战斗界面左侧的角色消息区域	
def roleInfoAreaDraw(x1,y1,x2,y2):
	#绘制背景图部分，其余部分有待填充，下同
	RoleInfoFile = path('image/roleInfoBg.jpg')
	RoleInfoImage_init = pygame.image.load(RoleInfoFile).convert()
	RoleInfoImage = pygame.transform.scale(RoleInfoImage_init,(x2-x1,y2-y1))
	screen.blit(RoleInfoImage,(x1,y1))

#绘制费用区域
def costAreaDraw(x1,y1,x2,y2):
	costFrameFile = path('image/costFrameBg.jpg')
	costFrame_init = pygame.image.load(costFrameFile).convert()
	costFrameImage = pygame.transform.scale(costFrame_init,(x2-x1,y2-y1))
	screen.blit(costFrameImage,(x1,y1))

#绘制选定的角色区域，含背景和角色卡片
#传入的参数为卡牌区的左上和右下角坐标，以及卡牌列表
def cardAreaDraw(x1,y1,x2,y2,selectedRolesList):
	cardBgFile = path('image/cardBg.jpg')
	cardBg_init = pygame.image.load(cardBgFile).convert()
	cardBg = pygame.transform.scale(cardBg_init,(x2-x1,y2-y1))
	screen.blit(cardBg,(x1,y1))

#绘制道具区域，包含背景和道具
#传入的参数为工具区的左上和右下角坐标，以及工具列表
def toolAreaDraw(x1,y1,x2,y2,toolsList):
	toolBgFile = path('image/toolBg.jpg')
	toolBg_init = pygame.image.load(toolBgFile).convert()
	toolBg = pygame.transform.scale(toolBg_init,(x2-x1,y2-y1))
	screen.blit(toolBg,(x1,y1))	
	
#用于测试#
pygame.init()
screen = pygame.display.set_mode((750,500),0,32)
pygame.display.set_caption("test_combatScene")
map_test = levelLoad(1)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			# 接收到退出事件后退出程序
			exit()
	selectedRoleList_test = []
	toolsList_test = []
	combatScene(map_test,selectedRoleList_test,toolsList_test,screen)
	pygame.display.update()	
	
	