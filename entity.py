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


class Button(Entity):
    def __init__(self, image, image2, rect, text):
        super(Button, self).__init__(image, rect)

        self.selected = False
        self.image1 = image
        self.image2 = image2

        self.font = pygame.font.SysFont("monospace", 30)
        self.label = self.font.render(text, 1, (0, 0, 0))

    def update(self, surface):
        if self.selected:
            self.image = self.image2
        else:
            self.image = self.image1

        surface.blit(self.label, (self.rect.x + 10, self.rect.centery - 15))