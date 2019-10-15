#这是写格子类和地图类的头文件

class Block:
    #'格子类'
    canPlantOn=True       #清醒的人能否站在这个格子上
    canZombieOn=True      #感染的人能否站在这个格子上
    isPlantOn=False       #是否有清醒的人站在这个格子上
    isZombieOn=False      #是否有感染的人站在这个格子上
    isHome=False          #是否为家（感染者往这个地方走）
    isBornPoint=False     #是否为出生点（感染者从这里出来）

    def setBlock(self,styleNum):    #给出一个数字来确定该格子的初始状态：0：都能放；1：感染者可走，清醒者不能放；2：感染者不能走，清醒者可放；3：都不能放
        if styleNum%2==1:
            self.canPlantOn=False
        if styleNum//2==1:
            self.canZombieOn=False

class Map:
    #'地图类'
    rowNumber=15           #列数
    columnNumber=10         #行数
    maps=[]                 #二维列表，里面放格子

    #def __init__(self,m = 10,n = 15):
    def __init__(self,m,n):                    #构造一个m*n(m行n列)的空地图
        self.rowNumber=n
        self.columnNumber=m
        for i in range(m): 
            self.maps.append([]) 
            for j in range(n):
                b=Block()
                self.maps[i].append(b)

    def setSomeBlock(self,i,j,styleNumber):     #将(i,j)位置的格子设置成某个状态
        self.maps[i][j].setBlock(styleNumber)

    def setHome(self,i,j):              #将(i,j)位置的格子设成家
        self.maps[i][j].isHome=True

    def setBornPoint(self,i,j):              #将(i,j)位置的格子设成出生点
        self.maps[i][j].isBornPoint=True

   

