from copy import deepcopy
from utils.generate import *
from utils.heuristics import *


def getRequiredValues(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return i, j


def swap(state, i1, j1, i2, j2):
    temp = state[i1][j1]
    state[i1][j1] = state[i2][j2]
    state[i2][j2] = temp


def moveUp(state):
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1 + 1, j1
    if i2 < len(state):
        swap(state, i1, j1, i2, j2)
        return state


def moveDown(state):
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1 - 1, j1
    if i2 >= 0:
        swap(state, i1, j1, i2, j2)
        return state


def moveLeft(state):
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1, j1 - 1
    if j2 >= 0:
        swap(state, i1, j1, i2, j2)
        return state


def moveRight(state):
    i1, j1 = getRequiredValues(state)
    i2, j2 = i1, j1 + 1
    if j2 < len(state[0]):
        swap(state, i1, j1, i2, j2)
        return state


def move(state):
    t1 = moveUp(deepcopy(state))
    t2 = moveDown(deepcopy(state))
    t3 = moveLeft(deepcopy(state))
    t4 = moveRight(deepcopy(state))

    possibleMoves = []
    for t in [t1, t2, t3, t4]:
        if t:
            possibleMoves.append(t)

    return possibleMoves
