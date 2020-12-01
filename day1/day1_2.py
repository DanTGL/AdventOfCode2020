sum = 2020

inputs = set(int(line.strip()) for line in open("day1/input"))

def result():
    for n in inputs:
        other_term = sum - n

        for n2 in inputs:
            third_term = other_term - n2

            if third_term != n2 != n and third_term in inputs:
                return n * n2 * third_term

print(result())