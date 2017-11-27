import pygame
import entity
import player
import collide
import sprite_pack
import constants

pygame.init()

surface = pygame.display.set_mode((constants.DISPLAY_X, constants.DISPLAY_Y))
clock = pygame.time.Clock()


class Main:
    def __init__(self):
        self.running = True

        self.player = player.Player(surface, (0, 0, 90, 90))
        self.player2 = player.Player(surface, (100, 100, 90, 90))

    def game_loop(self):
        while self.running:
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
                    if event.key == pygame.K_q:
                        self.player.load_pack(cube_pack2)
                        print("done")

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
            self.player.update_sprite()
            self.player2.update_location()
            self.player2.update_sprite()

            collide.collision_system(self.player, self.player2)

            self.player.render()
            self.player2.render()

            pygame.display.update()
            clock.tick(constants.FPS)


game = Main()
game.game_loop()
