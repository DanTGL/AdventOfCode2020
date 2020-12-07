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

def total_bags(bags_dict, bag_key):
    if not bags_dict[bag_key]:
        return False

    for key in bags_dict[bag_key].items():
        if key == "shiny gold":
            return True
        else:
            result = total_bags(bags_dict, key)
            if result:
                return result

    return False

total_count = 0
for key in bags:
    if total_bags(bags, key):
        total_count += 1
print(total_count)