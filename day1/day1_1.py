sum = 2020

inputs = set(int(line.strip()) for line in open("day1/input"))

for n in inputs:
    other_term = sum - n
    
    if other_term != n and other_term in inputs:
        result = n * other_term
        print(result)
        break