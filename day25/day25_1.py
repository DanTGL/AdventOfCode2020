from math import floor, ceil, sqrt

divisor = 20201227

# Old function to get loop size that I wrote. It works correctly but isn't very efficient
def detransform(subject_number, public_key):
    index = 0
    value = public_key
    while value != 1:
        temp = value
        value = value / subject_number
        if value != floor(value):
            value = temp + divisor
            continue

        index += 1

    return index

def discrete_log(a, b, m):

    n = int(sqrt(m) + 1)

    values = [0] * m

    for j in range(n, 0, -1):
        values[pow(a, j * n, m)] = j

    for i in range(n):

        cur = (pow(a, i, m) * b) % m
        
        if values[cur]:
            ans = values[cur] * n - i

            if ans < m:
                return ans

    raise Exception("Discrete logarithm failed!")


def transform(subject_number, loop_size):
    value = pow(subject_number, loop_size, divisor)

    return value

def handshake(card_public_key, door_public_key):
    card_loop_size = discrete_log(7, card_public_key, divisor)
    door_loop_size = discrete_log(7, door_public_key, divisor)

    card_encryption_key = transform(door_public_key, card_loop_size)
    door_encryption_key = transform(card_public_key, door_loop_size)

    if card_encryption_key != door_encryption_key:
        raise Exception(f"Encryption keys do not match\nCard encryption key: {card_encryption_key}\nDoor encryption key: {door_encryption_key}")
    return card_encryption_key

card = int(input("Card public key: "))
door = int(input("Door public Key: "))


print(handshake(card, door))
