import math

inputs = open("day13/input").read().splitlines()

bus_departures = inputs[1].split(",")

def earliest_bus():
    m = math.prod(list(map(int, filter(lambda x: x != "x", bus_departures))))
    x = 0
    for index, i in enumerate(bus_departures):
        if i == "x" or index == 0: continue

        b = int(math.floor(m / int(i)))
        x += ((-index % int(i)) * b * pow(b, -1, int(i)))

    return x % m


print(earliest_bus())