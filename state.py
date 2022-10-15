from copy import deepcopy
from random import random
from utils.generate import *
from utils.heuristics import *
from utils.move import *

DEFAULT_GAME2 = [[[1, 0, 2],
                  [3, 4, 5],
                  [6, 7, 8]]]

DEFAULT_GAME_NOT_SOLVABLE = [[1, 5, 2],
                             [3, 0, 4],
                             [6, 7, 8]]

DEFAULT_GAME = [[0, 1, 3],
                [4, 2, 5],
                [7, 8, 6]]


class State:
    def __init__(self, matrix, depth, fvalue):
        # init the each state that has its matrix, current tree depth and fvalue
        self.matrix = matrix
        self.depth = depth
        self.fvalue = fvalue


class PuzzleSolver:
    def __init__(self, size, heuristic):
        self.size = size
        #self.currentState = [generateValidRandomMatrix(self.size)]
        self.heuristic = heuristic  # h(n)
        self.solved = generateSolvedMatrix(self.size)
        self.steps = 0  # used to count the number of steps across path
        self.travelledStates = []
        self.availableStates = []

    def solve(self):
        randomMatrix = generateValidRandomMatrix(self.size)
        initialState = State(randomMatrix, 0, 0)
        initialState.fvalue = getManhattanDistance(
            deepcopy(initialState.matrix), self.solved)
        print("initial state matrix: {}\nfvalue {}\ndepth {}\n".format(
            initialState.matrix, initialState.fvalue, initialState.depth))

        # append the initial state to the available states
        self.availableStates.append(initialState)

        size = self.size

        stop = 0
        while stop != 10000:

            """ print("\n--------Iteration Available state {}:--------".format(stop))
            for i in self.availableStates:
                print("Matrix: {}\n fval: {}".format(i.matrix, i.fvalue)) """

            #print("\n--------Iteration {}:--------".format(stop))
            currState = self.availableStates[0]

            if currState.fvalue == 0:  # if the manhatten value is 0 we are done
                break

            # print(currState.matrix)

            # get all next states and append new state objects to the availableStates list
            possibleMoves = move(currState.matrix)
            for moves in possibleMoves:
                newState = State(moves, deepcopy(currState).depth+1, 0)
                newState.fvalue = getManhattanDistance(
                    deepcopy(newState.matrix), self.solved)

                # if we have already travelled the state, don't put it in available states.
                existingState = [
                    state for state in self.travelledStates if state.matrix == newState.matrix]
                if len(existingState) == 0:
                    self.availableStates.append(newState)

            # remove the currState from the available states (already travelled), as well as the duplicate move generated

            """ print('Before delete:')
            for i in self.availableStates:
                print("Matrix: {}\n fval: {}".format(i.matrix, i.fvalue)) """

            del self.availableStates[0]
            self.travelledStates.append(currState)

            # sort the available states by the smallest fvalue
            self.availableStates.sort(key=lambda x: x.fvalue, reverse=False)
            stop += 1

            """ print('\nafter delete & sort:')
            for i in self.availableStates:
                print("Matrix: {}\n fval: {}".format(i.matrix, i.fvalue)) """

        print(currState.matrix)
        print(stop)
        print('good job Chandler!')


def generateDebugTable(states, seen, depth, steps):
    print("Board States:\n" + printBoardString(states))
    print("seen:\n" + str(seen))
    print("depth:\n" + str(depth))
    print("steps:\n" + str(steps))


puzzle = PuzzleSolver(8, h1)
#solve(state.currentState, state.size, state.heuristic)
puzzle.solve()
