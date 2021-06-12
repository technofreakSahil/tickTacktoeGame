board =[" " for x in range(10)]

def isFreeSpace(pos):
    return board[pos]==" "
def insertLetter(letter,pos):
     board[pos]=letter
def printBoard(board):
    print("   |    |")
    print(" " + board[1] + " | " + board[2] + "  | " + board[3])
    print("   |    |")
    print("--------------")
    print("   |    |")
    print(" " + board[4] + " | " + board[5] + "  | " + board[6])
    print("   |    |")
    print("--------------")
    print("   |    |")
    print(" " + board[7] + " | " + board[8] + "  | " + board[9])
    print("   |    |")     

def isWinner(b, l):
    return (b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (
            b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or (
                       b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (
                       b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l)


def playerMove1():
    p = True
    while p:
        move = input("Player 1 please select a position to place 'X' on i.e (1-9)")
        try:
            move = int(move)
            if 0 < move < 10:
                if isFreeSpace(move):
                    p = False
                    insertLetter("X", move)
                else:
                    print("The space is full")
            else:
                print("Enter a valid position within the range")
        except:
            print("Enter a valid integer")
def playerMove2():
    p = True
    while p:
        move = input("Player 2 please select a position to place 'O' on i.e (1-9)")
        try:
            move = int(move)
            if 0 < move < 10:
                if isFreeSpace(move):
                    p = False
                    insertLetter("O", move)
                else:
                    print("The space is full")
            else:
                print("Enter a valid position within the range")
        except:
            print("Enter a valid integer")

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("Welcome to the Tic Tac Toe Game")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, "O")):
            playerMove1()
            printBoard(board)
        else:
            print("HUrray, Player 2 won the game")
            break
        if not (isWinner(board, "X")):
            playerMove2()
            printBoard(board)
        else:
            print("Hurray, Player 1 won the game")
            break
        if isBoardFull(board):
            print("Tie Game")

while  False:
     print("Play Again")
     
main()