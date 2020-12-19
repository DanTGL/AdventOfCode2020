from collections import defaultdict
import re

inputs = [line.split(" = ") for line in open("day14/input").read().splitlines()]

print(inputs)
memory = defaultdict(lambda: 0)

def run():
    mask1 = 0
    mask2 = 1
    for i in inputs:
        if i[0] == "mask":
            mask1 = int(i[1].replace("X", "0"), 2)
            mask2 = int(i[1].replace("X", "1"), 2)
        else:
            value = int(i[1])

            address = int(re.search("mem\[(.+?)\]", i[0]).group(1))
            memory[address] = (value | mask1) & mask2

run()
print(sum(memory.values()))