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
            is_coordinate_on_edge = (
                height_count == 0 or 
                width_count == 0 or 
                height_count == height-1 or
                width_count == width-1
            )

            if is_coordinate_on_edge:
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
    min_entities = 5
    max_entities = 8
    number_of_entities = random.randrange(min_entities,max_entities)

    for i in range(number_of_entities):
        while True:
            row = random.randrange(0,height)
            col = random.randrange(0,width)
 
            if  board[row][col] == ' ' and row != 3 and col != 3:
                if i == 0:
                    board[row][col] = get_entity('key')
                elif i < number_of_entities/3:
                    board[row][col] = get_entity('enemy')
                else:
                    random_item = get_entity('random')
                    board[row][col] = random_item['map_icon']
                break
        
    return board

def get_entity(entity):
    random_item_offset = 2

    if(entity == "key"):
        return get_all_entity()[0]['map_icon']
    elif(entity == "enemy"):
        return get_all_entity()[1]['map_icon']
    elif(entity == "random"): #random entity selection excludes the key and enemy entity
        return get_all_entity()[random.randrange(random_item_offset,len(get_all_entity()))]
    

def put_player_on_board(board, player):
    x = player['x']
    y = player['y']

    board[y][x] = player['map_icon']

    return board


def create_entity(type):
    entity = {}
    if type == 'sword':
        entity = {'type':'sword','additional_damage':random.randrange(2,6)}
    if type == 'key':
        entity = {'type':'key'}
    if type == 'food':
        entity = {'type':'food', 'restore_health': random.randrange(10,25)}
    if type == 'armor':
        entity = {'type':'armor', 'additional_armor': random.randrange(10,20)}
    if type == 'enemy':
        entity = {'type':'enemy', 'base_damage': random.randrange(10,20), 'current_health': random.randrange(150, 250), 'base_armor': random.randrange(150, 250)}
    return entity

    
def get_all_entity():
    list_of_all_entities = [
            {'map_icon':'K', 'type':'key'},
            {'map_icon':'X','type':'enemy'},
            {'map_icon':'S', 'type':'sword'},
            {'map_icon':'F', 'type':'food'},
            {'map_icon':'A','type':'armor'}
            ]
    return list_of_all_entities