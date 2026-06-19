def issafe(mat, row, col, num):
    for i in range(9):
        if mat[row][i] == num:
            return False

    for i in range(9):
        if mat[i][col] == num:
            return False

    startrow = row - (row % 3)
    startcol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if mat[i + startrow][j + startcol] == num:
                return False

    return True


def solvesudokurec(mat, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if mat[row][col] != 0:
        return solvesudokurec(mat, row, col + 1)

    for num in range(1, 10):
        if issafe(mat, row, col, num):
            mat[row][col] = num

            if solvesudokurec(mat, row, col + 1):
                return True

            mat[row][col] = 0

    return False


mat = []
for i in range(9):
    row = list(map(int, input(f"Enter row {i+1} elements: ").split()))
    mat.append(row)

if solvesudokurec(mat, 0, 0):
    print("Solved Sudoku:")
    for row in mat:
        print(*row)
else:
    print("No solution exists!")