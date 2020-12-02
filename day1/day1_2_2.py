# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)

import math

sum = 2020

inputs = set(int(line.strip()) for line in open("day1/input"))

result = math.prod(set(next(lambda x: True in (x != y and sum - x - y in inputs for y in inputs), inputs)))

print(result)
