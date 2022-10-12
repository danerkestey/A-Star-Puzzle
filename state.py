from copy import deepcopy
from utils.generate import *
from utils.heuristics import *
from utils.move import *

DEFAULT_GAME2 = [[[1, 0, 2],
                  [3, 4, 5],
                  [6, 7, 8]]]

DEFAULT_GAME = [[[1, 5, 2],
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
        possibleMoves = move(states[0])
        for m in possibleMoves:
            fValue = getFValue(deepcopy(m), 0, self.heuristic)
            print("Move: ", end="")
            print(m, end=", ")
            print(fValue)

        #print("\n\n::::::Debugging table:::::\n")
        #generateDebugTable(states, seen, depth, steps)

    def solveD(self):
        states = deepcopy(self.currentState)
        previousState = None
        size = self.size
        depth = 0

        stop = 0

        while self.heuristic(states[0], size) != 0 or stop!=15:
            state = states.pop(0)
            fValues = []
            possibleMoves = move(state)

            for m in possibleMoves:
                f = getFValue(deepcopy(m), depth, self.heuristic)
                fValues.append(f)

            print(fValues)
            minF = min(fValues)
            print("minF: " + str(minF))
            bestMoves = []

            for i, f in enumerate(fValues):
                if f == minF and possibleMoves[i] != previousState:
                    bestMoves.append(possibleMoves[i])

            previousState = state
            #states.extend(bestMoves)
            states = bestMoves
            depth += 1
            stop += 1
            print("States:\n{}".format(printBoardString(states)))


def generateDebugTable(states, seen, depth, steps):
    print("Board States:\n" + printBoardString(states))
    print("seen:\n" + str(seen))
    print("depth:\n" + str(depth))
    print("steps:\n" + str(steps))


state = State(8, h1)
#solve(state.currentState, state.size, state.heuristic)
state.solveD()