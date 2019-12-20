from map import *
from path import path


# 这是从文件中加载单人防守关卡出怪信息

# 加载关卡i的数据(int值)，从文件读取到一个元祖中
# 元组第一项为时间，第二项为怪物编号，第三项为出口，第四项为路径
def attackerload(i):
    level = path("res/levelData/level" + str(i) + "_defend.txt")
    fileP = open(level, mode='r')
    attacktime = []  # 加载出生时间
    attackerID = []  # 加载角色ID
    attackerborn = []  # 加载出生点
    attackerpathtime = []  # 切换轨道的时间
    attackerpathx = []    #切换轨道的位置
    attackerpathy = []
    count = 0
    while True:
        a = fileP.readline()
        a = a.strip()
        if a == "*":
            break
        a_array = a.split(" ")
        attacktime.append(int(a_array[0]))
        attackerID.append(int(a_array[1]))
        attackerborn.append(int(a_array[2]))

    while True:
        a = fileP.readline()
        a = a.strip()
        if a == "*":
            break
        a_array = a.split(" ")
        attackerpathtime.append(int(a_array[0]))
        attackerpathx.append(int(a_array[1]))
        attackerpathy.append(int(a_array[2]))

    fileP.close()
    attackerload1 = (attacktime, attackerID, attackerborn)
    attackerload2 = (attackerpathtime, attackerpathx, attackerpathy)
    return (attackerload1,attackerload2)



