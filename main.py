import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 20
BOARD_HEIGHT = 10


def create_player():
    player = {
            'y':PLAYER_START_Y,
            'x':PLAYER_START_X,
            'race':1,
            'name':'',
            'items':[],
            'icon':PLAYER_ICON,
            'base_dmg':5,
            'base_hp':100,
            'current_hp':100,
            'base_armor':0
            }

    return player


def no_collision(board, y, x, player):
    check_if_o = False

    if board[y][x] == '#':
            return  (False, board, check_if_o)
    
    elif board[y][x] == 'G':
        if can_open_gate(player, False):
            board[y][x] = 'O'
            check_if_o = True
            return  (True, board, check_if_o)
        else:
            return (False, board, check_if_o)

    elif board[y][x] == 'O':
        can_open_gate(player, True)
        check_if_o = True
        return  (True, board, check_if_o)

    return (True, board, check_if_o)

def can_open_gate(player,is_door_opened):
    has_key=False

    if not is_door_opened:
        for item in player['items']:
            if item['type'] == 'key':
                has_key=True
                player['items'].remove(item)
    else:
        has_key=True

    return has_key
        

def check_move(player,key_pressed,board):
    x = player['x']
    y = player['y']

    if key_pressed == 'w':
        y -= 1
    elif key_pressed == 'a':
        x -= 1
    elif key_pressed == 's':
        y += 1
    elif key_pressed == 'd':
        x += 1

    is_no_collision, modified_board, check_if_o = no_collision(board, y, x, player)
    modified_player = check_if_item(board, y, x, player)

    return (is_no_collision, modified_player, modified_board, check_if_o)
    

def check_if_item(board, y, x, player):
    if board[y][x] == 'S':
        player['items'].append(engine.create_item('sword'))

    elif board[y][x] == 'A':
        player['items'].append(engine.create_item('armor'))

    elif board[y][x] == 'F':
        food = engine.create_item('food')
        if(player['current_hp'] + food['restore_hp'] < player['base_hp']):
            player['current_hp'] += food['restore_hp']
        else:
            player['current_hp'] = player['base_hp']

    elif board[y][x] == 'K':
        player['items'].append(engine.create_item('key'))

    return (player)


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT) 

    is_running = True
    is_inventory_visible = False
    check_if_next = False

    """ The main game loop """
    while is_running:
        util.clear_screen()
        board = engine.put_player_on_board(board, player)
        ui.display_board(board)
        
        if is_inventory_visible:
            ui.display_stats(player)

        key = util.key_pressed()

        """ Quit from the game """
        if key == 'q':
                is_running = False

        """ Open or close inventorz """
        if key == 'i':
            if is_inventory_visible:
                is_inventory_visible = False
            else:
                is_inventory_visible = True
                
        """ Handles the movement input """  
        if key in ('w','a','s','d'):
            previous_x = player['x']
            previous_y = player['y']
            if key == 'w':
                valid_move, player, board, check_if_o = check_move(player,key,board)
                if valid_move:
                    player['y'] -= 1
                else:
                    continue
            elif key == 'a':
                valid_move, player, board, check_if_o = check_move(player,key,board)
                if valid_move:
                    player['x'] -= 1
                else:
                    continue
            elif key == 's':
                valid_move, player, board, check_if_o = check_move(player,key,board)
                if valid_move:
                    player['y'] += 1
                else:
                    continue
            elif key == 'd':
                valid_move, player, board, check_if_o = check_move(player,key,board)
                if valid_move:
                    player['x'] += 1
                else:
                    continue
            if check_if_o == False:
                board[previous_y][previous_x] = " "
            elif board[previous_y][previous_x] == "O":
                check_if_o = True
                check_if_next = True
                continue
            else:
                check_if_next = True
                continue
            
            if check_if_next == False:
                board[previous_y][previous_x] = ' '
            else:
                board[previous_y][previous_x] = "O"
                check_if_o = False
                check_if_next = False
            
 
        util.clear_screen()


if __name__ == '__main__':
    main()