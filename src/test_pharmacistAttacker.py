from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *

class TestPharmacistAttacker(TestCase):
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
        pharmacist = PharmacistAttacker(self.controller, [100, 100], 3)
        opponent = KamikazeDefender(self.controller, [100, 175], 1)
        opponent.attack()
        self.assertNotIn(opponent, Defender.defenders)
