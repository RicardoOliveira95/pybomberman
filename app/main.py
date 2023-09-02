import pygame

from sprites import Player, Wall
from event import AddEnemy
from engine import Engine
from sprites import Boar, Bird
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    DEFAULT_OBJ_SIZE,
    FRAMES_PER_SECOND,
    BACKGROUND_COLOR
)
import random


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

engine = Engine(screen=screen, clock=clock)

player = Player()

Wall.generate_walls((SCREEN_WIDTH, SCREEN_HEIGHT),
                    (DEFAULT_OBJ_SIZE, DEFAULT_OBJ_SIZE))

add_enemy = AddEnemy(1000)
engine.add_event(add_enemy)

engine.running = True

while engine.running:
    
    engine.events_handling()

    # Update all groups
    engine.groups_update()

    engine.screen.fill(BACKGROUND_COLOR)

    # Draw all sprites
    engine.draw_all_sprites()

    engine.draw_interface()

    # Check if the player's health reaches zero
    player = engine.groups["player"].sprites()[0]
    if player.get_health() <= 0:
        # Player has died, display game over screen
        engine.screen.fill((0, 0, 0))  # Fill the screen with black
        font = pygame.font.SysFont("comicsans", 50, True)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        engine.screen.blit(text, text_rect)
        pygame.display.flip()

        # Exit the game loop when player dies
        engine.running = False

    # Create instances of Boar and Bird and add them to sprite groups
    if random.random() < 0.001:  # Adjust the probability as needed
        boar = Boar()
        engine.add_to_group(boar, "enemies")
        engine.add_to_group(boar, "flammable")

    if random.random() < 0.01:  # Adjust the probability as needed
        bird = Bird()
        engine.add_to_group(bird, "enemies")
        engine.add_to_group(bird, "flammable")

    pygame.display.flip()
    engine.clock.tick(FRAMES_PER_SECOND)

# Game over screen loop (optional)
while not engine.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
