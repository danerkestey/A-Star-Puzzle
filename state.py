from copy import deepcopy
from utils.generate import *
from utils.heuristics import *
from utils.move import *

DEFAULT_GAME = [[[1, 0, 2],
                [3, 4, 5],
                [6, 7, 8]]]

DEFAULT_GAME2 = [[[1, 5, 2],
                  [3, 0, 4],
                  [6, 7, 8]]]


class State:
    def __init__(self, size, heuristic):
        self.size = size
        #self.currentState = [generateValidRandomMatrix(self.size)]
        self.currentState = DEFAULT_GAME
        self.heuristic = heuristic  # h(n)
        self.depth = 0  # g(n)
        self.solved = generateSolvedMatrix(self.size)
        self.steps = 0
        self.seenStates = []

    def solve(self):
        states = deepcopy(self.currentState)
        seen = deepcopy(self.seenStates)
        depth = deepcopy(self.depth)
        steps = deepcopy(self.steps)

        print("Location of 0: " + str(getRequiredValues(states[0])) + '\n')
        print(printBoardString(states) + '\n')

        print("Possible Moves: ")
        print(printBoardString(move(states[0])))

        #print("\n\n::::::Debugging table:::::\n")
        #generateDebugTable(states, seen, depth, steps)





state = State(8, h1)
#solve(state.currentState, state.size, state.heuristic)
state.solve()
