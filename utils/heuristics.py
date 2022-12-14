import numpy as np


def getFValue(state, solved, heuristic, depth):
    if heuristic == "h1":
        h = h1(state, solved)
    elif heuristic == "h2":
        h = h2(state, solved)
    elif heuristic == "h3":
        h = h3(state, solved)

    f = h + depth
    return f


def h1(state, solved):
    # This heuristic is the number of tiles out of place
    # by converting the array to an np array we can grab
    # the index of a 2d array with ease
    npStateArray = np.array(state)
    npSolvedArray = np.array(solved)

    misplacedTiles = 0

    for col in range(len(npStateArray[0])):
        for row in range(len(npStateArray[0])):
            if npStateArray[col][row] != 0:
                currPosition = np.argwhere(
                    npStateArray == npStateArray[col][row])
                goalPosition = np.argwhere(
                    npSolvedArray == npStateArray[col][row])

                # formula abs(colcurr - colgoal) + abs(rowcurr - rowgoal)
                if (abs(currPosition[0][0] - goalPosition[0][0])
                        + abs(currPosition[0][1] - goalPosition[0][1])) != 0:
                    misplacedTiles += 1

    return misplacedTiles


def h2(state, solved):
    # This heuristic is the sum of the Manhattan distances
    # of each tile from its goal position
    # by converting the array to an np array
    # we can grab the index of a 2d array with ease
    npStateArray = np.array(state)
    npSolvedArray = np.array(solved)

    manhattanDistances = []

    for col in range(len(npStateArray[0])):
        for row in range(len(npStateArray[0])):
            if npStateArray[col][row] != 0:
                currPosition = np.argwhere(
                    npStateArray == npStateArray[col][row])
                goalPosition = np.argwhere(
                    npSolvedArray == npStateArray[col][row])

                manhattanDistances.append(
                    abs(currPosition[0][0] - goalPosition[0][0])
                    + abs(currPosition[0][1] - goalPosition[0][1])
                )

    manhattanValue = sum(manhattanDistances)

    return manhattanValue


def h3(state, solved):
    # This heuristic is the sum of the Euclidean distances of each
    # tile from its goal position
    # This is done by taking the sqrt of each move squared
    # ex: tile moved 1 right 1 down = sqrt(1^2 + 1^2) = sqrt(2)

    # by converting the array to an np array we can grab the index
    # of a 2d array with ease
    npStateArray = np.array(state)
    npSolvedArray = np.array(solved)

    euclideanDistances = []

    for col in range(len(npStateArray[0])):
        for row in range(len(npStateArray[0])):
            if npStateArray[col][row] != 0:
                currPosition = np.argwhere(
                    npStateArray == npStateArray[col][row])
                goalPosition = np.argwhere(
                    npSolvedArray == npStateArray[col][row])

                # formula sqrt((colcurr - colgoal)^2 + (rowcurr - rowgoal)^2)
                euclideanDistances.append(
                    np.sqrt((currPosition[0][0] - goalPosition[0][0])**2
                            + (currPosition[0][1] - goalPosition[0][1])**2)
                )

    euclideanSum = sum(euclideanDistances)

    return euclideanSum
