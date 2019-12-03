from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *

class TestAuraDefender(TestCase):
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
        # Amplifies friends within reach model
        aura = AuraDefender(self.controller, [100, 100], 3)
        civilian = CivilianDefender(self.controller, [175, 100], 3)
        opponent = CivilianAttacker(self.controller, [250, 100], 3)
        aura.update()
        civilian.attack()
        self.assertAlmostEqual(opponent.hp, 108)
        aura.die()
        civilian.attack()
        self.assertAlmostEqual(opponent.hp, 98)
