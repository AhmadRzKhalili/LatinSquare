from random import randrange

n = int(input('Enter n: '))

def calculate_valid_values(valid_values):
    pass

def init_valid_values():
    values = [*range(1, n + 1)]
    valid_values = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(values)

        valid_values.append(row)

    return valid_values

def init_latin_square():
    latin_square = []

    for i in range(n):
        row = [0 for j in range(1, n + 1)]
        latin_square.append(row)

    return latin_square

def is_valid(valid_values):
    for i in  range(n):
        for j in range(n):
            if len(valid_values[i][j]) == 0:
                return False
    return True





