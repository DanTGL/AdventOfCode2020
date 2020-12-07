import string

inputs = [line.strip() for line in open("day6/input").read().split("\n\n")]

def count():
    count = 0
    for group in inputs:
        count += len(list(filter(lambda x: x in group, string.ascii_lowercase)))

    return count

print(count())