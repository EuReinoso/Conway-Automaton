class Individual:
    def __init__(self, rect):
        self.rect = rect
        self.alive = False
        self.adjacents = []

    def is_alive(self):
        count = 0
        for adj in self.adjacents:
            if adj.alive:
                count += 1
        if self.alive:
            if count < 2:
                self.alive = False
            if count > 3:
                self.alive = False
        else:
            if count == 3:
                self.alive = True