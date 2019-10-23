# Use the Abstract Base Classes module to implement inheritances of abstract classes
from abc import ABCMeta, ABC

import time
import pygame
from pygame.sprite import Sprite


class CharacterModel(Sprite, metaclass=ABCMeta):
    """
    The parent class for all the attackers and defenders in the game. Basic attributes and abstract methods are
    defined in this class.
    """
    MOVEMENT = [
        (0, -1),  # Up
        (-1, 0),  # Left
        (0, 1),  # Down
        (1, 0),  # Right
    ]

    last_created_time = 0
    HP = 0
    ATTACK_POWER = 0
    reach_model = None

    def __init__(self, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.init_image()
        self.type = ''
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 0
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0
        self.cost = 0
        self.cool_down_time = 0
        self.position = position
        self.direction = direction
<<<<<<< HEAD
        self.active = True
=======
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef

    def init_image(self):
        # TODO: to be implemented
        pass

    def update(self):
        # TODO: to be implemented
        pass

    def attack(self):
        if isinstance(self, Defender):
            # I'm a defender. I'll attack attackers.
            for attacker in Attacker.attackers:
                if CharacterModel.reachable(self, attacker):
                    attacker.attacked(self.attack_power, self)
        else:
            # I'm an attacker. I'll attack defenders.
            for defender in Defender.defenders:
                if CharacterModel.reachable(self, defender, self.reach_model):
                    defender.attacked(self.attack_power, self)

    def attacked(self, loss, attacker):
        self.hp -= loss
        if self.hp <= 0:
            self.die()

    def die(self):
<<<<<<< HEAD
        self.active = False
=======
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
        # TODO: to be implemented
        pass

    def special(self, character):
        """
        character: the object of special
        """
        pass

    def get_coordinate(self):
<<<<<<< HEAD
        coord = int(self.position[0] / 50), int(self.position[1] / 50)
=======
        coord = int(self.position[0] / 100), int(self.position[1] / 100)
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
        return coord
        # 100 is used for spacefilling; the true value should be the length of a tile on the map
        # Returns a tuple for the coordinate of the character

    @staticmethod
    def reachable(reaching_char, reached_char, reach_model):
        reach = []
        for delta_x, delta_y in reach_model:
            if reaching_char.direction == 0:
                # Up
                x = reaching_char.position[0] + delta_y
                y = reaching_char.position[1] - delta_x
            elif reaching_char.direction == 1:
                # Left
                x = reaching_char.position[0] - delta_x
                y = reaching_char.position[1] - delta_y
            elif reaching_char.direction == 2:
                # Down
                x = reaching_char.position[0] - delta_y
                y = reaching_char.position[1] + delta_x
            else:
                # Right
                x = reaching_char.position[0] + delta_x
                y = reaching_char.position[1] + delta_y
            reach.append((x, y))
        return reached_char in reach


class Defender(CharacterModel, ABC):
    """
    The parent class for all the defenders in the game. Attributes and methods unique to defenders are defined in
    this class. This class also maintains a list of references of defender objects.
    """
    defenders = []
    HP = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        Defender.defenders.append(self)
        # All defenders cannot move
        self.speed = 0


class Attacker(CharacterModel, ABC):
    """
    The parent class for all the attackers in the game. Attributes and methods unique to attackers are defined in
    this class. This class also maintains a list of references of attacker objects.
    """
    attackers = []
    HP = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        Attacker.attackers.append(self)

    # All attackers may move
    def move(self):
        self.position[0] += CharacterModel.MOVEMENT[self.direction][0] * self.speed
        self.position[1] += CharacterModel.MOVEMENT[self.direction][1] * self.speed


# The following are defenders.

class CivilianDefender(Defender):
    """
    The civilian defender class.
    """
    last_created_time = 0
    HP = 100
    ATTACK_POWER = 10
    reach_model = [(-1, 0), (-1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'CivilianDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 2
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 10
        self.cool_down_time = 15
        self.init_image()


class FattyDefender(Defender):
    """
    Fatty defender class.
    """
    last_created_time = 0
    HP = 400
    ATTACK_POWER = 5
    reach_model = []

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'FattyDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 2
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 18
        self.cool_down_time = 25
        self.init_image()


class KamikazeDefender(Defender):
    """
    Kamikaze defender class.
    """
    last_created_time = 0
    HP = 40
    ATTACK_POWER = 20
    reach_model = [(0, 1), (0, 2)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'KamikazeDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 10
        self.cool_down_time = 10
        self.init_image()


class PharmacistDefender(Defender):
    """
    Pharmacist defender class.
    """
    last_created_time = 0
    SPECIAL_INTERVAL = 120
    HP = 50
    ATTACK_POWER = 0
    reach_model = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'PharmacistDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = None
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 25
        self.cool_down_time = 80
        self.last_special_time = 0
        self.init_image()

    def update(self):
        if time.time() - self.last_special_time >= self.SPECIAL_INTERVAL:
            for defender in Defender.defenders:
<<<<<<< HEAD
                if CharacterModel.reachable(self, defender, self.reach_model) and defender.active:
=======
                if CharacterModel.reachable(self, defender, self.reach_model):
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
                    self.special(defender)
        super().update()

    def attacked(self, loss, attacker):
        super().attacked(loss, attacker)

    def special(self, character):
        if character.hp <= 0:
            character.hp = character.HP
            self.last_special_time = time.time()


class AuraDefender(Defender):
    """
    Aura defender class who provides buffs.
    """
    last_created_time = 0
    HP = 90
    ATTACK_POWER = 0
    reach_model = [(-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -1), (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (1, 2)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'AuraDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = None
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 20
        self.cool_down_time = 60
        self.init_image()

    def update(self):
        for defender in Defender.defenders:
            if CharacterModel.reachable(self, defender, self.reach_model):
                self.activate_special(defender)
        super().update()

    @staticmethod
    def activate_special(character):
        character.attack_power = 1.2 * character.ATTACK_POWER
        character.hp = 1.2 * character.HP

    def die(self):
        for defender in Defender.defenders:
            if CharacterModel.reachable(self, defender, self.reach_model):
                self.deactivate_special(defender)
        super().die()

    @staticmethod
    def deactivate_special(character):
        character.attack_power = character.ATTACK_POWER
        character.hp = character.HP


class BombDefender(Defender):
    """
    Bomb defender class.
    """
    last_created_time = 0
    SPECIAL_INTERVAL = 1.5  # seconds
    HP = 200
    ATTACK_POWER = 0
    reach_model = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'BombDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = None
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 28
        self.cool_down_time = 120
        self.created_time = time.time()
        self.init_image()

    def update(self):
        if time.time() - self.created_time >= self.SPECIAL_INTERVAL:
            # Iterate through neighbors and apply special
            for attacker in Attacker.attackers:
<<<<<<< HEAD
                if CharacterModel.reachable(self, attacker, self.reach_model) and attacker.active:
=======
                if CharacterModel.reachable(self, attacker, self.reach_model):
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
                    self.special(attacker)
            self.die()
        super().update()

    def die(self):
        for attacker in Attacker.attackers:
            if CharacterModel.reachable(self, attacker, self.reach_model):
                self.special(attacker)
        super().die()

    def special(self, character):
        character.attacked(self.hp, self)


# The following are attackers.

class CivilianAttacker(Attacker):
    """
    The civilian attacker class.
    """
    last_created_time = 0
    HP = 120
    ATTACK_POWER = 40
    reach_model = []

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'CivilianAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.2
        self.cost = 10
        self.cool_down_time = 10
        self.init_image()


class FattyAttacker(Attacker):
    """
<<<<<<< HEAD
    Fatty attacker class.
=======
    Fatty defender class.
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
    """
    last_created_time = 0
    HP = 400
    ATTACK_POWER = 25
    reach_model = []

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'FattyAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 4
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.1
        self.cost = 18
        self.cool_down_time = 25
        self.init_image()


class KamikazeAttacker(Attacker):
    """
<<<<<<< HEAD
    Kamikaze attacker class.
=======
    Kamikaze defender class.
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
    """
    last_created_time = 0
    HP = 40
    ATTACK_POWER = 50
    reach_model = [(0, 1)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'KamikazeAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 0.5
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.4
        self.cost = 15
        self.cool_down_time = 10
        self.init_image()


class PharmacistAttacker(Attacker):
    """
<<<<<<< HEAD
    Pharmacist attacker class.
=======
    Pharmacist defender class.
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
    """
    last_created_time = 0
    SPECIAL_INTERVAL = 60
    HP = 150
    ATTACK_POWER = 10
    reach_model = [(0, 1)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'PharmacistAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.2
        self.cost = 25
        self.cool_down_time = 80
        self.last_special_time = 0
        self.init_image()

    def attacked(self, loss, attacker):
        if self.last_special_time - time.time() >= self.SPECIAL_INTERVAL:
            # Kill attacker
            self.special(attacker)
            self.last_special_time = time.time()
        super().attacked(loss, attacker)

    def special(self, character):
        character.die()


class AuraAttacker(Attacker):
    """
<<<<<<< HEAD
    Aura attacker class who provides buffs.
=======
    Aura defender class who provides buffs.
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
    """
    last_created_time = 0
    HP = 240
    ATTACK_POWER = 30
    reach_model = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'AuraAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1.5
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.25
        self.cost = 20
        self.cool_down_time = 30
        self.init_image()

    def update(self):
        for attacker in Attacker.attackers:
            if CharacterModel.reachable(self, attacker, self.reach_model):
                self.activate_special(attacker)
        super().update()

    @staticmethod
    def activate_special(character):
        character.attack_power = 3 * character.ATTACK_POWER
        character.hp = 1.2 * character.HP

    def die(self):
        for attacker in Attacker.attackers:
            if CharacterModel.reachable(self, attacker, self.reach_model):
                self.deactivate_special(attacker)
        super().die()

    @staticmethod
    def deactivate_special(character):
        character.attack_power = character.ATTACK_POWER
        character.hp = character.HP


class BombAttacker(Attacker):
    """
<<<<<<< HEAD
    Bomb attacker class.
=======
    Bomb defender class.
>>>>>>> b7269823259783ebb7d02474680074aefb0edbef
    """
    last_created_time = 0
    HP = 210
    ATTACK_POWER = 0
    SPECIAL_ATTACK_POWER = 380
    reach_model = [(1, 0)]
    special_reach_model = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.type = 'BombAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.2
        self.cost = 28
        self.cool_down_time = 90
        self.init_image()

    def special(self, character):
        character.attacked(self.SPECIAL_ATTACK_POWER, self)

    def die(self):
        # Exert special attack to its 4-neighbors
        for defender in Defender.defenders:
            if CharacterModel.reachable(self, defender, self.special_reach_model):
                self.special(defender)
        super().die()


# Do we still need this class?
class Bullet(Sprite):
    """
    Class for bullets.
    """

    def __init__(self, character, reach_model, bullet_image, effect_type):
        super().__init__()
        self.position = character.position
        self.direction = character.direction
        self.attack_power = character.attack_power
        self.reach_model = reach_model
        self.bullet_image = bullet_image  # This can actually be a quite complex data structure... I'm not sure how
        # this should be structured but it should definitely be confirmed by the time the UI team writes the
        # init_image() method :)
        self.effect_type = effect_type  # For pharmacists, it increases hp of the same side.
        self.speed = 4  # Spacefiller; actual speed depend on tile size
        self.init_image()

    def init_image(self):
        pass

    def update(self):
        pass

    def hit(self):
        pass
