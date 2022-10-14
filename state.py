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
        previousState = None
        size = self.size
        depth = 0

        stop = 0

        while self.heuristic(states[0], size) != 0 and stop!=20:
            state = states.pop(0)
            fValues = []
            possibleMoves = move(state)

            #print(possibleMoves)

            #calculate misplaced tiles
            for possibleMove in possibleMoves:
                print(possibleMove)
                f = getFValue(deepcopy(possibleMove), depth, self.heuristic)
                fValues.append(f)

            print(fValues)
            minF = min(fValues)
            print("minF: " + str(minF))
            bestMoves = []

            for i, f in enumerate(fValues):
                if f == minF: #and possibleMoves[i] != previousState:
                    print('asd')
                    bestMoves.append(possibleMoves[i])

            print(bestMoves)

            previousState = state
            #states.extend(bestMoves)
            states = bestMoves
            #depth += 1
            stop += 1
            print(stop)
            print("States:\n{}".format(printBoardString(states)))



    def solveD(self):
        states = deepcopy(self.currentState)
        previousState = None
        size = self.size
        depth = 0

        print("Original State: {}".format(DEFAULT_GAME))
        stop = 0   

        while self.heuristic(states[0], size) != 0 and stop!=20:
            state = states.pop(0)
            possibleMoves = move(state)

            #print(possibleMoves)

            #get Manhattan distances
            manhattanValues = []
            for possibleMove in possibleMoves:
                #print(possibleMove)
                manhattanValues.append(getManhattanDistance(deepcopy(possibleMove), self.solved))

            print("manhattanValues: {}".format(manhattanValues))

            minManhattan = min(manhattanValues)
            print("min manhattan: " + str(minManhattan))
            bestMoves = []

            for i, val in enumerate(manhattanValues):
                if val == minManhattan: #and possibleMoves[i] != previousState:
                    bestMoves.append(possibleMoves[i])


            print("bestmoves: {} ".format(bestMoves))

            previousState = state
            #states.extend(bestMoves)
            
            #see if any of our best moves is the end step
            npbestMoves = np.array(bestMoves)
            if (np.argwhere(npbestMoves == solved)):
                break

            states = bestMoves
            #depth += 1
            stop += 1
            print(stop)
            print("States:\n{}".format(printBoardString(states)))


def generateDebugTable(states, seen, depth, steps):
    print("Board States:\n" + printBoardString(states))
    print("seen:\n" + str(seen))
    print("depth:\n" + str(depth))
    print("steps:\n" + str(steps))


state = State(8, h1)
#solve(state.currentState, state.size, state.heuristic)
state.solveD()