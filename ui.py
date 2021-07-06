import util

def display_board(board, player):
    for elem in board:
        for i in elem:
            print(i, end='')
        print('\n',end='')
    print(f"health: {player['current_health']} armor:  {player['base_armor']}")

def display_stats(player):


    line_selected = 0
    
    while True:
        util.clear_screen()

        print(f"Equipped armor: {player['equipped_armor']}")
        print(f"Equipped weapon: {player['equipped_weapon']}")
        print("health: ", player['current_health'], ", armor: ", player['base_armor'])

        counter = 0

        for item in player['items']:

            if item['type'] == 'sword':
                if line_selected == counter:
                    print(f"> type: {item['type']} damage:")
                else:
                    print(f"type: {item['type']} damage:")

            elif item['type'] == 'key':
                if line_selected == counter:
                    print(f"> type: {item['type']} damage:")
                else:
                    print(f"type: {item['type']} damage:")
            
            elif item['type'] == 'food':
                if line_selected == counter:
                    print(f"> type: {item['type']} damage:")
                else:
                    print(f"type: {item['type']} damage:")

            elif item['type'] == 'armor':
                if line_selected == counter:
                    print(f"> type: {item['type']} damage:")
                else:
                    print(f"type: {item['type']} damage:")

            else:
                print("type: " , item['type'])
            counter +=1


        key = util.key_pressed()

        if key == 'w':
            if line_selected == 0:
                continue
            elif line_selected == len(player['items']):
                counter = 0
            else:
                line_selected-=1
        elif key == 's':
            if line_selected == len(player['items'])-1:
                continue
            elif line_selected >= 0:
                line_selected+=1
        elif key == 'i':
            return player
        elif key == 'e':
            equipped = player['items'][line_selected]
            if equipped['type'] == 'armor':
               player['equipped_armor'] = equipped
            elif equipped['type'] == 'sword':
               player['equipped_weapon'] = equipped
         

        
    """ inventory_x_length = 10
    inventory_y_length = 5
    for i in range(inventory_y_length):
        for j in range(inventory_x_length):
            if(i == 0 or i == inventory_x_length-1):
                print("-", end="")
            else:
                print("|")
 """
    