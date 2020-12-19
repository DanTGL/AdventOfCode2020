import math
import numpy as np

inputs = [(line[0], int(line[1:])) for line in open("day12/input").read().splitlines()]

dirs = {
    "E": np.array([ 1, 0]),
    "N": np.array([ 0, 1]),
    "W": np.array([-1, 0]),
    "S": np.array([0, -1])
}

def rotate(v, angle):
    result = np.array([0, 0])
    result[0] = v[0] * int(math.cos(angle)) - v[1] * int(math.sin(angle))
    result[1] = v[0] * int(math.sin(angle)) + v[1] * int(math.cos(angle))
    return result

pos = np.array([10, 1])
ship_translation = np.array([0, 0])

print(int(math.sin(math.radians(-90))), np.cos(math.radians(90)))

for i in inputs:

    if i[0] == "L":
        pos = rotate(pos, math.radians(i[1]))
    elif i[0] == "R":
        pos = rotate(pos, math.radians(-i[1]))

    elif i[0] == "F":
        ship_translation += pos * i[1]

    else:
        d = dirs[i[0]]
        pos[0] += d[0] * i[1]
        pos[1] += d[1] * i[1]

print(abs(ship_translation[0]) + abs(ship_translation[1]))