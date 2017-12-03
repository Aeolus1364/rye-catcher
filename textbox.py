import entity
import pygame


class TextBox(entity.Entity):
    def __init__(self, font):
        super(TextBox, self).__init__(pygame.image.load("textbox.png"), (0, 640, 1024, 128))

        self.font = pygame.font.SysFont("monospace", 30)

    def write(self, text):
        label = self.font.render(text, 1, (0, 0, 0))
        return label
