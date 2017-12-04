import entity


class NPC(entity.Entity):
    def __init__(self, image, rect, npc_id):
        super(NPC, self).__init__(image, rect)

        self.npc_id = npc_id

        file = open("resources/npc_reject.txt", "r")
        data = file.read()
        file.close()

        self.texts = data.splitlines()
        self.counter = -1

    def interact(self):
        self.counter += 1
        if self.counter > len(self.texts) - 1:
            self.counter = 0
        return self.texts[self.counter]
