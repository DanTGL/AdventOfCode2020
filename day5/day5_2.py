rows = 128
columns = 8

seats = [int("".join("1" if i == "B" or i == "R" else "0" for i in seat), 2) for seat in open("day5/input").read().splitlines()]

def get_seat():
    for row in range(1, rows - 1):
        for col in range(columns):
            seat = row * columns + col
            if seat not in seats and seat - 1 in seats and seat + 1 in seats:
                return seat

print(get_seat())