# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)

inputs = list(line.strip().replace(":", "").replace("-", " ") for line in open("day2/input"))

result = 0
for i in inputs:
    args = i.split()
    min, max = int(args[0]), int(args[1])
    char = args[2]

    if min <= args[3].count(char) <= max:
        result += 1

print(result)