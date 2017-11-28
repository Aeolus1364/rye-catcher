import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, image, rect, bind_image):
        super(Entity, self).__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = rect[0]
        self.rect.y = rect[1]