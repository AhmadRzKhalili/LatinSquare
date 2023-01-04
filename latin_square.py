from random import randrange

n = int(input('Enter n: '))


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

def calculate_valid_values(valid_values, number, row_index, col_index):
    i = row_index
    for j in range(n):
        valid_values[i][j].remove(number)

    i = col_index
    for j in range(n):
        valid_values[j][i].remove(number)

    valid_values[row_index][col_index] = number

    return valid_values 

def calculate_mrv(valid_values):

    mrv = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(len(valid_values[i][j]))
        mrv.append(row)

    return mrv

def find_index_mrv(mrv_values):
    mrv = n
    row = 0
    col = 0

    for i in range(n):
        for j in  range(n):
            if mrv_values[i][j] < mrv:
                row = i
                col = j
                mrv = mrv_values[i][j]
    
    return row, col

row_stack = []
col_stack = []
valid_values_stack = []
latin_square_stack = []

latin_square = init_latin_square()
valid_values = init_valid_values()

mrv_values = calculate_mrv(valid_values)



