import random
import time

from decoratore import measure_time

with open('file.txt', 'w') as file:
    for _ in range(100):
        file.write(f'{str(random.randint(-100, 100))}\n')


def read_ints(file):
    numbers = []
    with open('file.txt', 'r') as f:
        [numbers.append(int(x)) for x in f.readlines()]
    return numbers


@measure_time
def search_three_numbers(ints, name='t'):
    print(f'Начало {name}')
    result = 0
    n = len(ints)
    for x in range(n):
        for y in range(x + 1, n):
            for z in range(y + 1, n):
                if ints[x] + ints[y] + ints[z] == 100:
                    result += 100
    return result
