import copy
from collections import defaultdict

inputs = [list(line) for line in open("day11/input").read().splitlines()]

nodes = defaultdict(lambda: [])

for y in range(len(inputs)):
    for x in range(len(inputs[y])):
        if inputs[y][x] != ".":

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 == j and 0 == i:
                        continue

                    index_x = x + j
                    index_y = y + i
                    while 0 <= index_y < len(inputs) and 0 <= index_x < len(inputs[y]):
                        if inputs[index_y][index_x] != ".":
                            nodes[x + len(inputs[y]) * y].append((index_y, index_x))
                            break
                        index_x += j
                        index_y += i



def round(seats):
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
                    result[y][x] = "#"
                elif seats[y][x] == "#" and occupied_adjacent >= 5:
                    result[y][x] = "L"

    return result

seats = inputs
while True:
    prev_seats = copy.deepcopy(seats)

    seats = round(seats)
    if prev_seats == seats:
        break
total_occupied = 0

for y in range(len(seats)):
    for x in range(len(seats[y])):
        if seats[y][x] == "#":
            total_occupied += 1
print("Total seats occupied: " + str(total_occupied))
    