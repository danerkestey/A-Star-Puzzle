from copy import deepcopy
from utils.generate import *
from utils.heuristics import *
from utils.move import *


class State:
    def __init__(self, size, heuristic):
        self.size = size
        self.currentState = [generateValidRandomMatrix(self.size)]
        self.heuristic = heuristic  # h(n)
        self.depth = 0  # g(n)
        self.solved = generateSolvedMatrix(self.size)
        self.steps = 0
        self.seenStates = []

    def testPrint(self, arr):
        t = ""
        for level in arr:
            temp = "["
            q = ''.join(str(i) for i in level)
            temp += q
            temp += "]"
            t += temp
        return t

    def solve(self):
        states = deepcopy(self.currentState)
        seen = deepcopy(self.seenStates)
        depth = deepcopy(self.depth)
        steps = deepcopy(self.steps)
        seen.append(states[0].tolist())
        minF = 0
        # print(states[0])
        while self.heuristic(states[0], self.size) != 0:
            # for _ in range(3):
            for state in states:
                t1 = moveUp(deepcopy(state), depth, self.heuristic)
                t2 = moveDown(deepcopy(state), depth, self.heuristic)
                t3 = moveLeft(deepcopy(state), depth, self.heuristic)
                t4 = moveRight(deepcopy(state), depth, self.heuristic)

                fValues = []

                for t in [t1, t2, t3, t4]:
                    if t[1] not in seen:
                        fValues.append(t[0])
                        seen.append(t[1])

                if len(fValues) > 0:
                    minF = min(fValues)

                nextState = []
                for t in [t1, t2, t3, t4]:
                    if t[0] == minF:
                        nextState.append(t[1])

                if len(nextState) > 0:
                    states = deepcopy(nextState)

                print(states)
                print("-------------")
                steps += 1
                depth += 1


state = State(8, h1)
state.solve()
