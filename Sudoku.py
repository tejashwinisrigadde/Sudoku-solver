def issafe(mat, row, col, num):

    # Check row
    for i in range(9):
        if mat[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if mat[i][col] == num:
            return False

    # Check 3x3 subgrid
    startrow = row - (row % 3)
    startcol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if mat[startrow + i][startcol + j] == num:
                return False

    return True


def solvesudokurec(mat, row, col):

    # Reached end of board
    if row == 8 and col == 9:
        return True

    # Move to next row
    if col == 9:
        row += 1
        col = 0

    # Skip filled cells
    if mat[row][col] != 0:
        return solvesudokurec(mat, row, col + 1)

    # Try numbers 1-9
    for num in range(1, 10):

        if issafe(mat, row, col, num):

            mat[row][col] = num

            if solvesudokurec(mat, row, col + 1):
                return True

            # Backtrack
            mat[row][col] = 0

    return False


def solvesudoku(mat):
    return solvesudokurec(mat, 0, 0)


mat = [
    [0, 0, 5, 0, 0, 7, 6, 3, 0],
    [6, 0, 9, 0, 4, 0, 0, 0, 0],
    [2, 0, 0, 0, 1, 8, 0, 9, 5],

    [1, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 9, 1, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 8],

    [7, 6, 0, 8, 3, 0, 0, 0, 9],
    [0, 0, 0, 0, 9, 0, 3, 0, 6],
    [0, 4, 3, 7, 0, 0, 8, 0, 0]
]

if solvesudoku(mat):
    print("Solved Sudoku:\n")
    for row in mat:
        print(*row)
else:
    print("No solution exists")