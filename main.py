import pygame
import entity
import player
import collide
import time


pygame.init()

DISPLAY_X = 800
DISPLAY_Y = 800
FPS = 30

surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
clock = pygame.time.Clock()

target = pygame.image.load("target.png")


class Main:
    def __init__(self):
        self.running = True

        self.player = player.Player(target, (0, 0, 64, 64))
        self.player2 = player.Player(target, (100, 100, 64, 64))

        self.player_group = pygame.sprite.Group()

        self.player_group.add(self.player, self.player2)

        self.time_old = 0
        self.time_current = 0
        self.time_diff = 0
        self.frame_length = 1/FPS
        self.frames_elapsed = 0

    def game_loop(self):
        while self.running:

            self.time_old = self.time_current

            self.time_current = time.time()

            self.time_diff = self.time_current - self.time_old
            self.frames_elapsed = self.time_diff/self.frame_length
            print(self.frames_elapsed)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.x_velocity += -self.player.velocity
                    if event.key == pygame.K_RIGHT:
                        self.player.x_velocity += self.player.velocity
                    if event.key == pygame.K_UP:
                        self.player.y_velocity += -self.player.velocity
                    if event.key == pygame.K_DOWN:
                        self.player.y_velocity += self.player.velocity
                    if event.key == pygame.K_w:
                        self.running = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.x_velocity -= -self.player.velocity
                    if event.key == pygame.K_RIGHT:
                        self.player.x_velocity -= self.player.velocity
                    if event.key == pygame.K_UP:
                        self.player.y_velocity -= -self.player.velocity
                    if event.key == pygame.K_DOWN:
                        self.player.y_velocity -= self.player.velocity

            surface.fill((255, 255, 255))

            self.player.update_location()
            self.player2.update_location()

            # collide.collision_system(self.player, self.player2)
            # print(pygame.sprite.collide_rect(self.player, self.player2))


            self.player_group.draw(surface)

            pygame.display.update()
            clock.tick(FPS)


def frame_limiter():

game = Main()
game.game_loop()
