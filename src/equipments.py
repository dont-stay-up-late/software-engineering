from pygame.sprite import Sprite
import pygame
from abc import ABCMeta
from threading import Timer
from random import choices
import models



class Equipment(Sprite, metaclass=ABCMeta):
    pass


class DefenderEquipment(Equipment, metaclass=ABCMeta):
    pass


class AttackerEquipment(Equipment, metaclass=ABCMeta):
    pass


class AmbulanceEquipment(DefenderEquipment):
    def __init__(self, defender, game_controller):
        super().__init__()
        game_controller.money['Defend'] += defender.cost // 2
        defender.die()


class GlueEquipment(DefenderEquipment):
    def __init__(self, track, game_controller):
        super().__init__()
        track.disable()
        timer = Timer(20, track.enable)
        timer.start()


class CanonEquipment(DefenderEquipment):
    def __init__(self, game_controller):
        chosen = choices(models.Attacker.attackers, k=2)
        for attacker in chosen:
            attacker.attacked(110, None)


class IndifferentEquipment(AttackerEquipment):
    def __init__(self, game_controller):
        for attacker in models.Attacker.attackers:
            attacker.attacked(40, None)
        for defender in models.Defender.defenders:
            defender.attacked(40, None)


class DopingEquipment(AttackerEquipment):
    doped = set()
    def __init__(self, game_controller):
        for attacker in models.Attacker.attackers:
            if attacker not in self.doped:
                attacker.speed = int(attacker.speed * 1.25)
                self.doped.add(attacker)


class SignalEquipment(AttackerEquipment):
    @staticmethod
    def hide_mouse():
        pygame.mouse.set_visible(True)

    @staticmethod
    def show_mouse():
        pygame.mouse.set_visible(False)

    def __init__(self, game_controller):
        self.hide_mouse()
        timer = Timer(5, self.show_mouse)
        timer.start()
