
import numpy as np

from utils.generate import generateHashMatrix, generateSolvedMatrix


def getFValue(state, g, heuristic):
    size = len(state) * len(state[0]) - 1
    h = heuristic(state, size)
    return g + h


def getManhattanDistance(state, solved):

    #by converting the array to an np array we can grab the index of a 2d array with ease
    npStateArray = np.array(state)
    npSolvedArray = np.array(solved)

    #print(npSolvedArray)
    manhattanDistances = []

    for col in range(len(npStateArray[0])):
        for row in range(len(npStateArray[0])):
            currPosition = np.argwhere(npStateArray == npStateArray[col][row])
            goalPosition = np.argwhere(npSolvedArray == npStateArray[col][row])

            #formula abs(colcurr - colgoal) + abs(rowcurr - rowgoal)
            manhattanDistances.append(abs(currPosition[0][0] - goalPosition[0][0]) + abs(currPosition[0][1] - goalPosition[0][1]))

            #print(npStateArray[col][row])
            #print(currPosition)
            #print(goalPosition)
            #print() 

    #print(manHattanDistances)
    manhattanValue = sum(manhattanDistances)
    #print(manhattanValue)
    return manhattanValue
    

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




#testing below
testState = [[1, 5, 2],
            [3, 0, 4],
            [6, 7, 8]]

solved = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

#getManhattanDistance(testState, solved)
