import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 20
BOARD_HEIGHT = 10


def create_player(role):
    if role == 'warrior':
        strength = 6 #+dmg and hp
        dexterity = 3 #dodge chance and crit (highest amount of damage)
        intelligence = 1  #spell damage (more dmg than strength damage, less than crit) and little dodge chance

        max_health = 200
        spell_damage = 0

    elif role == 'rogue':
        strength =1
        dexterity = 6
        intelligence = 3 

        max_health = 120
        spell_damage = 0

    elif role == 'mage':
        strength = 1
        dexterity = 2
        intelligence = 7

        max_health = 100
        spell_damage = 5

    player = {

            'y':PLAYER_START_Y,
            'x':PLAYER_START_X,
            'map_icon':PLAYER_ICON,

            'role': role,
            'name':'Pelőn',
            'items':[],
            
            'base_damage':5,
            'spell_damage': spell_damage,
            'base_armor':0,

            'strength' : strength,
            'dexterity': dexterity,
            'intelligence': intelligence,

            'max_health': max_health,
            'current_health': max_health,
            
            'equipped_armor' : 0,
            'equipped_weapon': 0

            }

    return player


def fight(player):
    enemy = engine.create_entity("enemy")
    is_player_won = False
    player_armor = player['base_armor'] + player['equipped_armor']['additional_armor']

    while True:
        util.clear_screen()
        print("""
    ,` -.)
   ( _/----._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()""")
        print("Player health:", player["current_health"], " dmg:", player["base_damage"], " armor:", player["base_armor"])

        print("Enemy health:", enemy["current_health"], " dmg:", enemy["base_damage"], " armor:", enemy["base_armor"])
        break

    return is_player_won ,player


def no_collision(board, y, x, player):
    is_player_on_the_gate = False

    if board[y][x] == '#':
            return  (False, board, is_player_on_the_gate)
    
    elif board[y][x] == 'G':
        if can_open_gate(player, False):
            is_player_on_the_gate = True
            return  (True, board, is_player_on_the_gate)
        else:
            return (False, board, is_player_on_the_gate)

    elif board[y][x] == 'X':
        fight(player)
        return (False, board, is_player_on_the_gate)

    elif board[y][x] == 'O':
        can_open_gate(player, True)
        is_player_on_the_gate = True
        return  (True, board, is_player_on_the_gate)

    return (True, board, is_player_on_the_gate)

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
    modified_player = check_if_entity(board, y, x, player)

    return (is_no_collision, modified_player, modified_board, check_if_o)
    

def check_if_entity(board, y, x, player):
    if board[y][x] == 'S':
        player['items'].append(engine.create_entity('sword'))

    elif board[y][x] == 'A':
        player['items'].append(engine.create_entity('armor'))

    elif board[y][x] == 'F':
        food = engine.create_entity('food')
        if(player['current_health'] + food['restore_health'] < player['max_health']):
            player['current_health'] += food['restore_health']
        else:
            player['current_health'] = player['max_health']

    elif board[y][x] == 'K':
        player['items'].append(engine.create_entity('key'))

    return player

def character_creation():
    pass


def main():
    role = character_creation()
    player = create_player('warrior')
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT) 

    is_running = True
    is_inventory_visible = False
    is_player_in_front_of_the_gate = False

    """ The main game loop """
    while is_running:
        util.clear_screen()
        board = engine.put_player_on_board(board, player)
        ui.display_board(board, player)

        key = util.key_pressed()

        """ Quit from the game """
        if key == 'q':
                is_running = False

        """ Open or close inventorz """
        if key == 'i':
            player = ui.display_stats(player)
           
                
        """ Handles the movement input """  
        if key in ('w','a','s','d'):
            previous_x = player['x']
            previous_y = player['y']
            if key == 'w':
                valid_move, player, board, is_player_on_gate = check_move(player,key,board)
                if valid_move:
                    player['y'] -= 1
                else:
                    continue
            elif key == 'a':
                valid_move, player, board, is_player_on_gate = check_move(player,key,board)
                if valid_move:
                    player['x'] -= 1
                else:
                    continue
            elif key == 's':
                valid_move, player, board, is_player_on_gate = check_move(player,key,board)
                if valid_move:
                    player['y'] += 1
                else:
                    continue
            elif key == 'd':
                valid_move, player, board, is_player_on_gate = check_move(player,key,board)
                if valid_move:
                    player['x'] += 1
                else:
                    continue

            if is_player_in_front_of_the_gate == False:
                board[previous_y][previous_x] = " "
                if is_player_on_gate == True:
                    is_player_in_front_of_the_gate = True
            else:
                board[previous_y][previous_x] = "O"
                is_player_in_front_of_the_gate = False
 
        util.clear_screen()


if __name__ == '__main__':
    main()