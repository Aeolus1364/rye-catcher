import entity
import pygame


class TextBox(entity.Entity):
    def __init__(self, font):
        super(TextBox, self).__init__(pygame.image.load("resources/textbox.png"), (0, 640, 1024, 128))

        self.font = pygame.font.SysFont("monospace", 20)

        self.x_offset = 10
        self.y_offset = 10
        self.text = ""

    def write(self, surface):
        label = self.font.render(self.text, 1, (0, 0, 0))
        surface.blit(label, (self.rect.x + self.x_offset, self.rect.y + self.y_offset))
