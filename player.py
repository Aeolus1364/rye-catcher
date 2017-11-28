import pygame
import entity


class Player(entity.Entity):
    def __init__(self, image, rect):
        super(Player, self).__init__(image, rect, True)

        self.x_velocity = 0
        self.y_velocity = 0

        self.velocity = 10

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        self.x_past = 0  # saves coordinates one frame in the past for collision
        self.y_past = 0

        self.moving = True

    def update_location(self):
        self.x_past = self.rect[0]
        self.y_past = self.rect[1]

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        # self.rect = (self.rect[0] + self.x_velocity, self.rect[1] + self.y_velocity, self.rect[2], self.rect[3])
