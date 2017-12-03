import pygame
import entity
import player
import collide
import time
import room
import random
import textbox


pygame.init()

DISPLAY_X = 64*16
DISPLAY_Y = 64*12
FPS = 30

surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
clock = pygame.time.Clock()

target = pygame.image.load("player.png")

pygame.display.set_caption("Game")
pygame.display.set_icon(target)


class Main:
    def __init__(self):
        self.running = True

        self.player = player.Player(target, (100, 128, 48, 48), (-8, -72))

        self.room = room.Room("room.txt")

        self.textbox = textbox.TextBox(None)

        self.player_group = pygame.sprite.Group()
        self.tile_group = pygame.sprite.Group()
        self.screen_elements = pygame.sprite.Group(self.textbox)

        self.player_group.add(self.player.sprite)

        self.time_old = 0
        self.time_current = 0
        self.time_diff = 0
        self.frame_length = 1/FPS
        self.delta_t = 0

        # for i in range(10):
        #     tile = entity.Tile(pygame.Surface((64, 64)), (random.randint(0, 500), random.randint(0, 500), 64, 64))
        #     self.tile_group.add(tile)

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

            collide.collision_resolve(self.player, self.room.tiles.sprites())

            self.player.update_sprite()

            self.room.tiles.draw(surface)
            self.player_group.draw(surface)
            pygame.draw.rect(surface, (100, 50, 100), self.player.rect)
            self.screen_elements.draw(surface)
            surface.blit(self.textbox.write("Testing testing 123"), (self.textbox.rect.x + 10, self.textbox.rect.y + 10))

            pygame.display.update()
            clock.tick(FPS)
        pygame.quit()


game = Main()
game.game_loop()
