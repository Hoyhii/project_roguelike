import random

def create_board(width, height):
    board = []  #width jelenti, hogy hány eleme van egy belső listának
                 #height jelenti, hogy hány lista van a listában
    hcount = 0
    for i in range(height):
        col = []
        wcount = 0
        for j in range(width):
            if hcount == 0 or hcount == height-1 or wcount == 0 or wcount == width-1:
                col.append('i')
            else:
                col.append(" ")
            wcount += 1
        board.append(col)
        hcount += 1
    while True:
        row = random.randrange(0,height)
        col = random.randrange(0,width)
        if board[row][col] == 'i':
            board[row][col] = 'G'
            break
    return board
    pass


def put_player_on_board(board, player):
    pass