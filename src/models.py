# Use the Abstract Base Classes module to implement inheritances of abstract classes
from abc import ABCMeta, ABC

import time
import pygame
from pygame.sprite import Sprite

from path import path

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
    filename = ''

    def __init__(self, controller, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.init_image(self.filename, 50, 50, 1)
        self.controller = controller
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
        self.active = True
        self.attacked_flag = False
        self.attacking_flag = False
        self.last_created_time = time.time()

    def init_image(self, filename, width, height, columns):
        # https://www.cnblogs.com/msxh/p/5013555.html
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = 0, 0, width, height
        self.columns = columns
        self.rate = self.controller.FPS / 2
        rect = self.master_image.get_rect()
        self.first_frame = 0
        self.last_frame = (rect.width // width) * (rect.height // height) - 1
        self.old_frame = -1
        self.frame = 0
        self.last_time = self.controller.frames_passed

    def update(self):
        # https://www.cnblogs.com/msxh/p/5013555.html
        if self.attacking_flag:
            pass
        elif self.attacked_flag:
            if self.direction == 0:
                # self.init_image(self, ATTACKED_IMAGE_0, width, height, columns)
                pass
            elif self.direction == 1:
                # self.init_image(self, ATTACKED_IMAGE_1, width, height, columns)
                pass
            elif self.direction == 2:
                # self.init_image(self, ATTACKED_IMAGE_2, width, height, columns)
                pass
            else:
                # self.init_image(self, ATTACKED_IMAGE_3, width, height, columns)
                pass
        else:
            if self.direction == 0:
                # self.init_image(self, WALK_IMAGE_0, width, height, columns)
                pass
            elif self.direction == 1:
                # self.init_image(self, WALK_IMAGE_1, width, height, columns)
                pass
            elif self.direction == 2:
                # self.init_image(self, WALK_IMAGE_2, width, height, columns)
                pass
            else:
                # self.init_image(self, WALK_IMAGE_3, width, height, columns)
                pass
        # self.attacked_flag = False
        # self.attacking_flag = False

        # Animation Effect
        if self.controller.frames_passed > self.last_time + self.rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = self.controller.frames_passed
        # if self.frame != self.old_frame:
        #     frame_x = (self.frame % self.columns) * self.frame_width
        #     frame_y = (self.frame // self.columns) * self.frame_height
        #     rect = (frame_x, frame_y, self.frame_width, self.frame_height)
        #     self.image = self.master_image.subsurface(rect)
        #     self.old_frame = self.frame

    def attack(self):
        #if self.controller.frames_passed % 10 != 0:
        #    return
        if isinstance(self, Defender):
            # I'm a defender. I'll attack attackers.
            attacking_num = 0
            for attacker in Attacker.attackers:
                if CharacterModel.reachable(self, attacker, self.reach_model):
                    attacker.attacked(self.attack_power, self)
                    self.attacking_flag = True
                    attacking_num += 1
            if attacking_num == 0:
                self.attacking_flag = False

        else:
            # I'm an attacker. I'll attack defenders.
            attacking_num = 0
            for defender in Defender.defenders:
                if CharacterModel.reachable(self, defender, self.reach_model):
                    defender.attacked(self.attack_power, self)
                    self.attacking_flag = True
                    attacking_num += 1
            if attacking_num == 0:
                self.attacking_flag = False

    def attacked(self, loss, attacker):
        self.attacked_flag = True
        self.hp -= loss * 0.1

    def die(self):
        self.active = False
        # All targets in range are no longer attacked
        if isinstance(self, Defender):
            for attacker in Attacker.attackers:
                if CharacterModel.reachable(self, attacker, self.reach_model):
                    attacker.attacked_flag = False
                    attacker.attacking_flag = False
        else:
            for defender in Defender.defenders:
                if CharacterModel.reachable(self, defender, self.reach_model):
                    defender.attacked_flag = False
                    defender.attacking_flag = False
        if isinstance(self, Attacker):
            # Money reward for defender
            # Currently the amount is set to half of the cost of the character itself. This could be adjusted.
            self.controller.money['Defend'] += self.cost // 2
        else:
            # Money reward for attacker
            # Currently the amount is set to half of the cost of the character itself. This could be adjusted.
            self.controller.money['Attack'] += self.cost // 2
        self.kill()

    def special(self, character):
        """
        character: the object of special
        """
        pass

    def get_coordinate(self):
        # Returns a tuple for the coordinate of the character
        coord = (self.position[0] - 265) // 75, (self.position[0] - 70) // 75
        return coord

    @staticmethod
    def reachable(reaching_char, reached_char, reach_model):
        reach = []
        for delta_x, delta_y in reach_model:
            if reaching_char.direction == 0:
                # Up
                x = (reaching_char.position[0] - 265) // 75 - delta_x
                y = (reaching_char.position[1] - 70) // 75 - delta_y
            elif reaching_char.direction == 1:
                # Left
                x = (reaching_char.position[0] - 265) // 75 - delta_y
                y = (reaching_char.position[1] - 70) // 75 + delta_x
            elif reaching_char.direction == 2:
                # Down
                x = (reaching_char.position[0] - 265) // 75 + delta_x
                y = (reaching_char.position[1] - 70) // 75 + delta_y
            else:
                # Right
                x = (reaching_char.position[0] - 265) // 75 + delta_y
                y = (reaching_char.position[1] - 70) // 75 - delta_x
            reach.append((x, y))
        x = (reached_char.position[0] - 265) // 75
        y = (reached_char.position[1] - 70) // 75
        return (x, y) in reach


class Defender(CharacterModel, ABC):
    """
    The parent class for all the defenders in the game. Attributes and methods unique to defenders are defined in
    this class. This class also maintains a list of references of defender objects.
    """
    defenders = []
    HP = 0

    def __init__(self, controller, position, direction):
        super().__init__(controller, position, direction)
        Defender.defenders.append(self)
        # All defenders cannot move
        self.speed = 0

    def die(self):
        Defender.defenders.remove(self)
        super().die()


class Attacker(CharacterModel, ABC):
    """
    The parent class for all the attackers in the game. Attributes and methods unique to attackers are defined in
    this class. This class also maintains a list of references of attacker objects.
    """
    attackers = []
    HP = 0
    speed_rate = 5

    def __init__(self, controller, position, direction):
        super().__init__(controller, position, direction)
        Attacker.attackers.append(self)

    # All attackers may move
    def move(self):
        self.position[0] += CharacterModel.MOVEMENT[self.direction][0] * self.speed * self.speed_rate
        self.position[1] += CharacterModel.MOVEMENT[self.direction][1] * self.speed * self.speed_rate

    def die(self):
        Attacker.attackers.remove(self)
        super().die()


# The following are defenders.

class CivilianDefender(Defender):
    """
    The civilian defender class.
    """
    last_created_time = 0
    HP = 100
    ATTACK_POWER = 10
    reach_model = [(-1, 0), (-1, 1), (0, 1), (0, 2), (0, 3), (0, 0), (1, 0), (1, 1)]
    filename = path('res/character/pingminb0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'CivilianDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 2
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 10
        self.cool_down_time = 15
        self.init_image(self.filename, 75, 75, 1)


class FattyDefender(Defender):
    """
    Fatty defender class.
    """
    last_created_time = 0
    HP = 400
    ATTACK_POWER = 5
    reach_model = [(0, 0)]
    filename = path('res/character/pangdunb0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'FattyDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 2
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 18
        self.cool_down_time = 25
        self.init_image(self.filename, 75, 75, 1)


class KamikazeDefender(Defender):
    """
    Kamikaze defender class.
    """
    last_created_time = 0
    HP = 40
    ATTACK_POWER = 10
    reach_model = [(0, 1), (0, 0),(0, 2)]
    filename = path('res/character/gansiduib0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'KamikazeDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 10
        self.cool_down_time = 10
        self.init_image(self.filename, 75, 75, 1)


class PharmacistDefender(Defender):
    """
    Pharmacist defender class.
    """
    last_created_time = 0
    SPECIAL_INTERVAL = 120
    HP = 50
    ATTACK_POWER = 5
    reach_model = [(-1, -1), (-1, 0), (-1, 1), (0, 0), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    filename = path('res//character/yaojishib0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'PharmacistDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = None
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 25
        self.cool_down_time = 80
        self.last_special_time = 0
        self.init_image(self.filename, 75, 75, 1)

    def update(self):
        if time.time() - self.last_special_time >= self.SPECIAL_INTERVAL:
            for defender in Defender.defenders:
                if CharacterModel.reachable(self, defender, self.reach_model) and defender.active:
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
    ATTACK_POWER = 10
    reach_model = [(-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, 0), (0, -1), (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (1, 2)]
    filename = path('res/character/gongtoub0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'AuraDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = None
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 20
        self.cool_down_time = 60
        self.init_image(self.filename, 75, 75, 1)

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
    ATTACK_POWER = 10
    reach_model = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    filename = path('res/mapnum/Mapnum1_0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'BombDefender'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = None
        self.defend_power = 0
        self.hp = self.HP
        self.cost = 28
        self.cool_down_time = 120
        self.created_time = time.time()
        self.init_image(self.filename, 75, 75, 1)

    def update(self):
        if time.time() - self.created_time >= self.SPECIAL_INTERVAL:
            self.die()
        super().update()

    def die(self):
        for attacker in Attacker.attackers:
            if CharacterModel.reachable(self, attacker, self.reach_model) and attacker.active:
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
    HP = 100
    ATTACK_POWER = 10
    reach_model = [(0, 0), (0, 1)]
    filename = path('res/character/pingminr0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'CivilianAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.2
        self.cost = 10
        self.cool_down_time = 10
        self.init_image(self.filename, 75, 75, 1)


class FattyAttacker(Attacker):
    """
    Fatty attacker class.
    """
    last_created_time = 0
    HP = 400
    ATTACK_POWER = 20
    reach_model = [(0, 0), (0, 1)]
    filename = path('res/character/pangdunr0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'FattyAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 4
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.1
        self.cost = 18
        self.cool_down_time = 25
        self.init_image(self.filename, 75, 75, 1)


class KamikazeAttacker(Attacker):
    """
    Kamikaze attacker class.
    """
    last_created_time = 0
    HP = 40
    ATTACK_POWER = 5
    reach_model = [(0, 1), (0, 0), (0, 2)]
    filename = path('res/character/gansiduir0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'KamikazeAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 0.5
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.4
        self.cost = 15
        self.cool_down_time = 10
        self.init_image(self.filename, 75, 75, 1)


class PharmacistAttacker(Attacker):
    """
    Pharmacist attacker class.
    """
    last_created_time = 0
    SPECIAL_INTERVAL = 60
    HP = 150
    ATTACK_POWER = 10
    reach_model = [(0, 1), (0, 0), (0, 2)]
    filename = path('res/character/yaojishir0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'PharmacistAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.2
        self.cost = 25
        self.cool_down_time = 80
        self.last_special_time = 0
        self.init_image(self.filename, 75, 75, 1)

    def attacked(self, loss, attacker):
        if time.time() - self.last_special_time >= self.SPECIAL_INTERVAL:
            # Kill attacker
            self.special(attacker)
            self.last_special_time = time.time()
        super().attacked(loss, attacker)

    def special(self, character):
        character.die()


class AuraAttacker(Attacker):
    """
    Aura attacker class who provides buffs.
    """
    last_created_time = 0
    HP = 240
    ATTACK_POWER = 30
    reach_model = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
    filename = path('res/character/gongtour0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'AuraAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1.5
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.25
        self.cost = 20
        self.cool_down_time = 30
        self.init_image(self.filename, 75, 75, 1)

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
    Bomb attacker class.
    """
    last_created_time = 0
    HP = 210
    ATTACK_POWER = 10
    SPECIAL_ATTACK_POWER = 380
    reach_model = [(0, 0), (0, 1), (0, 2)]
    special_reach_model = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
    filename = path('res/mapnum/Mapnum1_0.png')

    def __init__(self, controller, position, direction):
        self.controller = controller
        super().__init__(controller, position, direction)
        self.type = 'BombAttacker'
        self.attack_power = self.ATTACK_POWER
        self.attack_time = 1
        self.defend_power = 0
        self.hp = self.HP
        self.speed = 0.2
        self.cost = 28
        self.cool_down_time = 90
        self.init_image(self.filename, 75, 75, 1)

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
