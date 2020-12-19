inputs = [line.splitlines() for line in open("day16/input").read().split("\n\n")]

values = dict()
for i in inputs[0]:
    value, ranges = i.split(": ")
    ranges = [list(map(int, num.split("-"))) for num in ranges.split(" or ")]
    values[value] = ranges
    

error_rate = 0

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
            error_rate += j
print(error_rate)
