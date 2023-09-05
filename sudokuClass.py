class Sudoku:
    def __init__(self, board):
        self.board = [9*[0] for _ in range(9)]
        for k in range(9):
            self.board[k] = board[k].copy()

    def printboard(self):
        for row in self.board:
            for i, number in enumerate(row):
                if number == 0:
                    element = "_"
                else:
                    element = number
                if i == 8:
                    print(f" {element}")
                else:
                    print(f" {element}", end="")

    def putNumber(self, address, number):
        i, j = address
        self.board[i][j] = number

    def existNumberInRow(self, address, number):
        i, j = address
        if number in self.board[i]:
            return True
        else:
            return False

    def existNumberInColumn(self, address, number):
        i, j = address
        column = []
        for k in range(9):
            column.append(self.board[k][j])
        if number in column:
            return True
        else:
            return False

    def existNumberInBox(self, address, number):
        i, j = address
        box = []
        for k in range(3):
            box.extend(self.board[i-i % 3+k][j-j % 3:j-j % 3+3])
        if number in box:
            return True
        else:
            return False

    def canPutNumber(self, address, number):
        i, j = address
        if self.board[i][j] != 0:
            return False
        if self.existNumberInRow((i, j), number):
            return False
        if self.existNumberInColumn((i, j), number):
            return False
        if self.existNumberInBox((i, j), number):
            return False
        return True

    def issboardFilled(self):
        for k in range(9):
            if 0 in self.board[k]:
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
    a = Sudoku(board)
    a.printboard()
