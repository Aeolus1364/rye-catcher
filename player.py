import pygame
import entity
import sprite_pack


class Player(entity.Entity):
    def __init__(self, surface, rect):
        super(Player, self).__init__(surface, rect)

        self.x_velocity = 0
        self.y_velocity = 0

        self.velocity = 10

        self.x_past = 0  # saves coordinates one frame in the past for collision
        self.y_past = 0

        self.images = 0  # sprite sheet surface
        self.num_frames = 0  # number of frames in sprite sheet
        self.frame_rate = 0  # game frames per sprite frame
        self.current_sprite = 0  # current sprite frame
        self.current_frame = 0  # current game frame


        # self.load_pack(pack)

        self.moving = True

    def load_pack(self, pack):  # changes animation cycle
        self.images = pack[0]
        self.num_frames = pack[1]
        self.frame_rate = pack[2]
        self.current_sprite = 0
        self.current_frame = 0

    def update_location(self):
        self.x_past = self.x
        self.y_past = self.y

        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x_velocity or self.y_velocity:
            if not self.moving:
                self.moving = True
                self.load_pack(sprite_pack.cube_pack)
        else:
            if self.moving:
                self.moving = False
                self.load_pack(sprite_pack.blank)

    def update_sprite(self):  # every set amount of frames, the animation frame progresses by one
        self.current_frame += 1
        if self.current_frame > self.frame_rate:
            self.current_sprite += 1
            self.current_frame = 0
        if self.current_sprite > self.num_frames:
            self.current_sprite = 0

    def render(self):  # renders the correct sprite frame from the sheet based on current_sprite count
        self.surface.blit(self.images, (self.x, self.y), (self.width * self.current_sprite, 0, self.width, self.height))
