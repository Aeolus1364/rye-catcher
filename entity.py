import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super(Entity, self).__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = rect[0]
        self.rect.y = rect[1]


class Tile(Entity):
    def __init__(self, image, rect):
        super(Tile, self).__init__(image, rect)


class Door(Entity):
    def __init__(self, image, rect, dest, coords):
        super(Door, self).__init__(image, rect)

        self.room_dest = dest
        self.coords = coords