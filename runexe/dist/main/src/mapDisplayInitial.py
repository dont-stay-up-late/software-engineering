import pygame
from src.levelLoad import *
from src.path import path

#地图图片的加载初始化
def mapDisplayInitial(map,screen):
	#图像的名称转换，包含6种不同的状态
	homeImageFile = path("res/mapblock/home.png")
	bornPointImageFile = path("res/mapblock/born.png")
	zeroImageFile = path("res/mapblock/4.jpg")
	oneImageFile = path("res/mapblock/1.jpg")
	twoImageFile = path("res/mapblock/3.jpg")
	threeImageFile = path("res/mapblock/2.jpg")
	sixImageFile = path("res/mapblock/6.png")
	arrowImageFile = [path("res/mapblock/arrow0.png"),path("res/mapblock/arrow1.png"),path("res/mapblock/arrow2.png"),path("res/mapblock/arrow3.png")]

	#加载并转换图像
	homeImage_init = pygame.image.load(homeImageFile).convert_alpha()
	bornPointImage_init = pygame.image.load(bornPointImageFile).convert_alpha()
	zeroImage_init = pygame.image.load(zeroImageFile).convert()
	oneImage_init = pygame.image.load(oneImageFile).convert()
	twoImage_init = pygame.image.load(twoImageFile).convert()
	threeImage_init = pygame.image.load(threeImageFile).convert()
	sixImage_init = pygame.image.load(sixImageFile).convert()
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
	sixImage = pygame.transform.scale(sixImage_init, (imageSize, imageSize))
	arrowImage = []
	for image_init in arrowImage_init:
		arrowImage.append(pygame.transform.scale(image_init,(imageSize,imageSize)))
	#backGround = pygame.transform.scale(backGround,(750,500))
	mapImage = (homeImage, bornPointImage, zeroImage, oneImage, twoImage, threeImage, sixImage, arrowImage)
	return mapImage

