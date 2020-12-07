import string

inputs = [line.split() for line in open("day6/input").read().split("\n\n")]

def count():
    count = 0
    for group in inputs:
        questions = string.ascii_lowercase
        for person in group:
            questions = list(filter(lambda x: x in person, questions))

        count += len(questions)

    return count

print(count())