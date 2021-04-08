class Individual:
    def __init__(self, rect):
        self.rect = rect
        self.alive = False
        self.adjacents = []

    def is_alive(self):
        count = self.count_alive_adjacents()
        
        if self.alive:
            if count < 2:
                return False
            if count > 3:
                return False
            else:
                return True
        else:
            if count == 3:
                return True
            else:
                return False
    
    def count_alive_adjacents(self):
        count = 0
        for adj in self.adjacents:
            if adj.alive:
                count += 1
        return count