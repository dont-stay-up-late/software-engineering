from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *

class TestAttacker(TestCase):
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
    
    def test_move(self):
        attacker = CivilianAttacker(self.controller, [100, 100], 1)
        attacker.move()
        self.assertEqual(attacker.position, [99, 100])