from map import *
from path import path

#这是从文件中加载关卡信息

#加载关卡i的数据(int值)，从文件读取到一个元祖中
#元组第一项为地图的行和列数，第二项为地图中的block信息
def dataLoad(i):
	level = path("res/levelData/level" + str(i) + ".txt")
	fileP = open(level,mode = 'r')
	columnAndRow = []		#加载地图的行和列
	blockData = []			#加载地图中的方块信息
	directionData = []		#加载地图中的方向信息
	t = fileP.readline(4)
	t = t.strip('\n')
	#print(t)
	columnAndRow.append(int(t))		#行，6行
	t = fileP.readline(4)
	t = t.strip('\n')
	#print(t)
	columnAndRow.append(int(t))		#列，10列
	while (1):
		a = fileP.read(1)
		if a == "*":
			break
		if a == "\n" or a == "\r":
			continue
		blockData.append(int(a))
		
	s=""
	l=[]
	while (1):
		a=fileP.read(1)
		if a == "*":
			s=""
			break
		if  a==" " or a==",":
			if s!="":
				l.append(int(s))
			s=""
			continue
		if a=="\n" or a=="\r":
			if s!="":
				l.append(int(s))
			if len(l)==3:
				directionData.append(l)
			l=[]
			s=""
			continue	
		s+=a

	fileP.close()
	levelData = (columnAndRow,blockData,directionData)
	return levelData

#利用关卡的数据完成地图的初始化,并返回一个Map类的对象
def levelLoad(i):
	levelData = dataLoad(i)
	#m = map.columnNumber
	#n = map.rowNumber
	m = levelData[0][0]
	n = levelData[0][1]
	map = Map(m,n)
	for i in range(m):
		for j in range(n):
			k = levelData[1][i*n + j]
			#如果为家，对应于数字4
			if k == 4:
				map.setHome(i,j)
			#如果为出生点，对应于数字5
			elif k == 5:
				map.setBornPoint(i,j)
			elif k == 6:
				map.setPathway(i,j)
			else:
				map.setSomeBlock(i,j,k)
			
	for i in levelData[2]:
		map.setBlockDirection(i[0],i[1],i[2])
	return map

#a = levelLoad(1)
#print(a[0])
#print(a[1])
			

