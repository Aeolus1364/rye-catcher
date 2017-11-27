import pygame
import constants


slime = pygame.image.load("spritesheet_large.png")
cube = pygame.image.load("cube_spritesheet.png")
cube2 = pygame.image.load("cube_spritesheet2.png")

cube_pack = (cube, 3, constants.FPS/7)  # image surface, number of frames (starts at 0), frame rate
cube_pack2 = (cube2, 3, constants.FPS/7)
