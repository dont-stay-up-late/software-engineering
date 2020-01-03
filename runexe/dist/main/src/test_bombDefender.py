from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *
from time import sleep

class TestBombDefender(TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1280, 720), 0, 32)
        self.map_test = levelLoad(1)
        self.controller = GameController(1, self.map_test)

    def tearDown(self):
        for attacker in Attacker.attackers:
            attacker.die()
        for defender in Defender.defenders:
            defender.die()
        return super().tearDown()
    
    def test_update(self):
        # Die after 1.5 seconds and all opponents within reach model are subject to attack of its current hp
        bomb = BombDefender(self.controller, [100, 100], 0)
        opponent1 = CivilianDefender(self.controller, [25, 100], 0)
        opponent2 = FattyAttacker(self.controller, [100, 25], 0)
        sleep(1.5)
        bomb.update()
        self.assertNotIn(opponent1, Attacker.attackers)
        self.assertAlmostEqual(opponent2.hp, 205)
