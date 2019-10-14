import pygame
from pygame.sprite import Sprite
import abc # Use the Abstract Base Classes module to implement inheritances of abstract classes

class CharacterModel(Sprite, metaclass=abc.ABCMeta):
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

    def getCoordinate(self):
        coord = int(self.position[0] / 100), int(self.position[1] / 100)
        return coord
        # 100 is used for spacefilling; the true value should be the length of a tile on the map
        # Returns a tuple for the coordinate of the character

class Defender(CharacterModel):
    '''
    The parent class for all the defenders in the game. Attributes and methods unique to defenders are defined in this class. This class also maintains a list of references of defender objects.
    '''
    defenders = []

    def __init__(self, position, direction):
        super().__init__(position, direction)
        Defender.defenders.append(self)
        # All defenders cannot move
        self.speed = 0
    
    @abc.abstractmethod
    def special(self):
        pass
    

class Attacker(CharacterModel):
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

    # All attackers may move
    def move(self):
        self.position[0] += CharacterModel.MOVEMENT[self.direction][0] * self.speed
        self.position[1] += CharacterModel.MOVEMENT[self.direction][1] * self.speed


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

class FattyDefender(Defender):
    '''
    Fatty defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 5
        self.attack_time = 2
        self.defend_power = 0
        self.hp = 400
        self.cost = 18
        self.cool_down_time = 25
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

class KamikazeDefender(Defender):
    '''
    Kamikaze defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 20
        self.attack_time = 1
        self.defend_power = 0
        self.hp = 40
        self.cost = 10
        self.cool_down_time = 10
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

class PharmacistDefender(Defender):
    '''
    Pharmacist defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 0
        self.attack_time = None
        self.defend_power = 0
        self.hp = 50
        self.cost = 25
        self.cool_down_time = 80
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

class AuraDefender(Defender):
    '''
    Aura defender class who provides buffs.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 0
        self.attack_time = None
        self.defend_power = 0
        self.hp = 90
        self.cost = 20
        self.cool_down_time = 60
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

class BombDefender(Defender):
    '''
    Bomb defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 0
        self.attack_time = None
        self.defend_power = 0
        self.hp = 200
        self.cost = 28
        self.cool_down_time = 120
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

class FattyAttacker(Attacker):
    '''
    Fatty defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 25
        self.attack_time = 4
        self.defend_power = 0
        self.hp = 400
        self.speed = 0.1
        self.cost = 18
        self.cool_down_time = 25
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

class KamikazeAttacker(Attacker):
    '''
    Kamikaze defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 50
        self.attack_time = 0.5
        self.defend_power = 0
        self.hp = 40
        self.speed = 0.4
        self.cost = 15
        self.cool_down_time = 10
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

class PharmacistAttacker(Attacker):
    '''
    Pharmacist defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 10
        self.attack_time = 1
        self.defend_power = 0
        self.hp = 150
        self.speed = 0.2
        self.cost = 25
        self.cool_down_time = 80
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

class AuraAttacker(Attacker):
    '''
    Aura defender class who provides buffs.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 30
        self.attack_time = 1.5
        self.defend_power = 0
        self.hp = 240
        self.speed = 0.25
        self.cost = 20
        self.cool_down_time = 30
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

class BombAttacker(Attacker):
    '''
    Bomb defender class.
    '''
    last_created_time = 0

    def __init__(self, position, direction):
        super().__init__(position, direction)
        self.attack_power = 0
        self.attack_time = 1
        self.defend_power = 0
        self.hp = 210
        self.speed = 0.2
        self.cost = 28
        self.cool_down_time = 90
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

class Bullet(Sprite):
    '''
    Class for bullets.
    '''
    def __init__(self, character):
        self.position = character.position
        self.direction = character.direction
        self.attack_power = character.attack_power
        self.speed = 4 # Spacefiller; actual speed depend on tile size
        self.init_image()

    def init_image(self):
        pass

    def update(self):
        pass

    def hit(self):
        pass