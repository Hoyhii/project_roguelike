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


def main():
    player = create_player(PLAYER_START_X,PLAYER_START_Y)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    

    util.clear_screen()
    is_running = True
    while is_running:
        board = engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
                is_running = False
        if key in ('w','a','s','d'):
            
            if key == 'w':
                player['y'] -= 1
            elif key == 'a':
                player['x'] -= 1
            elif key == 's':
                player['y'] += 1
            elif key == 'd':
                player['x'] += 1
            
            
            

            
        util.clear_screen()


if __name__ == '__main__':
    main()