from random import randrange

N = int(input('Enter n: '))


def init_valid_values():
    values = [*range(1, N + 1)]
    valid_values = []

    for i in range(N):
        row = []
        for j in range(N):
            row.append(values)

        valid_values.append(row)

    return valid_values

def init_latin_square():
    latin_square = []

    for i in range(N):
        row = [0 for j in range(1, N + 1)]
        latin_square.append(row)

    return latin_square

def is_valid(valid_values):
    for i in  range(N):
        for j in range(N):
            if len(valid_values[i][j]) == 0:
                return False
    return True

def update_valid_values(valid_values, number, row_index, col_index):
    
    for i in range(N):
        arr = valid_values[row_index][i].copy()
        if number in arr:
            arr.remove(number)
            valid_values[row_index][i] = arr

    for i in range(N):
        arr = valid_values[i][col_index].copy()
        if number in arr:
            arr.remove(number)
            valid_values[i][col_index] = arr

    valid_values[row_index][col_index] = []

    return valid_values 

def update_mrv(valid_values):

    mrv = []


    for i in range(N):
        row = []
        for j in range(N):
            if len(valid_values[i][j]) > 0:
                row.append(len(valid_values[i][j]))
            else:
                row.append(N)

        mrv.append(row)

    return mrv

def find_index_mrv(mrv_values):
    mrv = N
    row = 0
    col = 0

    for i in range(N):
        for j in  range(N):
            if mrv_values[i][j] < mrv:
                row = i
                col = j
                mrv = mrv_values[i][j]
    
    return row, col

def forward_checking(latin_square, valid_values):
    
    for i in range(N*N):
        mrv_values = update_mrv(valid_values)
        indices = find_index_mrv(mrv_values)
        row = indices[0]
        col = indices[1]

        valid_values_arr = valid_values[row][col]
        number = valid_values_arr[0]
        latin_square[row][col] = number

        valid_values = update_valid_values(valid_values, number, row, col)

    return latin_square

def print_solution(solution):
    for i in range(N):
        for j in range(N):
            print(solution[i][j], end=" ")

        print()


latin_square = init_latin_square()
valid_values = init_valid_values()
solution = forward_checking(latin_square, valid_values)
print_solution(solution)

