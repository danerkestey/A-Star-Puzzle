from copy import deepcopy
from random import random
from utils.generate import *
from utils.heuristics import *
from utils.move import *
from state import *


def generateStates(size):
    steps = []
    nodes = []
    matrices = []
    count = 0

    while count != 100:
        randomMatrix = generateValidRandomMatrix(size)
        puzzle1 = PuzzleSolver(size, randomMatrix, "h1").solve()
        puzzle2 = PuzzleSolver(size, randomMatrix, "h2").solve()
        puzzle3 = PuzzleSolver(size, randomMatrix, "h3").solve()

        if puzzle1 and puzzle2 and puzzle3:
            matrices.append(randomMatrix)
            currSteps = [puzzle1[0], puzzle2[0], puzzle3[0]]
            steps.append(currSteps)

            currNodes = [puzzle1[1], puzzle2[1], puzzle3[1]]
            nodes.append(currNodes)

            count += 1
            print(count)

    return {"matrices": matrices, "steps": steps, "nodes": nodes}


# Get 8-puzzle
first = generateStates(15)
print("Puzzle            |          Steps           |        Nodes Expanded    |")
print("------------------------------------------------------------------------|")
print("                  |   h1   |   h2   |   h3   |   h1   |   h2   |   h3   |")
print("------------------------------------------------------------------------|")
for i in range(100):
    matrix = first["matrices"][i]
    step = first["steps"][i]
    node = first["nodes"][i]
    # print("{}             |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |".format(
    #     matrix, step[0], step[1], step[2], node[0], node[1], node[2]))
    # print("------------------------------------------------------------------------|")
    print("{}   {}   {}   {}   {}   {}   {} ".format(
        matrix, step[0], step[1], step[2], node[0], node[1], node[2]))
    print("------------------------------------------------------------------------|")
