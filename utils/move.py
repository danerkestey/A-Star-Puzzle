from utils.generate import *
from utils.heuristics import *


def getUniqueIdentifier(state, depth):
    state1D = list(chain.from_iterable(state))
    dp = disorderParameter(state)

    uniqueStr = "".join(str(x) for x in state1D)
    uniqueStr += str(depth)
    uniqueStr += str(dp)

    return uniqueStr


def getRequiredValues(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return i, j


def moveUp(state, depth, heuristic):
    size = len(state) * len(state[0]) - 1
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1 + 1, j1
    g = depth + 1
    if i2 < len(state):
        state[i1][j1], state[i2][j2] = state[i2][j2], state[i1][j1]
        h = heuristic(state, size)
    else:
        h = float('inf')

    f = g + h
    if isinstance(state, np.ndarray):
        return [f, state.tolist()]
    else:
        return [f, state]


def moveDown(state, depth, heuristic):
    size = len(state) * len(state[0]) - 1
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1 - 1, j1
    g = depth + 1
    if i2 >= 0:
        state[i1][j1], state[i2][j2] = state[i2][j2], state[i1][j1]
        h = heuristic(state, size)
    else:
        h = float('inf')

    f = g + h
    if isinstance(state, np.ndarray):
        return [f, state.tolist()]
    else:
        return [f, state]


def moveLeft(state, depth, heuristic):
    size = len(state) * len(state[0]) - 1
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1, j1 - 1
    g = depth + 1
    if j2 >= 0:
        state[i1][j1], state[i2][j2] = state[i2][j2], state[i1][j1]
        h = heuristic(state, size)
    else:
        h = float('inf')

    f = g + h
    if isinstance(state, np.ndarray):
        return [f, state.tolist()]
    else:
        return [f, state]


def moveRight(state, depth, heuristic):
    size = len(state) * len(state[0]) - 1
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1, j1 + 1
    g = depth + 1
    if j2 < len(state[0]):
        state[i1][j1], state[i2][j2] = state[i2][j2], state[i1][j1]
        h = heuristic(state, size)
    else:
        h = float('inf')

    f = g + h
    if isinstance(state, np.ndarray):
        return [f, state.tolist()]
    else:
        return [f, state]
