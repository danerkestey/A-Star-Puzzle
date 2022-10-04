from math import sqrt
import numpy as np
from itertools import chain


def isSolveable(mat):
    dp = disorderParameter(mat)
    if dp % 2 == 0:
        return True
    else:
        return False

# Calculate the disorder parameter of the matrix


def disorderParameter(mat):
    count = 0
    mat1D = list(chain.from_iterable(mat))
    for i in range(len(mat1D)):
        if i + 1 < len(mat1D):
            for j in range(i + 1, len(mat1D)):
                if mat1D[i] > mat1D[j]:
                    count += 1
            count -= 1
    return count


def generateRandomMatrix(limit):
    t = int(sqrt(limit + 1))
    x = np.arange(0, limit + 1)
    np.random.shuffle(x)
    x = np.reshape(x, (t, t))
    return x


def getCorrectInput():
    num = int(input("Enter the size of the matrix: "))
    while not sqrt(num + 1).is_integer() or num < 8:
        num = int(input("Incorrect size, please try again: "))
    return num


num = getCorrectInput()
matrix = generateRandomMatrix(num)
solve = isSolveable(matrix)
while not solve:
    matrix = generateRandomMatrix(num)
    solve = isSolveable(matrix)
