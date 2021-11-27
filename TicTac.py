import random
import time

board_letters = ["A3", "A2", "A1", "B3", "B1", "B2", "C3", "C1", "C2"]
player1 = "X"
player2 = "0"
computer0 = "0"
computerx = "X"


random_moves = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
ai_last_moveX = "X"
ai_last_moveY = "0"


def init_board():
    board = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]
    return board


board = init_board()


def get_move_ai_lastmove(board, ai_last_moveX):

    list_coord_empty = []
    list_coord_full = [[[0, 0], [0, 1], [0, 2]],
              [[1, 0], [1, 1], [1, 2]],
              [[2, 0], [2, 1], [2, 2]],
              [[0, 0], [1, 0], [2, 0]],
              [[0, 1], [1, 1], [2, 1]],
              [[0, 2], [1, 2], [2, 2]],
              [[0, 0], [1, 1], [2, 2]],
              [[0, 2], [1, 1], [2, 0]]]

    for item in list_coord_full:
        counter = 0
        for n in item:
            if board[n[0]][n[1]] == ai_last_moveX:
                counter += 1
        if counter == 2:
            for n in item:
                if board[n[0]][n[1]] == '.':
                    list_coord_empty = n

    game = True
    while game:

        move = random.choice(random_moves)

        for i in move:
            list_coord_empty.append(int(i))
        x = list_coord_empty[0]
        y = list_coord_empty[1]
        if board[x][y] == ".":
            game = False

    else:

        move = []

    return tuple(list_coord_empty)


def get_move(board, player1):

    list_coord_empty = []

    keep_asking = True

    while(keep_asking == True):
        move = input(f"please player {player1} moove coord: ").upper()
        if(move == "quit" or move == "QUIT"):
            break
        while (move not in board_letters):
            move = input("please select corect coord: ").upper()
            if(move == "quit" or move == "QUIT"):
                break
        else:
            list_coord_empty = []
            for x in move:

                if(x == "a" or x == "A"):
                    x = 0
                    list_coord_empty.append(x)

                elif(x == "b" or x == "B"):
                    x = 1
                    list_coord_empty.append(x)
                elif (x == "c" or x == "C"):
                    x = 2
                    list_coord_empty.append(x)
                else:
                    list_coord_empty.append(int(x)-1)

        if(board[list_coord_empty[0]][list_coord_empty[1]] == '.'):
            keep_asking = False
        else:
            move = ""

    return tuple(list_coord_empty)


def get_move_ai(board, computer0):

    list_coord_empty = []

    keep_asking = True

    while(keep_asking == True):
        move = random.choice(board_letters)
        list_coord_empty = []
        for x in move:

            if(x == "A"):
                x = 0
                list_coord_empty.append(x)

            elif(x == "B"):
                x = 1
                list_coord_empty.append(x)
            elif (x == "C"):
                x = 2
                list_coord_empty.append(x)
            else:
                list_coord_empty.append(int(x)-1)

        if(board[list_coord_empty[0]][list_coord_empty[1]] == '.'):
            keep_asking = False
        else:
            move = ""
    return tuple(list_coord_empty)


def mark(board, player1, row, col):

    board[row][col] = player1

    return board


def has_won(board, player1):
    if board[0][0] == player1 and board[0][1] == player1 and board[0][2] == player1:
        return False
    elif board[1][0] == player1 and board[1][1] == player1 and board[1][2] == player1:
        return False
    elif board[2][0] == player1 and board[2][1] == player1 and board[2][2] == player1:
        return False
    elif board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1:
        return False
    elif board[0][0] == player1 and board[1][0] == player1 and board[2][0] == player1:
        return False
    elif board[0][1] == player1 and board[1][1] == player1 and board[2][1] == player1:
        return False
    elif board[0][2] == player1 and board[1][2] == player1 and board[2][2] == player1:
        return False
    elif board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
        return False
    else:
        return True


def is_full(board):

    if "." in board[0] or "." in board[1] or "." in board[2]:
        return False
    else:
        return True


def print_board(board):
    print("==========================================")
    print("   1  " + "   2  "+"    3  ")
    print("A  " + f"{board[0][0]} " + " |  " +
          f"{board[0][1]}" + "  |   "+f"{board[0][2]}")
    print("------+-----+------")
    print("B  " + f"{board[1][0]} " + " |  " +
          f"{board[1][1]}" + "  |   "+f"{board[1][2]}")
    print("------+-----+------")
    print("C  " + f"{board[2][0]} " + " |  " +
          f"{board[2][1]}" + "  |   "+f"{board[2][2]}")


def print_result(board):

    if(has_won(board, player1) == False):

        print(f"player {player1} has won !")
        return False
    elif(has_won(board, player2) == False):

        print(f"player {player2} has won !")
        return False
    elif(has_won(board, computerx) == False):

        print(f"player {computerx} has won !")
        return False
    elif(has_won(board, computer0) == False):

        print(f"player {computer0} has won !")
        return False
    elif(has_won(board, ai_last_moveX) == False):

        print(f"player {ai_last_moveX} has won !")
        return False
    elif(has_won(board, ai_last_moveY) == False):

        print(f"player {ai_last_moveY} has won !")
        return False
    elif is_full(board) == True:
        print("This is a Tie")
        return False
    else:
        return True


def tic_toe(x):

    if(x == 1):
        board = init_board()
        i = 0
        while i < 15:
            print_board(board)
            coord = get_move(board, player1)
            row = coord[0]
            col = coord[1]
            mark(board, computerx, row, col)
            i = i+1
            if(print_result(board) == False):
                print_board(board)
                break

            print_board(board)
            coord = get_move(board, player2)
            row = coord[0]
            col = coord[1]
            mark(board, computer0, row, col)
            i = i+1
            if(print_result(board) == False):
                print_board(board)
                break
    elif x == 2:
        board = init_board()
        i = 0
        while i < 15:
            print_board(board)
            coord = get_move(board, player1)
            row = coord[0]
            col = coord[1]
            mark(board, computerx, row, col)
            i = i+1
            time.sleep(2)
            if(print_result(board) == False):
                print_board(board)
                break

            print_board(board)
            coord = get_move_ai(board, computer0)
            row = coord[0]
            col = coord[1]
            mark(board, computer0, row, col)
            i = i+1
            if(print_result(board) == False):
                print_board(board)
                break
    elif x == 3:
        board = init_board()

        i = 0
        while i < 15:
            print_board(board)
            coord = get_move_ai(board, computerx)
            row = coord[0]
            col = coord[1]
            mark(board, computerx, row, col)
            i = i+1
            if(print_result(board) == False):
                print_board(board)
                break

            time.sleep(2)
            print_board(board)
            coord = get_move(board, player2)
            row = coord[0]
            col = coord[1]
            mark(board, computer0, row, col)
            i = i+1
            time.sleep(2)
            if(print_result(board) == False):
                print_board(board)
                break

    elif x == 4:
        board = init_board()

        i = 0
        while i < 15:
            print_board(board)
            coord = get_move_ai(board, computerx)
            row = coord[0]
            col = coord[1]
            mark(board, computerx, row, col)
            i = i+1
            if(print_result(board) == False):
                print_board(board)
                break

            time.sleep(2)
            print_board(board)
            coord = get_move_ai(board, computer0)
            row = coord[0]
            col = coord[1]
            mark(board, computer0, row, col)
            i = i+1
            time.sleep(2)
            if(print_result(board) == False):
                print_board(board)
                break
    elif x == 5:
        board = init_board()

        i = 0
        while i < 15:
            print_board(board)
            coord = get_move(board, player1)
            row = coord[0]
            col = coord[1]
            mark(board, player1, row, col)
            i = i+1
            if(print_result(board) == False):
                print_board(board)
                break

            time.sleep(1)
            print_board(board)
            coord = get_move_ai_lastmove(board, ai_last_moveX)
            row = coord[0]
            col = coord[1]
            mark(board, ai_last_moveY, row, col)
            i = i+1
            time.sleep(1)
            if(print_result(board) == False):
                print_board(board)
                break
    elif x == 6:
        board = init_board()

        i = 0
        while i < 15:
            print_board(board)
            coord = get_move_ai_lastmove(board, ai_last_moveY)
            row = coord[0]
            col = coord[1]
            mark(board, computerx, row, col)
            i = i+1
            if(print_result(board) == False):
                print_board(board)
                break

            time.sleep(2)
            print_board(board)
            coord = get_move(board, player2)
            row = coord[0]
            col = coord[1]
            mark(board, player2, row, col)
            i = i+1
            time.sleep(2)
            if(print_result(board) == False):
                print_board(board)
                break


def main_menu():
    print("Game Mode :\n", "1. Player   Vs Player \n", '2. Player   Vs Al Bundy \n', "3. Al Bundy(easy) Vs Player \n", "4. Al Bundy Vs Al Bundy \n",
          "5. Player vs Safe Al Bundy \n", "6. Al Bundy Safe vs Player ")
    x = int(input("Select 1 , 2 , 3 , 4 ,5 or 6:  "))
    tic_toe(x)


if __name__ == '__main__':
    main_menu()
