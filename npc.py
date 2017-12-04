import entity


class NPC(entity.Entity):
    def __init__(self, image, rect, npc_id, text):
        super(NPC, self).__init__(image, rect)

        self.npc_id = npc_id

        file = open(text, "r")
        data = file.read()
        file.close()

        self.texts = data.splitlines()
        self.counter = -1

    def interact(self):
        if self.counter < len(self.texts) - 1:
            self.counter += 1
            return self.texts[self.counter]
