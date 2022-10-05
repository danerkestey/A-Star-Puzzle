from utils.generate import *
from utils.heuristics import *


class State:
    def __init__(self, size, heuristic):
        self.size = size
        self.currentState = generateValidRandomMatrix(self.size)
        self.hash = generateHashMatrix(self.currentState)
        self.i1 = getEmptySpacePosition(self.hash)[0]
        self.j1 = getEmptySpacePosition(self.hash)[1]
        self.heuristic = heuristic
        self.solved = generateSolvedMatrix(self.size)
        self.steps = 0

    def swap(self, i2, j2):
        tempMat = self.currentState
        temp = tempMat[self.i1][self.j1]
        tempMat[self.i1][self.j1] = tempMat[i2][j2]
        tempMat[i2][j2] = temp
        return tempMat

    def moveUp(self):
        i2, j2 = self.i1 + 1, self.j1
        temp = self.currentState
        h = self.heuristic(temp, self.size)
        if i2 < len(self.currentState):
            temp = self.swap(i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')
        return [h, temp]

    def moveDown(self):
        i2, j2 = self.i1 - 1, self.j1
        temp = self.currentState
        h = self.heuristic(temp, self.size)
        if i2 >= 0:
            temp = self.swap(i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')
        return [h, temp]

    def moveLeft(self):
        i2, j2 = self.i1, self.j1 - 1
        temp = self.currentState
        h = self.heuristic(temp, self.size)
        if j2 >= 0:
            temp = self.swap(i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')
        return [h, temp]

    def moveRight(self):
        i2, j2 = self.i1, self.j1 + 1
        temp = self.currentState
        h = self.heuristic(temp, self.size)
        if j2 < len(self.currentState[0]):
            temp = self.swap(i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')
        return [h, temp]

    def solve(self):
        print(self.currentState)
        print(self.solved)
        while self.heuristic(self.currentState, self.size) != 0:
            print(self.currentState)
            t1, t2, t3, t3 = self.moveUp(), self.moveDown(), self.moveLeft(), self.moveRight()
            nextState = sorted([t1, t2, t3, t3])[0]
            self.steps += 1
            self.currentState = nextState[1]


state = State(8, h1)
state.solve()
