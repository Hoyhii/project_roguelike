def display_board(board):
    for elem in board:
        for i in elem:
            print(i, end='')
        print('\n',end='')


def display_stats(player):
    print("hp: ", player['current_hp'], ", armor: ", player['base_armor'])
    for item in player['items']:
        if(item['type'] == 'sword'):

            #TODO

            print("type: " , item['type'], ", damage:")
        else:
            print("type: " , item['type'])
        
    """ inventory_x_length = 10
    inventory_y_length = 5
    for i in range(inventory_y_length):
        for j in range(inventory_x_length):
            if(i == 0 or i == inventory_x_length-1):
                print("-", end="")
            else:
                print("|")
 """
    