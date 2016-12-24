import random


def generate(length):

    result = ""
    for _ in range(1, length + 1):
        result += random.choice('01')
    return result

print(generate(64))
