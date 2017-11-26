import pygame
import entity
import player
import collide

pygame.init()

DISPLAY_X = 1280
DISPLAY_Y = 800
FPS = 30

surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y), pygame.FULLSCREEN)
clock = pygame.time.Clock()

slime = pygame.image.load("spritesheet_large.png")


class Main:
    def __init__(self):
        self.running = True

        self.player = player.Player(surface, (0, 0, 22, 40), slime)
        self.player2 = player.Player(surface, (100, 100, 22, 40), slime)

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.x_velocity += -5
                    if event.key == pygame.K_RIGHT:
                        self.player.x_velocity += 5
                    if event.key == pygame.K_UP:
                        self.player.y_velocity += -5
                    if event.key == pygame.K_DOWN:
                        self.player.y_velocity += 5
                    if event.key == pygame.K_w:
                        self.running = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.x_velocity -= -5
                    if event.key == pygame.K_RIGHT:
                        self.player.x_velocity -= 5
                    if event.key == pygame.K_UP:
                        self.player.y_velocity -= -5
                    if event.key == pygame.K_DOWN:
                        self.player.y_velocity -= 5

            surface.fill((255, 255, 255))


            self.player.update()
            self.player2.update()

            collide.collision_system(self.player, self.player2)

            self.player.render()
            self.player2.render()

            pygame.display.update()
            clock.tick(FPS)


Main().game_loop()

