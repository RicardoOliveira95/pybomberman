import random, pygame

class Effect:
    def __init__(self):
        self.image = pygame.image.load("images/fast_effect.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.position = (0, 0)
        self.active = False  # Set to True when picked up by player

    def apply_effect(self, player):
        pass  # Implement effect logic in subclasses

    def update(self):
        pass  # Implement any animation or movement here

class HealEffect(Effect):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/healing_effect.png").convert_alpha()

    def apply_effect(self, player):
        player.change_health(20)

class SlowEffect(Effect):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/slow_effect.png").convert_alpha()

    def apply_effect(self, player):
        player.change_speed(-2)

class AccelerateEffect(Effect):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/accelerate_effect.png").convert_alpha()

    def apply_effect(self, player):
        player.change_speed(2)
