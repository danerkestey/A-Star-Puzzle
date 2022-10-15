from math import sqrt
import numpy as np
from itertools import chain


def generateValidRandomMatrix(limit):
    # Generate a valid matrix that can be solved
    mat = generateRandomMatrix(limit)
    dp = disorderParameter(mat)
    N = len(mat)

    if N % 2 == 1:
        while not isSolvable(mat):
            mat = generateRandomMatrix(limit)
            dp = disorderParameter(mat)
    else:
        while isSolvable(mat):
            mat = generateRandomMatrix(limit)
            dp = disorderParameter(mat)

    print(dp)
    return mat


def isSolvable(puzzle):
    N = len(puzzle)
    dp = disorderParameter(puzzle)

    if N % 2 == 1:
        return dp % 2 == 0
    else:
        pos = findXPosition(puzzle)
        if pos % 2 == 1:
            return dp % 2 == 0
        else:
            return dp % 2 == 1


def findXPosition(puzzle):
    N = len(puzzle)
    # start from bottom-right corner of matrix
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if (puzzle[i][j] == 0):
                return N - i


def disorderParameter(mat):
    # Calculate the disorder parameter of the matrix
    N = len(mat)
    arr = list(chain.from_iterable(mat))
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
            # count pairs(arr[i], arr[j]) such that
            # i < j and arr[i] > arr[j]
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count += 1

    return inv_count


def generateSolvedMatrix(limit):
    # Generate a solved nxn matrix
    t = int(sqrt(limit + 1))
    x = np.arange(0, limit + 1)
    x = np.reshape(x, (t, t))
    return x


def generateRandomMatrix(limit):
    # Generate a random nxn matrix
    t = int(sqrt(limit + 1))
    x = np.arange(0, limit + 1)
    np.random.shuffle(x)
    x = np.reshape(x, (t, t))
    return x.tolist()


def getCorrectInput():
    # Makes sure that the input is a correct number to create a valid puzzle
    num = int(input("Enter the size of the matrix: "))
    while not sqrt(num + 1).is_integer() or num < 8:
        num = int(input("Incorrect size, please try again: "))
    return num


def printBoard(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print('{}'.format(j), end='\t')
            print()
    return


def printBoardString(matrix):
    text = ''
    # traverse the matrix and append the char
    for i in matrix:
        for j in i:
            text += str(j)
            text += '\n'
        text += '\n'
    return text


#### Testing ####
# num = getCorrectInput()
# mat = generateValidRandomMatrix(num)
# print(mat)
# print(disorderParameter(mat))
