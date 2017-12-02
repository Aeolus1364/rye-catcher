import pygame
import entity
import player
import collide
import time
import room
import random


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

        self.player = player.Player(target, (0, 50, 64, 64), (0, 0))
        self.tile = entity.Tile(pygame.Surface((64, 64)), (100, 50, 64, 64))
        self.tile2 = entity.Tile(pygame.Surface((100, 100)), (50, 100, 100, 100))

        self.room = room.Room("room.txt")

        self.player_group = pygame.sprite.Group()
        self.tile_group = pygame.sprite.Group()

        self.player_group.add(self.player.sprite)

        self.time_old = 0
        self.time_current = 0
        self.time_diff = 0
        self.frame_length = 1/FPS
        self.delta_t = 0

        for i in range(10):
            tile = entity.Tile(pygame.Surface((64, 64)), (random.randint(0, 500), random.randint(0, 500), 64, 64))
            self.tile_group.add(tile)

    def game_loop(self):
        while self.running:

            self.time_old = self.time_current

            self.time_current = time.time()

            self.time_diff = self.time_current - self.time_old
            self.delta_t = self.time_diff / self.frame_length

            self.player.delta_t = self.delta_t

            self.player.x_velocity_old = self.player.x_velocity
            self.player.y_velocity_old = self.player.y_velocity

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.x_velocity += -self.player.velocity
                        self.player.y_velocity = 0
                    if event.key == pygame.K_RIGHT:
                        self.player.x_velocity += self.player.velocity
                        self.player.y_velocity = 0
                    if event.key == pygame.K_UP:
                        self.player.y_velocity += -self.player.velocity
                        self.player.x_velocity = 0
                    if event.key == pygame.K_DOWN:
                        self.player.y_velocity += self.player.velocity
                        self.player.x_velocity = 0
                    if event.key == pygame.K_w:
                        self.running = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if self.player.x_velocity:
                            self.player.x_velocity -= -self.player.velocity
                    if event.key == pygame.K_RIGHT:
                        if self.player.x_velocity:
                            self.player.x_velocity -= self.player.velocity
                    if event.key == pygame.K_UP:
                        if self.player.y_velocity:
                            self.player.y_velocity -= -self.player.velocity
                    if event.key == pygame.K_DOWN:
                        if self.player.y_velocity:
                            self.player.y_velocity -= self.player.velocity

            surface.fill((255, 255, 255))

            collide.collision_resolve(self.player, self.tile_group.sprites())

            self.player.update_sprite()

            self.player_group.draw(surface)
            self.tile_group.draw(surface)

            pygame.display.update()
            clock.tick(FPS)


game = Main()
game.game_loop()
