# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)

inputs = list(line.strip().replace(":", "").replace("-", " ") for line in open("day2/input"))

result = 0
for i in inputs:
    args = i.split()
    index1, index2 = int(args[0]) - 1, int(args[1]) - 1
    char = args[2]
    
    if (args[3][index1] == char) != (args[3][index2] == char):
        result += 1

print(result)