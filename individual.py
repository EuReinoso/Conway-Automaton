class Individual:
    def __init__(self, rect):
        self.rect = rect
        self.alive = False
        self.adjacents = []