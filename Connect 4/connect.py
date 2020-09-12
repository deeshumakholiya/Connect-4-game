import numpy as np

#global variables, so that we can rid of these numbers in our code
ROW_COUNT = 5
COL_COUNT = 6

def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece #fill the baord with whatever piece player drops

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0 #the top most row is empty and user can fill bottom row first

def get_next_open_row(board, col):
    for r in range(ROW_COUNT): #range from 0 to (ROW_COUNTS -1)
        if board[r][col] == 0: #empty slot
            return r #1st instance thats empty

def print_board(board): #change the orientation of the board
    print(np.flip(board, 0)) #np command, flipping the board in x axis 

def winning_move(board, piece):
    #check horizontal location
    for c in range(COL_COUNT-3): #can only win from 1st 4 column
        for r in range (ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True


    #check vertical location for win
    for c in range(COL_COUNT):
        for r in range (ROW_COUNT-1):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #check positive slop diagonal
    for c in range(COL_COUNT-3):
        for r in range (ROW_COUNT-1):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #check negative slope diagonal
    for c in range(COL_COUNT-3):
        for r in range (1, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board() #put pieces here
print_board(board)
game_over = False #true only if gets 4 in a row
turn = 0 #differenciate whose turn


while not game_over:  
    #Ask for Player 1 Input
    if turn == 0:
        col =int(input("Player 1 your turn (0-4) :")) #get col

        if is_valid_location(board, col): #check
            row = get_next_open_row(board, col) #next empty row
            drop_piece(board, row, col, 1) #dropping piece (1 for player 1)

            if winning_move(board, 1):
                print("Player 1 wins !")
                game_over = True
    #Ask for Player 2 Input
    else:
        col = int(input("Player 2 your turn (0-4) :"))

        if is_valid_location(board, col): #same functanality
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2) #just the piece gets changed to 2


    print_board(board)

    turn += 1
    turn = turn % 2 #helps makes turn btw players