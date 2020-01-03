from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *

class TestPharmacistDefender(TestCase):
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
        # When friends' hp within reach model is 0 or negative, a pharmacist recovers it to it's full HP.
        pharmacist = PharmacistDefender(self.controller, [100, 100], 0)
        kamikaze = KamikazeDefender(self.controller, [100, 175], 0)
        aura_attacker = AuraAttacker(self.controller, [100, 250], 0)
        aura_attacker.speed = 0
        for _ in range(10000):
            aura_attacker.attack()
        self.assertEqual(kamikaze.hp, -2440)
        pharmacist.last_special_time = 0
        pharmacist.update()
        self.assertEqual(kamikaze.hp, 60)
        