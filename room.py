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

        self.activate = False
        self.end = False

        file = open(room, "r")
        data = file.read()
        file.close()

        self.foo = " "

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
                if j == "W":
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/water.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == " ":
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "0":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 1, (0, 64), (True, False)))
                elif j == "1":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 0, (0, 542), (True, False)))
                elif j == "2":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 2, (64, 0), (False, True)))
                elif j == "3":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 1, (896, 0), (False, True)))
                elif j == "4":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 3, (64, 0), (False, True)))
                elif j == "5":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 2, (896, 0), (False, True)))
                elif j == "6":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 4, (64, 0), (False, True)))
                elif j == "7":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 3, (896, 0), (False, True)))
                elif j == "8":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 5, (0, 64), (True, False)))
                elif j == "9":
                    self.doors.add(entity.Door(pygame.image.load("resources/tile.png"),
                                               (x_cursor, y_cursor, tile_size, tile_size), 4, (0, 542), (True, False)))
                elif j == "A":
                    self.npcs.add(npc.NPC(pygame.image.load("resources/scientist.png"),
                                          (x_cursor, y_cursor, tile_size, tile_size), 0, "resources/npc_reject.txt"))
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/blank64x80.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "a":
                    self.triggers.add(
                        entity.TriggerTile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size), 0))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "B":
                    self.npcs.add(npc.NPC(pygame.image.load("resources/scientist.png"),
                                          (x_cursor, y_cursor, tile_size, tile_size), 1, "resources/npc_nursery.txt"))
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/blank64x80.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "b":
                    self.triggers.add(
                        entity.TriggerTile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size), 1))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "C":
                    self.npcs.add(npc.NPC(pygame.image.load("resources/scientist.png"),
                                          (x_cursor, y_cursor, tile_size, tile_size), 1, "resources/npc_boiler.txt"))
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/blank64x80.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "c":
                    self.triggers.add(
                        entity.TriggerTile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size), 1))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "D":
                    self.npcs.add(npc.NPC(pygame.image.load("resources/scientist.png"),
                                          (x_cursor, y_cursor, tile_size, tile_size), 1, "resources/npc_bottle.txt"))
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/blank64x80.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "d":
                    self.triggers.add(
                        entity.TriggerTile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size), 1))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "E":
                    self.npcs.add(npc.NPC(pygame.image.load("resources/scientist.png"),
                                          (x_cursor, y_cursor, tile_size, tile_size), 1, "resources/npc_fitting.txt"))
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/blank64x80.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "e":
                    self.triggers.add(
                        entity.TriggerTile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size), 1))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "F":
                    self.npcs.add(npc.NPC(pygame.image.load("resources/water.png"),
                                          (x_cursor, y_cursor, tile_size, tile_size), 1, "resources/npc_computer.txt"))
                    self.tiles.add(
                        entity.Tile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size)))
                    self.floor.add(
                        entity.Tile(pygame.image.load("resources/tile.png"),
                                    (x_cursor, y_cursor, tile_size, tile_size)))
                elif j == "f":
                    self.triggers.add(
                        entity.TriggerTile(pygame.image.load("resources/blank.png"), (x_cursor, y_cursor, tile_size, tile_size), 1))
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
                if i.x_stick:
                    player.rect.y = i.coords[1]
                if i.y_stick:
                    player.rect.x = i.coords[0]
                return i.room_dest

    def action_test(self, player):
        for i in self.triggers:  # talks to npc
            if collide.collision_test(player.rect, i):
                for j in self.npcs.sprites():
                    if j.npc_id == i.npc_id:
                        self.foo = j.interact()
                        if j.activate:
                            self.activate = True
                            self.npcs.add(npc.NPC(pygame.image.load("resources/scientist.png"),
                                              (448, 16, 64, 64), 1,
                                              "resources/npc_fitting.txt"))
                        if j.end:
                            self.end = True
                        tuple = (self.foo, self.activate, self.end)
                        return tuple


