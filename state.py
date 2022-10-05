from puzzle.generate import *


class State:
    def __init__(self, size, heuristic):
        self.size = size
        self.currentState = generateValidRandomMatrix(self.size)
        self.hash = generateHashMatrix(self.currentState)
        self.i1 = getEmptySpacePosition(self.hash)[0]
        self.j1 = getEmptySpacePosition(self.hash)[1]
        self.heuristic = heuristic

    def swap(self, i2, j2):
        tempMat = self.currentState
        temp = tempMat[self.i1][self.j1]
        tempMat[self.i1][self.j1] = tempMat[i2][j2]
        tempMat[i2][j2] = temp
        return tempMat

    def moveUp(self):
        print(self.currentState)
        i2, j2 = self.i1 + 1, self.j1
        temp = self.currentState
        dp = self.heuristic(temp)
        if i2 < len(self.currentState):
            temp = self.swap(i2, j2)
            dp = self.heuristic(temp)
        else:
            dp = float('inf')
        return [dp, temp]

    def moveDown(self):
        print(self.currentState)
        i2, j2 = self.i1 - 1, self.j1
        temp = self.currentState
        dp = self.heuristic(temp)
        if i2 >= 0:
            temp = self.swap(i2, j2)
            dp = self.heuristic(temp)
        else:
            dp = float('inf')
        return [dp, temp]

    def moveLeft(self):
        print(self.currentState)
        i2, j2 = self.i1, self.j1 - 1
        temp = self.currentState
        dp = self.heuristic(temp)
        if j2 >= 0:
            temp = self.swap(i2, j2)
            dp = self.heuristic(temp)
        else:
            dp = float('inf')
        return [dp, temp]

    def moveRight(self):
        print(self.currentState)
        i2, j2 = self.i1, self.j1 + 1
        temp = self.currentState
        dp = self.heuristic(temp)
        if j2 < len(self.currentState[0]):
            temp = self.swap(i2, j2)
            dp = self.heuristic(temp)
        else:
            dp = float('inf')
        return [dp, temp]


state = State(8, disorderParameter)
print(state.moveUp())
