from utils.generate import *


def getFValue(state, g, heuristic):
    size = len(state) * len(state[0]) - 1
    h = heuristic(state, size)
    return g + h


def h1(stateMatrix, size):
    # The first heuristic: Number of misplaced tiles
    hash = generateHashMatrix(stateMatrix)
    t = generateSolvedMatrix(size)
    count = 0
    # for i in hash:
    #     if i in t and hash[i] != t[i]:
    #         count += 1
    for i in range(len(stateMatrix)):
        for j in range(len(stateMatrix[0])):
            if stateMatrix[i][j] != t[i][j]:
                count += 1
    return count
