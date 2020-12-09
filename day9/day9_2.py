inputs = [int(line) for line in open("day9/input").read().splitlines()]

prev_numbers = 25

def invalid_number():
    for i in range(prev_numbers, len(inputs)):
        invalid = True

        for j in inputs[i - prev_numbers:i]:
            
            term = inputs[i] - j
            if term in inputs[i - prev_numbers:i]:
                invalid = False
                break
            
        if invalid:
            return inputs[i]

def result():
    invalid = invalid_number()

    for i in range(len(inputs)):
        if invalid == inputs[i]:
            continue

        for j in range(i + 1, len(inputs)):
            if invalid == inputs[j]:
                break

            weakness = sum(inputs[i:j])

            if weakness == invalid:
                min_num = min(inputs[i:j])
                max_num = max(inputs[i:j])
                print(min_num, max_num)
                return f"{weakness}, {min_num + max_num}"

print(result())

