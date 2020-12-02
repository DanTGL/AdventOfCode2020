# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)
print(sum(1 if int(args[0]) <= args[3].count(args[2]) <= int(args[1]) else 0 for args in [line.replace(":", "").replace("-", " ").split() for line in open("day2/input")]))