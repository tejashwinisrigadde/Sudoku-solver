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
            if mat[i + startrow][j + startcol] == num:
                return False

    return True


def solvesudokurec(mat, row, col):
    # Base case: Sudoku solved
    if row == 8 and col == 9:
        return True

    # Move to next row
    if col == 9:
        row += 1
        col = 0

    # Skip filled cells
    if mat[row][col] != 0:
        return solvesudokurec(mat, row, col + 1)

    # Try numbers 1 to 9
    for num in range(1, 10):
        if issafe(mat, row, col, num):
            mat[row][col] = num

            # Recur for next cell
            if solvesudokurec(mat, row, col + 1):
                return True

            # Backtrack
            mat[row][col] = 0

    return False


print("Enter ZERO for empty cells!\n")

mat = []
for i in range(9):
    row = list(map(int, input(f"Enter row {i + 1} elements: ").split()))
    mat.append(row)

if solvesudokurec(mat, 0, 0):
    print("\nSolved Sudoku:")
    for row in mat:
        print(*row)
else:
    print("No solution exists!")