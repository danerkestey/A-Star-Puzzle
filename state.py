from copy import deepcopy
from random import random
from utils.generate import *
from utils.heuristics import *
from utils.move import *

'''State class is used to keep track of the states and their values/matrix'''


class State:
    def __init__(self, matrix, depth, fvalue):
        # init the each state that has its matrix, current tree depth and fvalue
        self.matrix = matrix
        self.depth = depth
        self.fvalue = fvalue


'''Main Function, used to solve, generate, and output the data'''


class PuzzleSolver:
    def __init__(self, size, heuristics):
        self.size = size
        self.solved = generateSolvedMatrix(self.size)
        self.steps = 0  # used to count the number of steps across path
        self.travelledStates = []
        self.availableStates = []
        self.heuristics = heuristics

    def solve(self):
        randomMatrix = generateValidRandomMatrix(self.size)
        initialState = State(randomMatrix, 0, 0)
        initialState.fvalue = getFValue(
            deepcopy(initialState.matrix), self.solved)

        initialState.fvalue = getFValue(
            deepcopy(initialState.matrix), self.solved)
        print("initial state matrix: {}\nfvalue {}\ndepth {}\n".format(
            initialState.matrix, initialState.fvalue, initialState.depth))

        # append the initial state to the available states
        self.availableStates.append(initialState)

        while self.steps != 10000:
            currState = self.availableStates[0]

            if currState.fvalue == 0:  # if the f value is 0 we are done
                break

            # print(currState.matrix)

            # get all next states and append new state objects to the availableStates list
            possibleMoves = move(currState.matrix)
            for moves in possibleMoves:
                newState = State(moves, deepcopy(currState).depth+1, 0)
                newState.fvalue = getFValue(
                    deepcopy(newState.matrix), self.solved)

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

        print(currState.matrix)
        print(self.steps)
        print(len(self.availableStates) + len(self.travelledStates))


'''Runnable'''
puzzle = PuzzleSolver(15, h3)
puzzle.solve()
