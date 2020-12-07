import re

inputs = open("day7/input").read().splitlines()

inputs = filter(lambda x: x != "", inputs)

bags = {}

for i in inputs:
    bag = " ".join(i.split()[:2])
    bags[bag] = {}
    for match in re.finditer("([0-9]) ([^\s]+ [^\s]+)|no other bags", i):
        if match.group() == "no other bags":
            break
        count = int(match.group(1))
        bags[bag][match.group(2)] = count

def total_bags(bag_key):
    result = 0

    for key, value in bags[bag_key].items():
        result += value + value * total_bags(key)

    return result

total_count = total_bags("shiny gold")
print(total_count)