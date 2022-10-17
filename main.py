from utils.generate import *
from utils.heuristics import *
from utils.move import *
from state import *
from pandas import DataFrame


def generateStates(size):
    matrices = []
    h1S, h2S, h3S, h1N, h2N, h3N = [], [], [], [], [], []
    count = 0

    while count != 2:
        randomMatrix = generateValidRandomMatrix(size)
        puzzle1 = PuzzleSolver(size, randomMatrix, "h1").solve()
        puzzle2 = PuzzleSolver(size, randomMatrix, "h2").solve()
        puzzle3 = PuzzleSolver(size, randomMatrix, "h3").solve()

        matrices.append(randomMatrix)
        h1S.append(puzzle1[0])
        h2S.append(puzzle2[0])
        h3S.append(puzzle3[0])
        h1N.append(puzzle1[1])
        h2N.append(puzzle2[1])
        h3N.append(puzzle3[1])

        count += 1
        print(count)
    df = DataFrame({'Steps h1': h1S, 'Steps h2': h2S, 'Steps h3': h3S,
                   'Nodes h1': h1N, 'Nodes h2': h2N, 'Nodes h3': h3N, })

    return {"mat": matrices, "dataframe": df}


# Get n-puzzle
n = 24
states = generateStates(n)

df = states["dataframe"]
df.to_excel('24puzzle3.xlsx', sheet_name='sheet1', index=False)
mat = states["mat"]
