from src.map import *
from src.path import path


# 这是从文件中加载单人防守关卡出怪信息

# 加载关卡i的数据(int值)，从文件读取到一个元祖中
# 元组第一项为时间，第二项为怪物编号，第三项为出口，第四项为路径
def defenderload(i):
    level = path("res/levelData/level" + str(i) + "_attack.txt")
    fileP = open(level, mode='r')
    defendtime = []  # 加载出生时间
    defenderID = []  # 加载角色ID
    defenderbornx = []  # 加载出生点横坐标
    defenderborny = []  # 加载出生点纵坐标
    defenderdir = []  # 加载进攻路径
    count = 0
    while True:
        a = fileP.readline()
        a = a.strip()
        if a == "*":
            break
        a_array = a.split(" ")
        defendtime.append(int(a_array[0]))
        defenderID.append(int(a_array[1]))
        defenderbornx.append(int(a_array[3]))
        defenderborny.append(int(a_array[2]))
        defenderdir.append(int(a_array[4]))


    fileP.close()
    defenderload = (defendtime, defenderID, defenderbornx, defenderborny, defenderdir)
    return defenderload



