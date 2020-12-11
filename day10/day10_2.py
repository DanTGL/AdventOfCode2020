from numpy.linalg import matrix_power
import numpy as np

inputs = list(np.uint64(jolts) for jolts in open("day10/input").read().splitlines())
inputs.append(0)
inputs = sorted(inputs)

highest_joltage = max(inputs)

nodes = []
for i in range(len(inputs)):
    nodes.append([np.uint64(1) if inputs[i] < x <= inputs[i] + 3 else np.uint64(0) for x in inputs])

result = np.uint64(0)
mat = np.matrix(nodes)
for i in range(2, len(inputs) + 1):
    result += matrix_power(nodes, i).item((0, len(inputs) - 1))

print(np.uint64(result))