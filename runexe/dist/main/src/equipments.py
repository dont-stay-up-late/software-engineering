from pygame.sprite import Sprite
import pygame
from abc import ABCMeta
from threading import Timer
from random import choices
from src.models import *
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


class ListEquipment(DefenderEquipment):
    count = 1
    def __init__(self, game_controller, last_cds):
        super().__init__()
        ListEquipment.count -= 1
        if time.time() - CivilianDefender.last_created_time < 15:
            CivilianDefender.last_created_time += 5
        if time.time() - FattyDefender.last_created_time < 60:
            FattyDefender.last_created_time += 5
        if time.time() - KamikazeDefender.last_created_time < 10:
            KamikazeDefender.last_created_time += 5
        if time.time() - PharmacistDefender.last_created_time < 25:
            PharmacistDefender.last_created_time += 5
        if time.time() - AuraDefender.last_created_time < 80:
            AuraDefender.last_created_time += 5
        for i in range(len(last_cds)):
            last_cds[i] -= 5000


class CanonEquipment(DefenderEquipment):
    count = 1
    def __init__(self, game_controller):
        super().__init__()
        CanonEquipment.count -= 1
        chosen = choices(Attacker.attackers, k=2)
        for attacker in chosen:
            attacker.attacked(2000, EquipmentAttacker())


class IndifferentEquipment(AttackerEquipment):
    count = 1
    def __init__(self, game_controller):
        super().__init__()
        IndifferentEquipment.count -= 1
        for attacker in Attacker.attackers:
            attacker.attacked(800, EquipmentAttacker())
        for defender in Defender.defenders:
            defender.attacked(800, EquipmentAttacker())


class DopingEquipment(AttackerEquipment):
    count = 1
    doped = set()
    def __init__(self, game_controller):
        super().__init__()
        DopingEquipment.count -= 1
        for attacker in Attacker.attackers:
            if attacker not in self.doped:
                attacker.speed = attacker.speed * 1.25
                DopingEquipment.doped.add(attacker)


class SignalEquipment(AttackerEquipment):
    count = 1

    on = False

    @staticmethod
    def turn_off():
        SignalEquipment.on = False

    def __init__(self, game_controller):
        super().__init__()
        SignalEquipment.count -= 1
        SignalEquipment.on = True
        timer = Timer(5, SignalEquipment.turn_off)
        timer.start()
