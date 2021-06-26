from main import PLAYER_START_X
import random


def create_board(width, height):
    height_count = 0
    board = []  
    #width jelenti, hogy hány eleme van egy belső listának
    #height jelenti, hogy hány lista van a listában

    """ Creates a rectangle map with borders around it """
    for i in range(height):
        col = []
        width_count = 0

        for j in range(width):
            is_coorinate_on_edge = (
                height_count == 0 or 
                width_count == 0 or 
                height_count == height-1 or
                width_count == width-1
            )

            if is_coorinate_on_edge:
                col.append('#')
            else:
                col.append(" ")

            width_count += 1
            
        board.append(col)
        height_count += 1

    """ Creates a gate on the board """
    while True:
        row = random.randrange(0,height)
        col = random.randrange(0,width)

        if board[row][col] == '#':
            board[row][col] = 'G'
            break

    """ Places randomized type and amount of items on the map  """
    for i in range(random.randrange(3,6)):
        while True:
            row = random.randrange(0,height)
            col = random.randrange(0,width)

            if board[row][col] == ' ':
                random_item = get_all_items()[random.randrange(0,len(get_all_items()))]
                board[row][col] = random_item['icon']
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
    list_of_all_items = [
            {'icon':'S', 'type':'sword'},
            {'icon':'K', 'type':'key'},
            {'icon':'F', 'type':'food'},
            {'icon':'A','type':'armor'}
            ]
    return list_of_all_items