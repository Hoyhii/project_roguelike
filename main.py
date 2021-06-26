import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 20
BOARD_HEIGHT = 10


def create_player(PLAYER_START_X,PLAYER_START_Y):
    player = {
        'y':PLAYER_START_Y,
        'x':PLAYER_START_X,
        'race':1,
        'name':'',
        'items':[],
        'icon':'@',
        'base_dmg':5,
        'base_hp':100,
        'current_hp':100,
        'base_armor':0
    }
    return player


def no_collision(board,coordinate_y,coordinate_x):
    if board[coordinate_y][coordinate_x] == '#':
            return False
    return True


def check_move(player,key_pressed,board):
    coordinate_x = player['x']
    coordinate_y = player['y']
    if key_pressed == 'w':
        coordinate_y -= 1
    elif key_pressed == 'a':
        coordinate_x -= 1
    elif key_pressed == 's':
        coordinate_y += 1
    elif key_pressed == 'd':
        coordinate_x += 1
    return (no_collision(board,coordinate_y,coordinate_x), check_if_item(board, coordinate_y, coordinate_x, player))
    

def check_if_item(board, coordinate_y, coordinate_x, player):
    if board[coordinate_y][coordinate_x] == 'S':
        player['items'].append(engine.create_item('sword'))
    if board[coordinate_y][coordinate_x] == 'A':
        player['base_armor']+=engine.create_item('armor')['additional_armor']
        #player['armor'].append(engine.create_item('armor'))
    if board[coordinate_y][coordinate_x] == 'F':
        food = engine.create_item('food')
        if(player['current_hp'] + food['restore_hp'] < player['base_hp']):
            player['current_hp'] += food['restore_hp']
        else:
            player['current_hp'] = player['base_hp']
    if board[coordinate_y][coordinate_x] == 'K':
        player['items'].append(engine.create_item('key'))
    return player


def main():
    player = create_player(PLAYER_START_X,PLAYER_START_Y)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    

    
    is_running = True
    is_inventory_visible = False
    while is_running:
        util.clear_screen()
        board = engine.put_player_on_board(board, player)
        ui.display_board(board,player)
        if is_inventory_visible:
            ui.display_stats(player)
        key = util.key_pressed()

        if key == 'q':
                is_running = False
        if key == 'i':
            if is_inventory_visible:
                is_inventory_visible = False
            else:
                is_inventory_visible = True
        if key in ('w','a','s','d'):
            previous_x = player['x']
            previous_y = player['y']
            if key == 'w':
                valid_move, player = check_move(player,key,board)
                if valid_move:
                    player['y'] -= 1
                else:
                    continue
            elif key == 'a':
                valid_move, player = check_move(player,key,board)
                if valid_move:
                    player['x'] -= 1
                else:
                    continue
            elif key == 's':
                valid_move, player = check_move(player,key,board)
                if valid_move:
                    player['y'] += 1
                else:
                    continue
            elif key == 'd':
                valid_move, player = check_move(player,key,board)
                if valid_move:
                    player['x'] += 1
                else:
                    continue
            board[previous_y][previous_x] = " "
            

            
        util.clear_screen()

if __name__ == '__main__':
    main()