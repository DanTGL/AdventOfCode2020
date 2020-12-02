# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)
print(sum(1 if (args[3][int(args[0]) - 1] == args[2]) != (args[3][int(args[1]) - 1] == args[2]) else 0 for args in [line.replace(":", "").replace("-", " ").split() for line in open("day2/input")]))
