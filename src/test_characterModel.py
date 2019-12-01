from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *


class TestCharacterModel(TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1280, 720),0,32)
        self.map_test = levelLoad(1)
        self.controller = GameController(1, self.map_test)
    
    def tearDown(self):
        for attacker in Attacker.attackers:
            attacker.die()
        for defender in Defender.defenders:
            defender.die()
        return super().tearDown()

    def test_attack(self):
        attacker = AuraAttacker(self.controller, (100, 100), 0)
        defender = CivilianDefender(self.controller, (100, 25), 2)
        attacker.attack()
        defender.attack()
        self.assertAlmostEqual(attacker.hp, 230)
        self.assertAlmostEqual(defender.hp, 70)

    def test_die(self):
        attacker = AuraAttacker(self.controller, (100, 100), 0)
        self.assertIn(attacker, Attacker.attackers)
        attacker.die()
        self.assertNotIn(attacker, Attacker.attackers)
