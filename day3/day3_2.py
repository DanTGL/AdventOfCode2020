# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)

import math
inputs = open("day3/input").read().splitlines()

def tree_encounters(slope_x, slope_y):
    result = 0
    pos_x = slope_x
    pos_y = slope_y

    while (pos_y < len(inputs)):
        if inputs[pos_y][pos_x % len(inputs[pos_y])] == "#":
            result += 1

        pos_x += slope_x
        pos_y += slope_y

    return result

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

prod = math.prod(tree_encounters(x, y) for x, y in slopes)

print(f"Total product of all slope tree encounters: {prod}")