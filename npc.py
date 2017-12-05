import entity


class NPC(entity.Entity):
    def __init__(self, image, rect, npc_id, text):
        super(NPC, self).__init__(image, rect)

        self.npc_id = npc_id

        self.activate = False
        self.end = False

        file = open(text, "r")
        data = file.read()
        file.close()

        self.texts = data.splitlines()
        self.counter = -1

    def interact(self):
        if self.counter < len(self.texts) - 1:
            self.counter += 1
            if self.texts[self.counter] == "Scientist: Stop right there!":
                self.activate = True
            elif self.texts[self.counter] == "You: I only wanted to save them...":
                self.end = True
            return self.texts[self.counter]
