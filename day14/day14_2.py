from collections import defaultdict
import re

inputs = [line.split(" = ") for line in open("day14/input").read().splitlines()]

memory = defaultdict(lambda: 0)

def generate_combinations(mask):
    result = [""]

    for i in range(len(mask)):
        newResult = list(result)
        for r in range(len(result)):
            if mask[i] == "X":
                newResult.append(result[r] + "1")
                newResult[r] += "0"
            else:
                newResult[r] += "1"
        result = newResult




    return list(map(lambda x: int(x, 2), result))

def run():
    address_masks = []
    for i in inputs:
        if i[0] == "mask":
            #floating_bits = [i for i, x in enumerate(i[1]) if x == "X"]
            address_masks = generate_combinations(i[1])
            address_mask1 = int(i[1].replace("X", "1"), 2)
            #print(address_masks)
        else:
            address = int(re.search("mem\[(.+?)\]", i[0]).group(1))

            for address_mask in address_masks:
                memory[(address | address_mask1) & address_mask] = int(i[1])


run()
print(sum(memory.values()))