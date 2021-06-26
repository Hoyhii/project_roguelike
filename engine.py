from main import PLAYER_START_X
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
                col.append('#')
            else:
                col.append(" ")
            wcount += 1
        board.append(col)
        hcount += 1
    while True:
        row = random.randrange(0,height)
        col = random.randrange(0,width)
        if board[row][col] == '#':
            board[row][col] = 'G'
            break
    for i in range(random.randrange(3,6)):
        while True:
            row = random.randrange(0,height)
            col = random.randrange(0,width)
            if board[row][col] == ' ':
                item = get_all_items()[random.randrange(0,len(get_all_items()))]
                board[row][col] = item['icon']
                break
    return board


def put_player_on_board(board, player):
    x = player['x']
    y = player['y']

    board[y][x] = player['icon']

    return board

def create_item(type):
    item = {}
    if type == 'sword':
        item = {'type':'sword','additional_dmg':random.randrange(2,6)}
    if type == 'key':
        item = {'type':'key'}
    if type == 'food':
        item = {'type':'food', 'restore_hp': random.randrange(10,25)}
    if type == 'armor':
        item = {'type':'armor', 'additional_armor':random.randrange(10,20)}
    return item

    
def get_all_items():
    items = [{'icon':'S', 'type':'sword'},
            {'icon':'K', 'type':'key'},
            {'icon':'F', 'type':'food'},
            {'icon':'A','type':'armor'}]
    return items