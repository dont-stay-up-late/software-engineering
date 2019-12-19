from pygame.sprite import Sprite
import pygame
from abc import ABCMeta
from threading import Timer
from random import choices
import models
import time



class Equipment(Sprite, metaclass=ABCMeta):
    pass


class DefenderEquipment(Equipment, metaclass=ABCMeta):
    pass


class AttackerEquipment(Equipment, metaclass=ABCMeta):
    pass


class AmbulanceEquipment(DefenderEquipment):
    count = 1
    def __init__(self, defender, game_controller):
        super().__init__()
        game_controller.money['Defend'] += defender.cost // 2
        defender.die()


class ListEquipment(DefenderEquipment):
    count = 1
    def __init__(self, track, game_controller):
        super().__init__()
        ListEquipment.count -= 1
        if time.time() - CivilianDefender.last_created_time > 15:
            CivilianDefender.last_created_time += 5
        if time.time() - FattyDefender.last_created_time > 60:
            FattyDefender.last_created_time += 5
        if time.time() - KamikazeDefender.last_created_time > 10:
            KamikazeDefender.last_created_time += 5
        if time.time() - PharmacistDefender.last_created_time > 25:
            PharmacistDefender.last_created_time += 5
        if time.time() - AuraDefender.last_created_time > 80:
            AuraDefender.last_created_time += 5


class CanonEquipment(DefenderEquipment):
    count = 1
    def __init__(self, game_controller):
        super().__init__()
        CanonEquipment.count -= 1
        chosen = choices(models.Attacker.attackers, k=2)
        for attacker in chosen:
            attacker.attacked(110, None)


class IndifferentEquipment(AttackerEquipment):
    count = 1
    def __init__(self, game_controller):
        super().__init__()
        IndifferentEquipment.count -= 1
        for attacker in models.Attacker.attackers:
            attacker.attacked(40, None)
        for defender in models.Defender.defenders:
            defender.attacked(40, None)


class DopingEquipment(AttackerEquipment):
    count = 1
    doped = set()
    def __init__(self, game_controller):
        super().__init__()
        DopingEquipment.count -= 1
        for attacker in models.Attacker.attackers:
            if attacker not in self.doped:
                attacker.speed = int(attacker.speed * 1.25)
                DopingEquipment.doped.add(attacker)


# TODO: This equipment needs modification since there is no multi player mode now.
class SignalEquipment(AttackerEquipment):
    count = 1

    @staticmethod
    def hide_mouse():
        pygame.mouse.set_visible(True)

    @staticmethod
    def show_mouse():
        pygame.mouse.set_visible(False)

    def __init__(self, game_controller):
        super().__init__()
        SignalEquipment.count -= 1
        self.hide_mouse()
        timer = Timer(5, self.show_mouse)
        timer.start()
