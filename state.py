from puzzle.generate import generateValidRandomMatrix


class State:
    def __init__(self, size):
        self.size = size
        self.currentState = generateValidRandomMatrix(self.size)
