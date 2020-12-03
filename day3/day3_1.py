# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)

inputs = open("day3/input").read().splitlines()

result = 0
pos_x = 0

for pos_y in range(1, len(inputs)):
    pos_x += 3
    if inputs[pos_y][pos_x % len(inputs[pos_y])] == "#":
        result += 1

print(f"Total trees encountered: {result}")
