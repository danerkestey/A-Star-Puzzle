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

    def turnToString(self, matrix):
        text = ''

        # traverse the matrix and append the char
        for i in matrix:
            for j in i:
                text += str(j)

        return text


state = State(8, h1)
# solve(state.currentState, state.size, state.heuristic)
# state.solve()
