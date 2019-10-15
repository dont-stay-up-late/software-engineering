import pygame
from pygame.locals import *
from sys import exit

# from levelLoad import levelLoad,dataLoad
# from map import Map
from levelLoad import *
from map import *

pygame.init()


#地图在初始化之后进行显示，传入的参数为Map类对象
def mapDisplay(map):
	#图像的名称转换，包含6种不同的状态
	homeImageFile = r"image/1.jpg"
	bornPointImageFile = r"image/2.jpg"
	zeroImageFile = r"image/3.jpg"
	oneImageFile = r"image/4.jpg"
	twoImageFile = r"image/1.jpg"
	threeImageFile = r"image/2.jpg"
	backGroundFile = r"image/background.jpg"

	#创建窗口以及窗口标题，窗口大小为750*500
	screen = pygame.display.set_mode((750,500),0,32)
	pygame.display.set_caption("test")
	
	#加载并转换图像
	homeImage_init = pygame.image.load(homeImageFile).convert()
	bornPointImage_init = pygame.image.load(bornPointImageFile).convert()
	zeroImage_init = pygame.image.load(zeroImageFile).convert()
	oneImage_init = pygame.image.load(oneImageFile).convert()
	twoImage_init = pygame.image.load(twoImageFile).convert()
	threeImage_init = pygame.image.load(threeImageFile).convert()
	backGround = pygame.image.load(backGroundFile).convert()

	#地图中用于填充格子的图像的大小
	imageSize = 50

	#图像放缩，若图像大小给定，则此部分可以省去
	homeImage = pygame.transform.scale(homeImage_init,(imageSize,imageSize))
	bornPointImage = pygame.transform.scale(bornPointImage_init,(imageSize,imageSize))
	zeroImage = pygame.transform.scale(zeroImage_init,(imageSize,imageSize))
	oneImage = pygame.transform.scale(oneImage_init,(imageSize,imageSize))
	twoImage = pygame.transform.scale(twoImage_init,(imageSize,imageSize))
	threeImage = pygame.transform.scale(threeImage_init,(imageSize,imageSize))
	backGround = pygame.transform.scale(backGround,(750,500))

	m = map.columnNumber	#地图加载时的行数
	n = map.rowNumber		#地图加载时的列数
	xBegin = 50				#地图显示的左上角横坐标，可以根据地图的大小进行改变，取决于m,n的值
	yBegin = 50				#地图显示的左上角横坐标
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				# 接收到退出事件后退出程序
				exit()
		screen.blit(backGround,(0,0))			#显示背景图像
		#图像显示
		for i in range(m):
			y = i*imageSize + yBegin
			for j in range(n):
				x = j*imageSize + xBegin
				if map.maps[i][j].isHome:
					screen.blit(homeImage,(x,y))
				elif map.maps[i][j].isBornPoint:
					screen.blit(bornPointImage,(x,y))
				elif map.maps[i][j].canPlantOn and map.maps[i][j].canZombieOn:
					screen.blit(zeroImage,(x,y))
				elif (not map.maps[i][j].canPlantOn) and map.maps[i][j].canZombieOn:
					screen.blit(oneImage,(x,y))
				elif map.maps[i][j].canPlantOn and (not map.maps[i][j].canZombieOn):
					screen.blit(twoImage,(x,y))
				else:
					screen.blit(threeImage,(x,y))
		pygame.display.update()
		
map_test = levelLoad(1)
mapDisplay(map_test)
	
	