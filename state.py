from utils.generate import *
from utils.heuristics import *


class State:
    def __init__(self, size, heuristic):
        self.size = size
        self.currentState = [generateValidRandomMatrix(self.size)]
        self.heuristic = heuristic  # h(n)
        self.depth = 0  # g(n)
        self.solved = generateSolvedMatrix(self.size)
        self.steps = 0
        self.seenStates = []

    def getUniqueIdentifier(self, state, depth):
        state1D = list(chain.from_iterable(state))
        dp = disorderParameter(state)

        uniqueStr = "".join(str(x) for x in state1D)
        uniqueStr += str(depth)
        uniqueStr += str(dp)

        return uniqueStr

    def getRequiredValues(self, state):
        hash = generateHashMatrix(state)
        i1 = getEmptySpacePosition(hash)[0]
        j1 = getEmptySpacePosition(hash)[1]

        return i1, j1

    def swap(self, state, i1, j1, i2, j2):
        tempMat = state
        temp = tempMat[i1][j1]
        tempMat[i1][j1] = tempMat[i2][j2]
        tempMat[i2][j2] = temp
        return tempMat

    def moveUp(self, state, depth):
        i1, j1 = self.getRequiredValues(state)
        i2, j2 = i1 + 1, j1
        temp = state
        h = self.heuristic(temp, self.size)
        g = depth + 1
        if i2 < len(state):
            temp = self.swap(state, i1, j1, i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')

        f = g + h
        return [f, temp]

    def moveDown(self, state, depth):
        i1, j1 = self.getRequiredValues(state)
        i2, j2 = i1 - 1, j1
        temp = state
        h = self.heuristic(temp, self.size)
        g = depth + 1
        if i2 >= 0:
            temp = self.swap(state, i1, j1, i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')

        f = g + h
        return [f, temp]

    def moveLeft(self, state, depth):
        i1, j1 = self.getRequiredValues(state)
        i2, j2 = i1, j1 - 1
        temp = state
        h = self.heuristic(temp, self.size)
        g = depth + 1
        if j2 >= 0:
            temp = self.swap(state, i1, j1, i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')

        f = g + h
        return [f, temp]

    def moveRight(self, state, depth):
        i1, j1 = self.getRequiredValues(state)
        i2, j2 = i1, j1 + 1
        temp = state
        h = self.heuristic(temp, self.size)
        g = depth + 1
        if j2 < len(state[0]):
            temp = self.swap(state, i1, j1, i2, j2)
            h = self.heuristic(temp, self.size)
        else:
            h = float('inf')

        f = g + h
        return [f, temp]

    def solve(self):
        # print(self.currentState)
        # print(self.solved)
        # g = self.depth
        # state = self.currentState
        # size = self.size
        # while self.heuristic(state, size) != 0:
        #     t1, t2, t3, t3 = self.moveUp(g), self.moveDown(
        #         g), self.moveLeft(g), self.moveRight(g)
        #     nextState = sorted([t1, t2, t3, t3])[0]
        #     # print("State: ", nextState[1], " f value: ", nextState[0])
        #     print(sorted([t1, t2, t3, t3]))
        #     self.steps += 1
        #     g += 1
        #     state = nextState[1]
        self.seenStates.append(self.getUniqueIdentifier(
            self.currentState[0], self.depth))
        while self.heuristic(self.currentState[0], self.size) != 0:
            self.depth += 1
            for state in self.currentState:
                t1, t2, t3, t4 = self.moveUp(state, self.depth), self.moveDown(
                    state, self.depth), self.moveLeft(state, self.depth), self.moveRight(state, self.depth)
                potentialStates = {}
                fValues = []
                for t in [t1, t2, t3, t4]:
                    tStr = self.getUniqueIdentifier(t[1], self.depth)
                    if tStr not in self.seenStates:
                        fValues.append(t[0])
                        potentialStates[t[0]] = t[1]
                minF = min(fValues)
                nextState = []
                for key in potentialStates:
                    if key == minF:
                        nextState.append(potentialStates[key])
                        self.seenStates.append(potentialStates[key])
                self.currentState = nextState
                self.steps += 1
                print(self.currentState)

    def test(self):
        print(self.heuristic(self.solved, self.size))


state = State(8, h1)
state.solve()
