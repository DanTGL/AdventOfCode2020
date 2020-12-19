import copy
from numpy.linalg import matrix_power
from collections import defaultdict
import numpy as np

inputs = [list(line) for line in open("day11/input").read().splitlines()]

nodes = defaultdict(lambda: [])
for y in range(len(inputs)):
    for x in range(len(inputs[y])):
        #nodes.append([np.uint64(i) for i in range(len(inputs)) if inputs[i] == "#"])

        if inputs[y][x] != ".":

            
            for i in range(y - 1, y + 2):
                if 0 <= i < len(inputs):
                    for j in range(x - 1, x + 2):
                        if x == j and y == i:
                            continue
                        if 0 <= j < len(inputs[i]):
                        
                            if inputs[i][j] == ".":
                                continue
                            nodes[x + len(inputs[y]) * y].append((i, j))

def round(seats):
    total_changed = 0
    result = copy.deepcopy(seats)
    for y in range(len(seats)):
        for x in range(len(seats[y])):

            if seats[y][x] != ".":
                occupied_adjacent = 0
                for node in nodes[x + len(seats[y]) * y]:
                    neighbour = seats[node[0]][node[1]]

                    if neighbour == "#":
                        occupied_adjacent += 1

                if seats[y][x] == "L" and occupied_adjacent == 0:
                    total_changed += 1
                    result[y][x] = "#"
                elif seats[y][x] == "#" and occupied_adjacent >= 4:
                    total_changed += 1
                    result[y][x] = "L"
    if total_changed == 0:
        raise Exception
    return result

seats = inputs
try:
    while True:
        seats = round(seats)
except Exception:
    total_occupied = 0
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if seats[y][x] == "#":
                total_occupied += 1
    print("Total seats occupied: " + str(total_occupied))
