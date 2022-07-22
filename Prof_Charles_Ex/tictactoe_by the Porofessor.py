import os

grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
current_player = "X"


def print_grid():
    os.system("cls")
    for row in grid:
        print(" | ".join(row))


def who_won():
    for row in grid:
        if row[0] == row[1] == row[2] != "_":
            return row[0]
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != "_":
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] != "_":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != "_":
        return grid[0][2]
    return None


def get_input():
    while True:
        user_cell = input(f"Enter the cell you want to mark (player {current_player}): ")
        try:
            user_cell = int(user_cell)
        except:
            print("Please enter a number between 1 and 9")
            continue
        if user_cell < 1 or user_cell > 9:
            print("Please enter a number between 1 and 9")
            continue
        return user_cell


def restart():
    global current_player, grid
    input("Press a key to restart")
    current_player = "X"
    grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    print_grid()


def find_cell_index_with_mapping(number):
    mapping = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    for row_index in range(len(mapping)):
        row = mapping[row_index]
        for col_index in range(len(row)):
            cell = row[col_index]
            if number == cell:
                return (row_index, col_index)


def find_cell_index_with_maths(number):
    row_index = abs(number - 9) // 3
    col_index = (number-1) % 3
    return (row_index, col_index)


print_grid()
while True:
    number = get_input()

    (row_index, col_index) = find_cell_index_with_mapping(number)
    # (row_index, col_index) = find_cell_index_with_maths(number)

    if grid[row_index][col_index] != "_":
        print("Cell already marked")
        continue

    grid[row_index][col_index] = current_player
    current_player = "X" if current_player == "O" else "O"

    print_grid()

    who = who_won()

    if who == None and not "_" in [cell for row in grid for cell in row]:
        print("No one won!")
        restart()

    if who:
        print(f"Player {who} won!")
        restart()
