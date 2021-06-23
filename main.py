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
        'items':{},
        'icon':'@'
    }
    return player

def no_collision(board,coordinate_y,coordinate_x):
    if board[coordinate_y][coordinate_x] == '#':
            return False
    return True

def valid_move(player,key,board):
    coordinate_x = player['x']
    coordinate_y = player['y']
    if key == 'w':
        coordinate_y -= 1
        return no_collision(board,coordinate_y,coordinate_x)
    if key == 'a':
        coordinate_x -= 1
        return no_collision(board,coordinate_y,coordinate_x)
    if key == 's':
        coordinate_y += 1
        return no_collision(board,coordinate_y,coordinate_x)
    if key == 'd':
        coordinate_x += 1
        return no_collision(board,coordinate_y,coordinate_x)
    
def main():
    player = create_player(PLAYER_START_X,PLAYER_START_Y)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    

    
    is_running = True
    while is_running:
        util.clear_screen()
        board = engine.put_player_on_board(board, player)
        ui.display_board(board)
        key = util.key_pressed()

        if key == 'q':
                is_running = False
        if key in ('w','a','s','d'):
            previous_x = player['x']
            previous_y = player['y']
            if key == 'w':
                if valid_move(player,key,board):
                    player['y'] -= 1
                else:
                    continue
            elif key == 'a':
                if valid_move(player,key,board):
                    player['x'] -= 1
                else:
                    continue
            elif key == 's':
                if valid_move(player,key,board):
                    player['y'] += 1
                else:
                    continue
            elif key == 'd':
                if valid_move(player,key,board):
                    player['x'] += 1
                else:
                    continue
            board[previous_y][previous_x] = " "
            

            
        util.clear_screen()

if __name__ == '__main__':
    main()