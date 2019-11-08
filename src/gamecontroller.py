import numpy as np
import os
from src import models
from levelLoad import levelLoad

class GameController(object):

    '''
    Game state codes. Written according to the use case diagram.
    May be modified or deleted in future versions.
    '''
    START_GAME_STATE = 1
    DEX_STATE = 2
    GAME_HELP_STATE = 3
    GAME_SETTINGS_STATE = 4
    EXIT_STATE = 5
    GAME_MODE_SELECT_STATE = 6
    SINGLE_MODE_PREPARE_STATE = 7
    MULTI_MODE_PREPARE_STATE = 8
    GAME_END_STATE = 10
    DEFENDER_SET_STATE = 11
    ATTACKER_SET_STATE = 12
    TRAIL_CHANGE_STATE = 13
    CHARA_SPECIAL_STATE = 14
    ITEM_USE_STATE = 15
    ATTACK_HIT_STATE = 16
    '''
    Constant names
    '''
    CHARA_NAMES = ['CivilianAttacker', 'FattyAttacker', 'KamikazeAttacker', 'PharmacistAttacker', 'AuraAttacker', 'BombAttacker',
                   'CivilianDefender', 'FattyDefender', 'KamikazeDefender', 'PharmacistDefender', 'AuraDefender', 'BombDefender']
    ITEM_NAMES = []

    '''
    Game controller class. Contains some global variables.
    '''
    def __init__(self, level, map):
        # Volume and display System
        self.volume = 30
        self.full_screen = False
        # Game mode (single w/o network connection, or multiplayer w/ network connection)
        self.game_mode = 'Single'
        self.player_side = 'Attack'
        # Dex
        self.chara_dex_unlocked = {}
        self.item_dex_unlocked = {}
        # Variables related to the game process
        self.level = level
        self.map = map
        self.attacker_money = 400
        self.defender_money = 400
        # Cooldown time for different kinds of characters; in turn, for civilian, fatty, kamikaze, pharmacist, aura and bomb characters
        self.cooldown_time = {'CivilianAttacker': 0, 'FattyAttacker': 0, 'KamikazeAttacker': 0, 'PharmacistAttacker': 0, 'AuraAttacker': 0, 'BombAttacker': 0,
                              'CivilianDefender': 0, 'FattyDefender': 0, 'KamikazeDefender': 0, 'PharmacistDefender': 0, 'AuraDefender': 0, 'BombDefender': 0}

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
