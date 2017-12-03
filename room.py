import pygame
import entity
import collide


class Room:
    def __init__(self, room):
        self.tiles = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()

        file = open(room, "r")
        data = file.read()
        file.close()

        x_cursor = 0
        y_cursor = 0

        tile_size = 64

        data_setx = data.splitlines()

        for i in data_setx:
            data_sety = list(i)
            x_cursor = 0

            for j in data_sety:
                if j == "H":
                    self.tiles.add(
                        entity.Tile(pygame.Surface((tile_size, tile_size)), (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "G":
                    self.doors.add(entity.Door(pygame.image.load("resources/wall.png"),
                                                 (x_cursor, y_cursor, tile_size, tile_size), 1, (64, 256)))
                x_cursor += tile_size
            y_cursor += tile_size

    def render(self, surface):
        self.tiles.draw(surface)
        self.doors.draw(surface)

    def collide(self, player):
        collide.collision_resolve(player, self.tiles)

        for i in self.doors:
            if collide.collision_test(player.rect, i):
                player.rect.x = i.coords[0]
                player.rect.y = i.coords[1]
                return i.room_dest