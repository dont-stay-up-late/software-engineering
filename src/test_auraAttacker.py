from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *

class TestAuraAttacker(TestCase):
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
        # Raise hp and attacking power of friends within reach model
        aura = AuraAttacker(self.controller, [100, 100], 0)
        civilian = CivilianAttacker(self.controller, [100, 175], 0)
        aura.update()
        self.assertAlmostEqual(civilian.hp, 1.2 * civilian.HP)
        self.assertAlmostEqual(civilian.attack_power, 3 * civilian.ATTACK_POWER)
        aura.update()
        self.assertAlmostEqual(civilian.hp, 1.2 * civilian.HP)
        self.assertAlmostEqual(civilian.attack_power, 3 * civilian.ATTACK_POWER)
        aura.die()
        self.assertAlmostEqual(civilian.hp, civilian.HP)
        self.assertAlmostEqual(civilian.attack_power, civilian.ATTACK_POWER)
