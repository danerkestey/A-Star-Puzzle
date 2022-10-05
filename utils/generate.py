from math import sqrt
import numpy as np
from itertools import chain


def getEmptySpacePosition(hash):
    return hash[0]


def generateHashMatrix(mat):
    # Make a hashmap of the matrix to reduce position lookup time
    hash = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            hash[mat[i][j]] = (i, j)
    return hash


def generateValidRandomMatrix(limit):
    # Generate a valid matrix that can be solved
    matrix = generateRandomMatrix(limit)
    solve = isSolveable(matrix)
    while not solve:
        matrix = generateRandomMatrix(limit)
        solve = isSolveable(matrix)
    return matrix


def isSolveable(mat):
    # Checks to see if the matrix is solvable
    dp = disorderParameter(mat)
    if dp % 2 == 0:
        return True
    else:
        return False


def disorderParameter(mat):
    # Calculate the disorder parameter of the matrix
    count = 0
    mat1D = list(chain.from_iterable(mat))
    for i in range(len(mat1D)):
        if i + 1 < len(mat1D):
            for j in range(i + 1, len(mat1D)):
                if mat1D[i] > mat1D[j]:
                    count += 1
            count -= 1
    return count


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
    return x


def getCorrectInput():
    # Makes sure that the input is a correct number to create a valid puzzle
    num = int(input("Enter the size of the matrix: "))
    while not sqrt(num + 1).is_integer() or num < 8:
        num = int(input("Incorrect size, please try again: "))
    return num


# num = getCorrectInput()
# mat = generateValidRandomMatrix(num)
# print(mat)
# print(disorderParameter(mat))
