inputs = open("day13/input").read().splitlines()

start_timestamp = int(inputs[0])
bus_departures = list(map(int, filter(lambda x: x != "x", inputs[1].split(","))))

def earliest_bus(time_stamp):
    start = int(time_stamp)
    while True:
        for i in bus_departures:

            if time_stamp % i == 0:
                return (time_stamp - start) * i

        time_stamp += 1


print(earliest_bus(start_timestamp))
