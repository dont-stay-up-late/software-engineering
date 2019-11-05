
import pygame

#地图在初始化之后进行显示，传入的参数为地图的左上角坐标，Map类对象，以及窗口句柄
def mapDisplay(x1,y1,map,screen):
	#图像的名称转换，包含6种不同的状态
	homeImageFile = r"image/1.jpg"
	bornPointImageFile = r"image/2.jpg"
	zeroImageFile = r"image/3.jpg"
	oneImageFile = r"image/4.jpg"
	twoImageFile = r"image/1.jpg"
	threeImageFile = r"image/2.jpg"
	#backGroundFile = r"image/background.jpg"

	#加载并转换图像
	homeImage_init = pygame.image.load(homeImageFile).convert()
	bornPointImage_init = pygame.image.load(bornPointImageFile).convert()
	zeroImage_init = pygame.image.load(zeroImageFile).convert()
	oneImage_init = pygame.image.load(oneImageFile).convert()
	twoImage_init = pygame.image.load(twoImageFile).convert()
	threeImage_init = pygame.image.load(threeImageFile).convert()
	#backGround = pygame.image.load(backGroundFile).convert()

	#地图中用于填充格子的图像的大小
	imageSize = 50

	#图像放缩，若图像大小给定，则此部分可以省去
	homeImage = pygame.transform.scale(homeImage_init,(imageSize,imageSize))
	bornPointImage = pygame.transform.scale(bornPointImage_init,(imageSize,imageSize))
	zeroImage = pygame.transform.scale(zeroImage_init,(imageSize,imageSize))
	oneImage = pygame.transform.scale(oneImage_init,(imageSize,imageSize))
	twoImage = pygame.transform.scale(twoImage_init,(imageSize,imageSize))
	threeImage = pygame.transform.scale(threeImage_init,(imageSize,imageSize))
	#backGround = pygame.transform.scale(backGround,(750,500))

	m = map.columnNumber	#地图加载时的行数
	n = map.rowNumber		#地图加载时的列数
	xBegin = x1 			#地图显示的左上角横坐标，可以根据地图的大小进行改变，取决于m,n的值
	yBegin = y1		 	    #地图显示的左上角纵坐标

	#图像在内存中存储
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
	
	
	