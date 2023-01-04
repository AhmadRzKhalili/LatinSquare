from random import randrange


def init_valid_values(n):
    values = [*range(1, n + 1)]
    valid_values = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(values)

        valid_values.append(row)

    return valid_values

def init_latin_square(n):
    latin_square = []

    for i in range(n):
        row = [0 for j in range(1, n + 1)]
        latin_square.append(row)

    return latin_square

def is_valid(valid_values, n):
    for i in  range(n):
        for j in range(n):
            if len(valid_values[i][j]) == 0:
                return False
    return True

def update_valid_values(valid_values, number, row_index, col_index, n):
    
    for i in range(n):
        arr = valid_values[row_index][i].copy()
        if number in arr:
            arr.remove(number)
            valid_values[row_index][i] = arr

    for i in range(n):
        arr = valid_values[i][col_index].copy()
        if number in arr:
            arr.remove(number)
            valid_values[i][col_index] = arr

    valid_values[row_index][col_index] = []

    return valid_values 

def update_mrv_heuristic(valid_values, n):

    mrv = []


    for i in range(n):
        row = []
        for j in range(n):
            if len(valid_values[i][j]) > 0:
                row.append(len(valid_values[i][j]))
            else:
                row.append(n)

        mrv.append(row)

    return mrv

def find_index_mrv(mrv_values, n):
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

def forward_checking(latin_square, valid_values, n):
    
    for i in range(n * n):
        mrv_values = update_mrv_heuristic(valid_values, n)
        indices = find_index_mrv(mrv_values, n)
        row = indices[0]
        col = indices[1]

        valid_values_arr = valid_values[row][col]
        number = valid_values_arr[0]
        latin_square[row][col] = number

        valid_values = update_valid_values(valid_values, number, row, col, n)

    return latin_square

def print_solution(solution, n):
    for i in range(n):
        for j in range(n):
            print(solution[i][j], end=" ")

        print()


def main():
    n = int(input('Enter n: '))
    latin_square = init_latin_square(n)
    valid_values = init_valid_values(n)
    solution = forward_checking(latin_square, valid_values, n)
    print_solution(solution, n)

if __name__ == "__main__":
    main()
