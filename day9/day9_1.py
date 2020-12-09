inputs = [int(line) for line in open("day9/input").read().splitlines()]

prev_numbers = 25

def result():
    for i in range(prev_numbers, len(inputs)):
        invalid = True

        for j in inputs[i - prev_numbers:i]:
            
            term = inputs[i] - j
            if term in inputs[i - prev_numbers:i]:
                invalid = False
                break
            
        if invalid:
            return inputs[i]

print(result())
