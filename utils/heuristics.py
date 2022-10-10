from utils.generate import *


def h1(mat, size):
    # The first heuristic: Number of misplaced tiles
    hash = generateHashMatrix(mat)
    t = generateSolvedMatrix(size)
    count = 0
    # for i in hash:
    #     if i in t and hash[i] != t[i]:
    #         count += 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != t[i][j]:
                count += 1
    return count
