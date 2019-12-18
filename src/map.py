# 这是写格子类和地图类的头文件


class Block:
    # '格子类'
    def __init__(self):
        self.canPlantOn = True  # 清醒的人能否站在这个格子上
        self.canZombieOn = True  # 感染的人能否站在这个格子上
        self.isPlantOn = False  # 是否有清醒的人站在这个格子上
        self.isZombieOn = False  # 是否有感染的人站在这个格子上
        self.isHome = False  # 是否为家（感染者往这个地方走,不可放置防守方）
        self.isBornPoint = False  # 是否为出生点（感染者从这里出来）
        self.isPathway = False  #是否为轨道（感染者可切换进攻路径，防守者不可放置，不可放置防守方）

        self.blockDirection = -1  # 僵尸走上格子时改变的方向，-1为不改变方向，0123为上左下右，若可变则该变量为元组
        self.blockDirections=[]
        self.directionNum=0
        self.directionOrder=0

    def setBlock(self, styleNum):  # 给出一个数字来确定该格子的初始状态：0：都能放；1：感染者可走，清醒者不能放；2：感染者不能走，清醒者可放；3：都不能放
        if styleNum % 2 == 1:
            self.canPlantOn = False
        if styleNum//2 == 1:
            self.canZombieOn = False

    def changeDirection(self):  # 若这个格子可以变化方向则变之
        if self.directionNum >1 :
            self.directionOrder = (self.directionOrder+1) % self.directionNum
            self.blockDirection = self.blockDirections[self.directionOrder]


class Map:
    # '地图类'

    # def __init__(self,m = 6,n = 10):
    def __init__(self, m, n):  # 构造一个m*n(m行n列)的空地图
        self.rowNumber = n      # 列数
        self.columnNumber = m   # 行数
        self.fortress_HP = 3   #初始生命，先设成3
        self.time_limit = 180   #时间限制，以秒为单位
        self.PathwayCD = 5   #切换轨道的冷却时间

        self.maps = []  # 二维列表，里面放格子
        self.homes = []  # 元组列表，里面放所有的家
        self.Pathways = []  # 二维列表，里面放所有的轨道
        self.PathwaysShiftTime = []  # 存储上次轨道切换的时间
        self.bornPoints = []  # 元组列表，里面放所有的出生点

        # 下面是UI所需的一些变量，都是像素为单位
        self.blockSize = 75  # 每个格子为正方形，这个是边长
        self.xBegin = 265  # 左上角横坐标
        self.yBegin = 70  # 左上角纵坐标

        for i in range(m):
            self.maps.append([])
            for j in range(n):
                b = Block()
                self.maps[i].append(b) # maps第一元素是行数，即y，第二元素是列数，即x

    def setSomeBlock(self, i, j, styleNumber):  # 将(i,j)位置的格子设置成某个状态
        self.maps[i][j].setBlock(styleNumber)

    def setHome(self, i, j):  # 将(i,j)位置的格子设成家
        self.maps[i][j].isHome = True
        self.setSomeBlock(i, j, 1)
        self.homes.append((i, j))

    def setBornPoint(self, i, j):  # 将(i,j)位置的格子设成出生点
        self.maps[i][j].isBornPoint = True
        self.setSomeBlock(i, j, 1)
        self.bornPoints.append((i, j))

    def setPathway(self, i, j):    # 将(i,j)位置的格子设成轨道
        self.maps[i][j].isPathway = True
        self.setSomeBlock(i, j, 1)
        self.Pathways.append((i, j))
        self.PathwaysShiftTime.append(- self.PathwayCD)

    # 将(i,j)位置的格子赋上方向,若能是多个方向，则多次输入即可，含着能变为的所有方向
    def setBlockDirection(self, i, j, k):
        if self.maps[i][j].blockDirections.count(k)==0:
            if self.maps[i][j].blockDirection==-1:
                self.maps[i][j].blockDirection = k
            self.maps[i][j].directionNum=1
            self.maps[i][j].blockDirections.append(k)
        
        # 若该格子能变化方向：就加三个变量：blockDirections记录元组,directionNum记录方向数，directionOrder记录现在是哪个方向

    def positionToBlock(self, position):  # 将position这个位置元组（像素为单位）变成格子元组(方便点击时等情况调用)
        x = int((position[0]-self.xBegin)/self.blockSize)
        y = int((position[1]-self.yBegin)/self.blockSize)
        if x < 0 or y < 0 or y >= self.columnNumber or x >= self.rowNumber:
            # 如果位置出界，则返回(-1,-1)
            return [-1, -1]
        else:
            return[x,y]  # 这里返回的x和y指的是坐标

    def blockToPosition(self, blockPosition):  # 将blockPosition中心的像素位置输出
        x=int((blockPosition[0]+0.5)*self.blockSize+self.xBegin)
        y=int((blockPosition[1]+0.5)*self.blockSize+self.yBegin)
        return [x,y]

    # 轨的使用
    def update_Pathway(self, coordinate, olddirection):
        k = len(self.maps[coordinate[1]][coordinate[0]].blockDirections)
        for i in range(k):
            if self.maps[coordinate[1]][coordinate[0]].blockDirections[i] == olddirection:
                if i == k - 1:
                    self.maps[coordinate[1]][coordinate[0]].blockDirection = \
                    self.maps[coordinate[1]][coordinate[0]].blockDirections[0]
                else:
                    self.maps[coordinate[1]][coordinate[0]].blockDirection = \
                    self.maps[coordinate[1]][coordinate[0]].blockDirections[i + 1]

#攻击者每次刷新都调用这个函数，重新确定移动方向
def update_direction(attacker,map):
    # Return True if attacker die in this method.
    x=(attacker.position[0]-map.xBegin)/map.blockSize
    y=(attacker.position[1]-map.yBegin)/map.blockSize
    i=int(y)   # 因为maps的是行列，对应（y,x)，逻辑上有问题
    j=int(x)

    if i<0 or j<0 or i>=map.columnNumber or j>=map.rowNumber:
        #如果某个进攻者跑出了地图，需要一些机制来报错，现在让它直接消失好了
        attacker.die()
        return True
    if map.maps[i][j].isHome==True:
        map.fortress_HP-=1
        #这里再加一些进家时的代码
        return True
    map.maps[i][j].isZombieOn=True
    d=attacker.direction
    if (d==0 and y-i<=0.5) or (d==1 and x-j<=0.5) or (d==2 and y-i>=0.5) or (d==3 and x-j>=0.5): 
        if map.maps[i][j].blockDirection!=-1:
            attacker.direction=map.maps[i][j].blockDirection
    #更新攻击者方向

    return False

