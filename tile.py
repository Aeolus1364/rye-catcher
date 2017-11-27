import entity
import sprite_pack


class Tile(entity.Entity):
    def __init__(self, surface, rect):
        super(Tile, self).__init__(surface, rect)

        self.image = sprite_pack.target

    def render(self):
        self.surface.blit(self.image, (self.x, self.y))


