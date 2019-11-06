import numpy as np
import os
from src import models
from levelLoad import levelLoad

class GameController(object):

    # Constant names
    CHARA_NAMES = ['CivilianAttacker', 'FattyAttacker', 'KamikazeAttacker', 'PharmacistAttacker', 'AuraAttacker', 'BombAttacker',
                   'CivilianDefender', 'FattyDefender', 'KamikazeDefender', 'PharmacistDefender', 'AuraDefender', 'BombDefender']
    ITEM_NAMES = []

    # Game controller class. Contains some global variables.
    def __init__(self, level, map, mode = 'Single', player = 'Attack'):
        # Volume and display System
        self.volume = 30
        self.full_screen = False
        self.paused = False
        # Game time
        self.level_time_limit = map.time_limit
        self.FPS = 30
        self.frames_passed = 0
        # Game mode (single w/o network connection, or multiplayer w/ network connection)
        self.game_mode = mode
        self.player_side = player
        # Levels unlocked
        # ...
        # Dex
        self.initCharaDex()
        self.initItemDex()
        # Variables related to the game process
        self.level = level
        self.map = map
        self.money = {'Attack': 400, 'Defend': 400}
        self.money_restore_rate = {'Attack': 0.1, 'Defend': 0.1}
        self.fortress_HP = map.fortress_HP
        self.item_used_total_count = {'Attack': 0, 'Defend': 0}
        # Cooldown time for different kinds of characters; in turn, for civilian, fatty, kamikaze, pharmacist, aura and bomb characters
        self.cooldown_time = {'CivilianAttacker': 0, 'FattyAttacker': 0, 'KamikazeAttacker': 0, 'PharmacistAttacker': 0, 'AuraAttacker': 0, 'BombAttacker': 0,
                              'CivilianDefender': 0, 'FattyDefender': 0, 'KamikazeDefender': 0, 'PharmacistDefender': 0, 'AuraDefender': 0, 'BombDefender': 0}
        # Network related variables
        if self.game_mode == 'Network':
            # To be implemented
            pass

    def update(self):
        # Executed per frame
        self.frames_passed += 1
        for i in self.cooldown_time:
            if self.cooldown_time[i] > 0: self.cooldown_time[i] -= 1
        if self.game_mode == 'Single':
            self.money[self.player_side] += self.money_restore_rate
        else:
            self.money['Attack'] += self.money_restore_rate['Attack']
            self.money['Defend'] += self.money_restore_rate['Defend']
        if self.checkResult() is not None:
            # Game ends; show respective message
            # To be implemented in the UI module
            pass

    def attackerAdded(self, attacker):
        if self.attacker_money >= attacker.cost:
            self.attacker_money -= attacker.cost
            self.cooldown_time[attacker.type] = attacker.cool_down_time
            # Cool UI stuff - to be implemented in the UI module
        else:
            # Show a message that says not enough money
            # To be implemented in the UI module
            pass

    def defenderAdded(self, defender):
        if self.attacker_money >= defender.cost:
            self.defender_money -= defender.cost
            self.cooldown_time[defender.type] = defender.cool_down_time
            # Cool UI stuff - to be implemented in the UI module
        else:
            # Show a message that says not enough money
            # To be implemented in the UI module
            pass

    def reloadLevel(self, level):
        self.level = level
        self.map = levelLoad(self.level)

    def addCharacter(self, character):
        if isinstance(character, models.Attacker):
            models.Attacker.attackers.append(character)
            # ...
        elif isinstance(character, models.Defender):
            models.Defender.defenders.append(character)
            # ...

    def setVolume(self, vol):
        '''
        Set system volume; music and sound system to be implemented
        '''
        self.volume = vol

    def initCharaDex(self):
        '''
        Initialize character dex system
        '''
        if os.path.exists('chara_dex.npz'):
            exist_list = np.load('chara_dex.npz')
        else:
            exist_list = [True, False, False, False, False, False,
                          True, False, False, False, False, False]
            np.save('chara_dex.npz', exist_list)
        self.chara_dex_unlocked = dict(zip(GameController.CHARA_NAMES, exist_list))

    def initItemDex(self):
        '''
        Initialize character dex system
        '''
        if os.path.exists('item_dex.npz'):
            exist_list = np.load('item_dex.npz')
        else:
            exist_list = [True, False, False, False, False, False,
                          True, False, False, False, False, False]
            np.save('item_dex.npz', exist_list)
        self.item_dex_unlocked = dict(zip(GameController.ITEM_NAMES, exist_list))

    def characterSelectable(self, character):
        return self.cooldown_time[character] <= 0 and self.mo

    def gameTime(self):
        return self.frames_passed / self.FPS

    def checkResult(self):
        if self.gameTime() <= self.level_time_limit and self.fortress_HP > 0: return None
        elif self.fortress_HP <= 0: return 'Attack'
        else: return 'Defend'



