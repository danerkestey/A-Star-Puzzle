from copy import deepcopy
from utils.generate import *
from utils.heuristics import *
from utils.move import *
from solve import *


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
        seen.append(self.testPrint(states[0].tolist()))
        seenD = {}
        seenD[self.testPrint(states[0].tolist())] = ""
        minF = 0
        # print(states[0])
        while self.heuristic(states[0], self.size) != 0:
            # for _ in range(3):
            for state in states:
                bestMoves = move(deepcopy(state), depth, self.heuristic)

                print(len(bestMoves))
                nextState = []
                for m in bestMoves:
                    sM = self.testPrint(m)
                    if sM not in seenD:
                        print("Ayoo")
                        nextState.append(m)
                        seenD[sM] = ""

                print(len(nextState))
                if len(nextState) > 0:
                    states = deepcopy(nextState)

                print(states)
                print("-------------")
                steps += 1
                depth += 1


state = State(8, h1)
# solve(state.currentState, state.size, state.heuristic)
state.solve()
