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

    def turnToString(self, arr):
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
        # Old version: uses array, both don't work
        seen.append(self.turnToString(states[0].tolist()))
        seenD = {}
        seenD[self.turnToString(states[0].tolist())] = ""

        while self.heuristic(states[0], self.size) != 0:
            # for _ in range(3):
            state = states.pop(0)
            bestMoves = move(deepcopy(state), depth, self.heuristic)

            print(bestMoves)
            for m in bestMoves:
                sM = self.turnToString(m)
                if sM not in seen:
                    states.append(m)
                    # seenD[sM] = ""
                    seen.append(sM)

            steps += 1
            depth += 1
            # if len(nextState) > 0:
            #     states = deepcopy(nextState)

            print(len(seen))
            print("-------------")


state = State(8, h1)
# solve(state.currentState, state.size, state.heuristic)
state.solve()
