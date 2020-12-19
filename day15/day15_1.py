inputs = list(map(int, open("day15/input").readline().split(",")))

def rounds():
    turns = {num: index + 1 for index, num in enumerate(inputs[:-1])}
    prev_spoken = inputs[-1]

    for i in range(len(inputs), 2020):

        if prev_spoken not in turns.keys():
            turns[prev_spoken] = i
            prev_spoken = 0
        else:
            tmp = turns[prev_spoken]
            turns[prev_spoken] = i
            prev_spoken = i - tmp
    return prev_spoken

print(rounds())