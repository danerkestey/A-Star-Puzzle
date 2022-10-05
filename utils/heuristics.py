from utils.generate import *


def h1(mat, size):
    # The first heuristic: Number of misplaced tiles
    hash = generateHashMatrix(mat)
    t = generateHashMatrix(generateSolvedMatrix(size))
    count = 0
    for i in hash:
        if hash[i] != t[i]:
            count += 1
    return count
