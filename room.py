import pygame
import entity
import collide
import npc


class Room:
    def __init__(self, room):
        self.tiles = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.triggers = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()

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
                        entity.Tile(pygame.image.load("resources/wall.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == " ":
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "G":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 1, (64, 192)))
                elif j == "F":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 0, (896, 192)))
                elif j == "A":
                    self.npcs.add(npc.NPC(pygame.image.load("resources/scientist.png"),
                                          (x_cursor, y_cursor, tile_size, tile_size), 0))
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/blank64x80.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "Q":
                    self.triggers.add(
                        entity.TriggerTile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size), 0))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))

                x_cursor += tile_size
            y_cursor += tile_size

    def render(self, surface):
        self.tiles.draw(surface)
        self.doors.draw(surface)
        self.floor.draw(surface)
        self.npcs.draw(surface)


    def collide(self, player):
        collide.collision_resolve(player, self.tiles)

        for i in self.doors:  # moves you through the door
            if collide.collision_test(player.rect, i):
                player.rect.x = i.coords[0]
                player.rect.y = i.coords[1]
                return i.room_dest

    def action_test(self, player):
        for i in self.triggers:  # talks to npc
            if collide.collision_test(player.rect, i):
                for j in self.npcs.sprites():
                    if j.npc_id == i.npc_id:
                        return j.interact()

