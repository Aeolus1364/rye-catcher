import pygame

pygame.init()

DISPLAY_X = 800
DISPLAY_Y = 600
FPS = 30

surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
clock = pygame.time.Clock()


class Main:
    def __init__(self):
        self.game_exit = False

    def game_loop(self):
        while not self.game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: