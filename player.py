import pygame
import entity


class Player(entity.Entity):
    def __init__(self, surface, rect, images):
        super(Player, self).__init__(surface, rect)

        self.x_velocity = 0
        self.y_velocity = 0

        self.x_past = 0
        self.y_past = 0

        self.images = images

        self.num_img = 6
        self.current = 0

        self.current_frame = 0
        self.max_frame = 4.3

    def update(self):
        self.x_past = self.x
        self.y_past = self.y

        self.x += self.x_velocity
        self.y += self.y_velocity

        self.current_frame += 1
        if self.current_frame > self.max_frame:


            self.current += 1
            self.current_frame = 0
        if self.current > self.num_img:
            self.current = 0

    def render(self):
        self.surface.blit(self.images, (self.x, self.y), (self.width*self.current, 0, self.width, self.height))
        # surface.blit(self.test.images, (self.test.x, self.test.y), (self.test.x_w*self.test.current, 0, self.test.x_w, self.test.x_h))
