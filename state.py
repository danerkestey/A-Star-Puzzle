from copy import deepcopy
from random import random
from utils.generate import *
from utils.heuristics import *
from utils.move import *

'''State class is used to keep track of the states and their values/matrix'''


class State:
    def __init__(self, matrix, depth, fvalue):
        self.matrix = matrix
        self.depth = depth
        self.fvalue = fvalue


'''Main Function, used to solve, generate, and output the data'''


class PuzzleSolver:
    def __init__(self, size, matrix, heuristics):
        self.size = size
        self.solved = generateSolvedMatrix(self.size)
        self.steps = 0
        self.travelledStates = []
        self.availableStates = []
        self.heuristics = heuristics
        self.matrix = matrix

    def solve(self):
        randomMatrix = deepcopy(self.matrix)
        initialState = State(randomMatrix, 0, 0)
        state = deepcopy(initialState)
        initialState.fvalue = getFValue(
            state.matrix, self.solved, self.heuristics, state.depth)

        # append the initial state to the available states
        self.availableStates.append(initialState)

        while self.steps != 10000:
            currState = self.availableStates[0]

            if currState.fvalue == 0:  # if the f value is 0 we are done
                break

            # get all next states and append new state objects to the availableStates list
            possibleMoves = move(currState.matrix)
            for moves in possibleMoves:
                newState = State(moves, deepcopy(currState).depth + 1, 0)
                matrix = deepcopy(newState)
                newState.fvalue = getFValue(
                    matrix.matrix, self.solved, self.heuristics, matrix.depth)

                # if we have already travelled the state, don't put it in available states.
                existingState = [
                    state for state in self.travelledStates if state.matrix == newState.matrix]

                if len(existingState) == 0:
                    self.availableStates.append(newState)

            # remove the currState from the available states (already travelled), as well as the duplicate move generated
            del self.availableStates[0]
            self.travelledStates.append(currState)

            # sort the available states by the smallest fvalue
            self.availableStates.sort(key=lambda x: x.fvalue, reverse=False)
            self.steps += 1

        nodesExpanded = len(self.availableStates) + len(self.travelledStates)
        # print("Heuristic: {}, depth: {}".format(
        #     self.heuristics, self.availableStates[0].depth))
        return [self.availableStates[0].depth, nodesExpanded]
