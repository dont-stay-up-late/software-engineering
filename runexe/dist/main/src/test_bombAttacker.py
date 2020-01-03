from unittest import TestCase

from src.gamecontroller import GameController
from src.levelLoad import levelLoad
from src.models import *

class TestBombAttacker(TestCase):
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
        # Special attack upon death
        bomb = BombAttacker(self.controller, [100, 100], 0)
        opponent = KamikazeDefender(self.controller, [100, 175], 1)
        for _ in range(11):
            opponent.attack()
        if bomb.hp <= 0:
            bomb.die()
        self.assertAlmostEqual(opponent.hp, 60)
