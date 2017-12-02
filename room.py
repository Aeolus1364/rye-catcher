import pygame
import entity


def load_room(room):
    file = open(room, "r")
    data = file.read()
    file.close()

    x_cursor = 0
    y_cursor = 0

    tile_size = 64

    tile_list = []

    data_setx = data.splitlines()

    for i in data_setx:
        data_sety = list(i)
        x_cursor = 0

        for j in data_sety:
            if j == "H":
                print(x_cursor, y_cursor)
                tile_list.append(entity.Tile(pygame.Surface((tile_size, tile_size)), (x_cursor, y_cursor, tile_size, tile_size)))
            x_cursor += tile_size
        y_cursor += tile_size

    return tile_list


class Room:
    def __init__(self, room):
        self.tiles = pygame.sprite.Group()

        for i in load_room(room):
            self.tiles.add(i)