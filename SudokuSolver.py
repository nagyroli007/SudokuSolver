# Check the given block for possible numbers
def check_block(numbers, x, y):
    # Stores the possibility of the 9 numbers
    possible = [True, True, True, True, True, True, True, True, True]
    # Check the 9 numbers
    for i in range(1, 10):
        for r in range(9):
            # Checks the row and the column
            if numbers[x][r] == i or numbers[r][y] == i:
                possible[i - 1] = False
        # Checks in tha 3x3 area
        for x2 in range(x - x % 3, x + 3 - x % 3):
            for y2 in range(y - y % 3, y + 3 - y % 3):
                if numbers[x2][y2] == i:
                    possible[i - 1] = False
    # Counts the number of possibilities
    number_of_true = 0
    for i in range(9):
        if possible[i]:
            number_of_true += 1
    # If more than one possibility, then it cannot change the block
    if number_of_true > 1:
        return 0
    # Search, and return with the one possibility
    for i in range(9):
        if possible[i]:
            return i + 1


# First solving method. Runs through every block, and searches for block, where only one number can go
def easy_solve(numbers):
    is_there_empty = True
    # Runs until there is no empty blokc
    while is_there_empty:
        is_there_empty = False
        changed_one = False
        # Runs trough
        for x in range(9):
            for y in range(9):
                # If empty block
                if numbers[x][y] == 0:
                    # Search for possible number
                    possible = check_block(numbers, x, y)
                    # If found one, change that block
                    if possible != 0:
                        numbers[x][y] = possible
                        changed_one = True
                    # If that block cannot be changed for now, then there is one empty block for sure
                    else:
                        is_there_empty = True
        # If none of the blocks are changed then this method cannot solve the sudoku
        if not changed_one:
            print("Easy: No")
            break
    return numbers


# Prints out the sudoku
def print_sudoku(numbers):
    for x in range(9):
        for y in range(9):
            print(numbers[x][y], end='')
        print()


# Opening the file containing the numbers of the sudoku, 0 means empty block
file = open("sudoku.txt", "r")
# 2D list for the numbers in the sudoku
numbers = [[0 for x in range(9)] for y in range(9)]
# Saving the numbers from the file
for i in range(9):
    row = file.readline()
    for f in range(9):
        numbers[i][f] = int(row[f])
numbers = easy_solve(numbers)
print_sudoku(numbers)
