inputs = set(int(jolts) for jolts in open("day10/input").read().splitlines())

highest_joltage = max(inputs) + 3
inputs.add(highest_joltage)

jolts = 0
diffs = [0, 0, 0]

while len(inputs) != 0:
    joltage = min(inputs)
    inputs.remove(joltage)

    diff = joltage - jolts - 1

    if 0 <= diff <= 2:
        diffs[diff] += 1
        jolts = joltage

print(diffs[0], diffs[2])
print(diffs[0] * diffs[2])
