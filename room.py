import pygame


def load_room(room):
    file = open(room, "r")
    data = file.read()
    file.close()


class Room:
    def __init__(self, room):
        self.tiles = pygame.sprite.Group()

        load_room(room)

