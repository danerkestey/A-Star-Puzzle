import numpy as np

def getFValue(state, solved):

    #by converting the array to an np array we can grab the index of a 2d array with ease
    npStateArray = np.array(state)
    npSolvedArray = np.array(solved)

    #print(npSolvedArray)
    manhattanDistances = []
    misplacedTiles = 0

    for col in range(len(npStateArray[0])):
        for row in range(len(npStateArray[0])):
            if npStateArray[col][row] != 0:
                currPosition = np.argwhere(npStateArray == npStateArray[col][row])
                goalPosition = np.argwhere(npSolvedArray == npStateArray[col][row])

                #formula abs(colcurr - colgoal) + abs(rowcurr - rowgoal)
                if (abs(currPosition[0][0] - goalPosition[0][0]) + abs(currPosition[0][1] - goalPosition[0][1])) != 0:
                    misplacedTiles += 1 

                manhattanDistances.append(abs(currPosition[0][0] - goalPosition[0][0]) + abs(currPosition[0][1] - goalPosition[0][1]))

    manhattanValue = sum(manhattanDistances)
    return manhattanValue + misplacedTiles
    

#### testing below ####
""" testState = [[1, 5, 2],
            [3, 0, 4],
            [6, 7, 8]]

solved = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

DEFAULT_GAME2 = [[7, 2, 4],
                [5, 0, 6],
                [8, 3, 1]]

getFValue(DEFAULT_GAME2, solved) """
