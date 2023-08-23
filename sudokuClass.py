def printBoard(board):
    for row in board:
        for i, number in enumerate(row):
            if number == 0:
                element = "_"
            else:
                element = number
            if i == 8:
                print(f" {element}")
            else:
                print(f" {element}", end="")


def putNumber(board, address, number):
    i, j = address
    board[i][j] = number


def existNumberInRow(board, address, number):
    i, j = address
    if number in board[i]:
        return True
    else:
        return False


def existNumberInColumn(board, address, number):
    i, j = address
    column = []
    for k in range(9):
        column.append(board[k][j])
    if number in column:
        return True
    else:
        return False


def existNumberInBox(board, address, number):
    i, j = address
    box = []
    for k in range(3):
        box.extend(board[i-i % 3+k][j-j % 3:j-j % 3+3])
    if number in box:
        return True
    else:
        return False


def canPutNumber(board, address, number):
    i, j = address
    if board[i][j] != 0:
        return False
    if existNumberInRow(board, (i, j), number):
        return False
    if existNumberInColumn(board, (i, j), number):
        return False
    if existNumberInBox(board, (i, j), number):
        return False
    return True


def isBoardFilled(board):
    for k in range(9):
        if 0 in board[k]:
            return False
    return True


if __name__ == "__main__":
    board = [
        [0, 3, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 2, 6],
        [2, 8, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 2, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [9, 0, 0, 1, 0, 0, 8, 7, 0],
        [0, 2, 0, 4, 8, 0, 0, 0, 0],
        [0, 0, 4, 0, 6, 0, 0, 1, 0]
    ]

    printBoard(board)
