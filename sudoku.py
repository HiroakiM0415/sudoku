board=9*[9*[0]]

def printBoard(board):
    for row in  board:
        for i,number in enumerate(row):
            if number==0:
                element="_"
            else:
                element=number
            if i==8:
                print(f" {element}")
            else:
                print(f" {element}", end="")

def catPutNumber(bord,range,number):
    return False

printBoard(board)