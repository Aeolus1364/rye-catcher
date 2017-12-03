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

clock = pygame.time.Clock()

target = pygame.image.load("resources/player_real.png")
button = pygame.image.load("resources/button.png")  # 256 * 64
button2 = pygame.image.load("resources/button_pressed.png")

pygame.display.set_caption("Game")
pygame.display.set_icon(target)


class Main:
    def __init__(self):
        self.surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))

        # menu vars
        self.menu_running = True
        self.button_selected = 0

        self.button_play = entity.Button(button, button2, (DISPLAY_X/2 - 256/2, DISPLAY_Y/2 - 64, 256, 64), "Play")
        self.button_options = entity.Button(button, button2, (DISPLAY_X/2 - 256/2, DISPLAY_Y/2 + 64, 256, 64), "Settings")

        self.menu_elements = pygame.sprite.Group(self.button_play, self.button_options)

        # game_loop vars
        self.running = True
        self.controls_enabled = True
        self.player = player.Player(target, (100, 128, 52, 30), (-6, -64 - 30))

        self.rooms = []
        for i in range(2):
            temproom = room.Room("resources/room"+str(i)+".txt")
            self.rooms.append(temproom)

        self.current_room = 0

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
        self.menu()
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

                if self.controls_enabled:
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
                        if event.key == pygame.K_e:
                            self.surface = self.surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y), pygame.FULLSCREEN)

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

            self.surface.fill((255, 255, 255))

            switch = self.rooms[self.current_room].collide(self.player)
            if switch is not None:
                self.current_room = switch

            self.player.update_sprite()

            self.rooms[self.current_room].render(self.surface)
            pygame.draw.rect(self.surface, (100, 50, 100), self.player.rect)

            self.player_group.draw(self.surface)

            self.screen_elements.draw(self.surface)

            self.textbox.write("Testing testing 123", self.surface)

            pygame.display.update()
            clock.tick(FPS)
        pygame.quit()

    def menu(self):
        while self.menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_running = False
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.button_selected += 1
                        if self.button_selected > 1:
                            self.button_selected = 0
                    if event.key == pygame.K_UP:
                        self.button_selected -= 1
                        if self.button_selected < 0:
                            self.button_selected = 1
                    if event.key == pygame.K_SPACE:
                        if self.button_play.selected:
                            self.menu_running = False
                        elif self.button_options.selected:
                            pass

            self.surface.fill((255, 255, 255))

            self.menu_elements.draw(self.surface)

            if self.button_selected == 0:
                self.button_play.selected = True
                self.button_options.selected = False
            elif self.button_selected == 1:
                self.button_options.selected = True
                self.button_play.selected = False

            self.button_play.update(self.surface)
            self.button_options.update(self.surface)

            pygame.display.update()
            clock.tick(FPS)

game = Main()
game.game_loop()
