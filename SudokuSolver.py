# Stores the number of tries
tries = 0


# Is the number valid in the given position
def is_number_good(numbers, x, y):
    num = numbers[x][y]
    for i in range(9):
        if numbers[x][i] == num and i != y:
            return False
        if numbers[i][y] == num and i != x:
            return False
    for x2 in range(x - x % 3, x + 3 - x % 3):
        for y2 in range(y - y % 3, y + 3 - y % 3):
            if numbers[x2][y2] == num and x2 != x and y2 != y:
                return False
    return True


# Gets the numbers and the current position
def backtracking(numbers, x, y):
    global tries
    # Starting from the given pos, and running to the end
    while x < 9:
        while y < 9:
            # If the current pos is empty (is 0), then try putting there a number (from 1 to 9)
            if numbers[x][y] == 0:
                for i in range(1, 10):
                    tries += 1
                    numbers[x][y] = i
                    # If the number in the for loop is good, then start this function again from the next position
                    if is_number_good(numbers, x, y):
                        b = backtracking(numbers, x + int(y / 9), y % 9)
                        # If it returns with -1, then no number was good in that positoin, so try the next in the current pos
                        if b == -1:
                            numbers[x][y] = 0
                        # Else it quits from all of the backtracking functions
                        else:
                            return 1
                    # If the tried number wasnt good, then reset is to nothing
                    else:
                        numbers[x][y] = 0
                # Tried all numbers from 1 to 9, none was good. Return with -1, so tries the next number in the previous position
                return -1
            y += 1
        x += 1
        y = 0


# Prints out the sudoku
def print_sudoku(numbers):
    for x in range(9):
        for y in range(9):
            print(numbers[x][y], end='')
            if y == 2 or y == 5:
                print("|", end="")
        print()
        if x == 2 or x == 5:
            print("---+---+---")


# Opening the file containing the numbers of the sudoku, 0 means empty block
file = open("sudoku.txt", "r")
# 2D list for the numbers in the sudoku
numbers = [[0 for x in range(9)] for y in range(9)]
# Saving the numbers from the file
for i in range(9):
    row = file.readline()
    for f in range(9):
        numbers[i][f] = int(row[f])
backtracking(numbers, 0, 0)
print_sudoku(numbers)

print("\nTries: " + str(tries))
