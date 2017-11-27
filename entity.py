import pygame


class Entity:
    def __init__(self, surface, rect):
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]

        self.surface = surface

