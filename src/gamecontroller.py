from levelLoad import levelLoad

class GameController(object):
    '''
    Game controller class. Contains some global variables.
    '''
    def __init__(self, level, map):
        self.level = level
        self.map = levelLoad(self.level)
        self.attacker_money = 400
        self.defender_money = 400
        # Cooldown time for different kinds of characters; in turn, for civilian, fatty, kamikaze, pharmacist, aura and bomb characters
        self.attacker_cooldown_time = [0, 0, 0, 0, 0, 0]
        self.defender_cooldown_time = [0, 0, 0, 0, 0, 0]

    def attackerSelected(self, attacker):
        self.attacker_money -= attacker.cost
        self.defender

    def defenderSelected(self, defender):
        self.defender_money -= defender.cost

    def

    def reloadLevel(self, level):
        self.level = level
        self.map = levelLoad(self.level)