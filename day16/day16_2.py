import math
from collections import defaultdict

inputs = [line.splitlines() for line in open("day16/input").read().split("\n\n")]

values = dict()
for i in inputs[0]:
    value, ranges = i.split(": ")
    ranges = [list(map(int, num.split("-"))) for num in ranges.split(" or ")]
    values[value] = ranges
    

valid_tickets = inputs[2][1:]

for i in inputs[2][1:]:
    ticket_values = list(map(int, i.split(",")))
    
    for j in ticket_values:
        valid = False
        for k in values.values():
            for ranges in k:

                if ranges[0] <= j <= ranges[1]:
                    valid = True
                    break
            if valid:
                break
        
        if not valid:
            valid_tickets.remove(i)
            break


value_score = defaultdict(lambda: [0 for i in values])

for i in valid_tickets:
    ticket_values = list(map(int, i.split(",")))
    for j, ticket_value in enumerate(ticket_values):
        for key, value in values.items():
            for ranges in value:
                if ranges[0] <= ticket_value <= ranges[1]:
                    value_score[key][j] += 1
                    break


occupied_values = set()

result = dict()

while len(value_score) > 0:
    id = min(value_score, key=value_score.get)
    max_value = value_score[id].index(max(value_score[id]))
    max_value = 0
    last_index = 0
    for i in range(len(value_score[id])):
        if value_score[id][i] > max_value and i not in occupied_values:
            max_value = value_score[id][i]
            last_index = i

    occupied_values.add(last_index)
    result[id] = last_index
    value_score.pop(id)

print(sorted(result.items(), key=lambda x: x[1]))

indices = [index for key, index in result.items() if key.startswith("departure")]
print(indices)

ticket = inputs[1][1]
ticket_values = list(map(int, ticket.split(",")))
print(math.prod(ticket_values[index] for index in indices))
