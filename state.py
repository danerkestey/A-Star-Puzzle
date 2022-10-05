from puzzle.generate import *


class State:
    def __init__(self, size):
        self.size = size
        self.currentState = generateValidRandomMatrix(self.size)
        self.hash = generateHashMatrix(self.currentState)
        self.i1 = getEmptySpacePosition(self.hash)[0]
        self.j1 = getEmptySpacePosition(self.hash)[1]

    def swap(self, i2, j2):
        temp = self.currentState[self.i1][self.j1]
        self.currentState[self.i1][self.j1] = self.currentState[i2][j2]
        self.currentState[i2][j2] = temp

    def moveUp(self):
        print(self.currentState)
        i2, j2 = self.i1 + 1, self.j1
        if i2 < len(self.currentState):
            self.swap(i2, j2)
        print(self.currentState)

    def moveDown(self):
        print(self.currentState)
        i2, j2 = self.i1 - 1, self.j1
        if i2 >= 0:
            self.swap(i2, j2)
        print(self.currentState)

    def moveLeft(self):
        print(self.currentState)
        i2, j2 = self.i1, self.j1 - 1
        if j2 >= 0:
            self.swap(i2, j2)
        print(self.currentState)

    def moveRight(self):
        print(self.currentState)
        i2, j2 = self.i1, self.j1 + 1
        if j2 < len(self.currentState[0]):
            self.swap(i2, j2)
        print(self.currentState)


state = State(8)
state.moveDown()
