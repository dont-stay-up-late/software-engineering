import pygame,sys,time
from pygame.locals import *
from map import *
from mapDisplay import *
from models import *
from gamecontroller import *


#战斗界面的UI，实现角色移动、防守方攻击、伤害判定、死亡等，测试版本

pygame.init()
screen = pygame.display.set_mode((750,500),0,32)
pygame.display.set_caption("test_combat_UI")

#地图准备
level = 1
map_test = levelLoad(1)
controller = GameController(level,map_test)
#mapDisplay(map_test,screen)

#角色准备
attackers = []
deffenders = []
for i in range(3):
	attackers.append(AuraAttacker(controller,[(9+0.5)*map_test.blockSize+map_test.xBegin,(1+0.5)*map_test.blockSize+map_test.yBegin],0))
	deffenders.append(CivilianDefender(controller,[(i+1+0.5)*map_test.blockSize+map_test.xBegin,(1+0.5)*map_test.blockSize+map_test.yBegin],0))
attackerFile = r"image/CvilianAttacker.jpg"
deffenderFile = r"image/CivilianDeffender.jpg"
attackerImage = pygame.image.load(attackerFile).convert()
deffenderImage = pygame.image.load(deffenderFile).convert()
attackerImage = pygame.transform.scale(attackerImage,(50,50))
deffenderImage = pygame.transform.scale(deffenderImage,(50,50))


#计时准备
COUNT = pygame.USEREVENT + 1
pygame.time.set_timer(COUNT,33) #每0.001秒发一次
counts = 0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			# 接收到退出事件后退出程序
			exit()
		if event.type == COUNT:
			counts = counts + 1
			#防守方攻击，攻击方死亡判定
			if counts % 10 == 0:
				for i in range(len(deffenders)):
					deffenders[i].attack()
			for attacker in attackers:
				if attacker.hp <= 0:
					attackers.remove(attacker)
			#攻击方移动，攻击，防守方死亡判定
			for i, attacker in enumerate(attackers):
				if i == 1 and counts < 200:
					break
				if i == 2 and counts < 400:
					break
				#print("attackers[%d].position:%f,%f"%(1,attackers[1].position[0],attackers[1].position[1]))
				attacker.move()
				if update_direction(attacker,map_test):
					attackers.remove(attacker)
				if counts % 10 == 0:
					attacker.attack()
			for deffender in deffenders:
				if deffender.hp <= 0:
					deffenders.remove(deffender)

			#绘制变化后的场景
			#screen.fill((255,255,0))
			mapDisplay(map_test,screen)
			for i in range(3):
				if i < len(deffenders):
					block = map_test.positionToBlock(deffenders[i].position)
					x = block[0]*map_test.blockSize+map_test.xBegin
					y = block[1]*map_test.blockSize+map_test.yBegin
					screen.blit(deffenderImage,(x,y))
				if i < len(attackers):
					x = attackers[i].position[0] - 0.5*map_test.blockSize
					y = attackers[i].position[1] - 0.5*map_test.blockSize
					screen.blit(attackerImage,(x,y))
					#print("The image location is : %f,%f"%(x,y))
					print("The attacks[%d]'s HP is : %d"%(i,attackers[i].hp))
	#print("attackers[%d].position:%f,%f" % (1, attackers[1].position[0], attackers[1].position[1]))
	pygame.display.update()