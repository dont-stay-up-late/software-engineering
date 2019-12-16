import pygame
from levelLoad import *
from path import path

#在生成游戏时，根据窗口的大小对map中的格子、左上角坐标进行计算和更新
def setMapUI(map,x1,y1,imageSize):
	map.xBegin=x1
	map.yBegin=y1
	map.blockSize=imageSize


#地图在初始化之后进行显示，传入的参数为Map类对象和窗口句柄
def mapDisplay(map,screen,mapImage):
	#地图中用于填充格子的图像的大小
	imageSize = map.blockSize
	# mapImage = (homeImage, bornPointImage, zeroImage, oneImage, twoImage, threeImage, arrowImage)
	homeImage = mapImage[0]
	bornPointImage = mapImage[1]
	zeroImage = mapImage[2]
	oneImage = mapImage[3]
	twoImage = mapImage[4]
	threeImage = mapImage[5]
	sixImage = mapImage[6]
	arrowImage = mapImage[7]
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
			elif map.maps[i][j].isPathway:
				screen.blit(sixImage,(x,y))

			if map.maps[i][j].blockDirection!=-1:
				screen.blit(arrowImage[map.maps[i][j].blockDirection],(x,y))



