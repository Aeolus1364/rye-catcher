import pygame
import entity


class Player:
    def __init__(self, image, rect, offset):

        self.sprite = PlayerSprite(image, rect, offset)

        self.rect = pygame.Rect(rect)

        self.x_velocity = 0
        self.y_velocity = 0

        self.x_velocity_old = 0
        self.y_velocity_old = 0

        self.velocity = 8

        self.delta_t = 0

        self.moving = True

    def update_x(self):
        self.rect.x += self.x_velocity * self.delta_t

    def update_y(self):
        self.rect.y += self.y_velocity * self.delta_t

    def update_sprite(self):
        self.sprite.update_pos(self.rect.x, self.rect.y)


class PlayerSprite(entity.Entity):
    def __init__(self, image, rect, offset):
        super(PlayerSprite, self).__init__(image, rect)

        self.x_offset = offset[0]
        self.y_offset = offset[1]

    def update_pos(self, x, y):
        self.rect.x = x + self.x_offset
        self.rect.y = y + self.y_offset




