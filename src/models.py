import pygame
from pygame.sprite import Sprite
import abc # Use the Abstract Base Classes module to implement inheritances of abstract classes

class Model(Sprite, metaclass=abc.ABCMeta):
    '''
    The parent class for all the attackers and defenders in the game. Basic attributes and abstract methods are defined in this class.
    '''
    MOVEMENT = [
        (0, -1), # Up
        (-1, 0), # Left
        (0, 1),  # Down
        (1, 0),  # Right
    ]

    last_created_time = 0

    def __init__(self, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.init_image()
        self.type = ''
        self.attack_power = 0
        self.attack_time = 0
        self.defend_power = 0
        self.hp = 0
        self.speed = 0
        self.cost = 0
        self.cool_down_time = 0
        self.position = position
        self.direction = direction
    
    @abc.abstractmethod
    def init_image(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass
    
    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def attacked(self, loss):
        pass


class Defender(Model):
    '''
    The parent class for all the defenders in the game. Attributes and methods unique to defenders are defined in this class. This class also maintains a list of references of defender objects.
    '''
    defenders = []

    def __init__(self, position, direction):
        super().__init__(position, direction)
        Defender.defenders.append(self)
    
    @abc.abstractmethod
    def special(self):
        pass
    

class Attacker(Model):
    '''
    The parent class for all the attackers in the game. Attributes and methods unique to attackers are defined in this class. This class also maintains a list of references of attacker objects.
    '''
    attackers = []

    def __init__(self, position, direction):
        super().__init__(position, direction)
        Attacker.attackers.append(self)
    
    @abc.abstractmethod
    def die(self):
        pass


# The following are defenders.

class CivilianDefender(Defender):
    '''
    The civilian defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 10
        self.attack_time = 2
        self.defend_power = 0
        self.hp = 100
        self.speed = 0
        self.cost = 10
        self.cool_down_time = 15
        self.init_image()

    def init_image(self):
        # Prepare UI-related stuff. Should we draw it right in this method (or in next update)?
        pass
    
    def update(self):
        pass

    def attack(self):
        pass

    def special(self):
        pass

    def attacked(self, loss):
        pass

# The following are attackers.

class CivilianAttacker(Attacker):
    '''
    The civilian attacker class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 40
        self.attack_time = 1
        self.defend_power = 0
        self.hp = 120
        self.speed = 0.2
        self.cost = 10
        self.cool_down_time = 10
        self.init_image()
    
    def init_image(self):
        pass

    def update(self):
        self.move()
        pass

    def attack(self):
        pass
    
    def special(self):
        pass

    def attacked(self, loss):
        pass

    def move(self):
        self.position[0] += Model.MOVEMENT[self.direction][0] * self.speed
        self.position[1] += Model.MOVEMENT[self.direction][1] * self.speed