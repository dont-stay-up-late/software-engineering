import pygame
from levelLoad import *
from path import path

#在生成游戏时，根据窗口的大小对map中的格子、左上角坐标进行计算和更新
def setMapUI(map,x1,y1,imageSize):
	map.xBegin=x1
	map.yBegin=y1
	map.blockSize=imageSize


#地图在初始化之后进行显示，传入的参数为Map类对象和窗口句柄
def mapDisplay(map,screen):
	#图像的名称转换，包含6种不同的状态
	homeImageFile = path("image/home.png")
	bornPointImageFile = path("image/born.png")
	zeroImageFile = path("image/3.jpg")
	oneImageFile = path("image/4.jpg")
	twoImageFile = path("image/1.jpg")
	threeImageFile = path("image/2.jpg")
	arrowImageFile = [path("image/arrow0.png"),path("image/arrow1.png"),path("image/arrow2.png"),path("image/arrow3.png")]

	#加载并转换图像
	homeImage_init = pygame.image.load(homeImageFile).convert_alpha()
	bornPointImage_init = pygame.image.load(bornPointImageFile).convert_alpha()
	zeroImage_init = pygame.image.load(zeroImageFile).convert()
	oneImage_init = pygame.image.load(oneImageFile).convert()
	twoImage_init = pygame.image.load(twoImageFile).convert()
	threeImage_init = pygame.image.load(threeImageFile).convert()
	arrowImage_init = []
	for image in arrowImageFile:
		arrowImage_init.append(pygame.image.load(image).convert_alpha())
	#backGround = pygame.image.load(backGroundFile).convert()

	#地图中用于填充格子的图像的大小
	imageSize = map.blockSize 

	#图像放缩，若图像大小给定，则此部分可以省去
	homeImage = pygame.transform.scale(homeImage_init,(imageSize,imageSize))
	bornPointImage = pygame.transform.scale(bornPointImage_init,(imageSize,imageSize))
	zeroImage = pygame.transform.scale(zeroImage_init,(imageSize,imageSize))
	oneImage = pygame.transform.scale(oneImage_init,(imageSize,imageSize))
	twoImage = pygame.transform.scale(twoImage_init,(imageSize,imageSize))
	threeImage = pygame.transform.scale(threeImage_init,(imageSize,imageSize))
	arrowImage = []
	for image_init in arrowImage_init:
		arrowImage.append(pygame.transform.scale(image_init,(imageSize,imageSize)))
	#backGround = pygame.transform.scale(backGround,(750,500))

	m = map.columnNumber	#地图加载时的行数
	n = map.rowNumber		#地图加载时的列数
	xBegin = map.xBegin			#地图显示的左上角横坐标，可以根据地图的大小进行改变，取决于m,n的值
	yBegin = map.yBegin		 	#地图显示的左上角纵坐标

	#图像在内存中存储
	for i in range(m):
		y = i*imageSize + yBegin
		for j in range(n):
			x = j*imageSize + xBegin
			if map.maps[i][j].canPlantOn and map.maps[i][j].canZombieOn:
				screen.blit(zeroImage,(x,y))
			elif (not map.maps[i][j].canPlantOn) and map.maps[i][j].canZombieOn:
				screen.blit(oneImage,(x,y))
			elif map.maps[i][j].canPlantOn and (not map.maps[i][j].canZombieOn):
				screen.blit(twoImage,(x,y))
			else:
				screen.blit(threeImage,(x,y))

			if map.maps[i][j].isHome:
				screen.blit(homeImage,(x,y))
			elif map.maps[i][j].isBornPoint:
				screen.blit(bornPointImage,(x,y))
			elif map.maps[i][j].blockDirection!=-1:
				screen.blit(arrowImage[map.maps[i][j].blockDirection],(x,y))



