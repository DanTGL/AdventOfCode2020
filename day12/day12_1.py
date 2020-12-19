import math

inputs = [(line[0], int(line[1:])) for line in open("day12/input").read().splitlines()]

dirs = {
    "E": [ 1, 0],
    "N": [ 0, 1],
    "W": [-1, 0],
    "S": [-1, 0]
}

dir = 0
pos = [0, 0]

for i in inputs:

    if i[0] == "L":
        dir += math.radians(i[1])
    elif i[0] == "R":
        dir -= math.radians(i[1])

    elif i[0] == "F":
        print(dir, math.cos(dir), math.sin(dir))
        pos[0] += math.cos(dir) * i[1]
        pos[1] += math.sin(dir) * i[1]
    else:
        d = dirs[i[0]]
        pos[0] += d[0] * i[1]
        pos[1] += d[1] * i[1]

print(abs(pos[0]) + abs(pos[1]))