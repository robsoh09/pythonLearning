import random 
def choose_player(player_a, player_b):
    player_list = []
    player_list.append(player_a)
    player_list.append(player_b)

    choice = random.choice(player_list)    
    if choice == player_a: #if random choice is a, then choice2 must be player_b 
        choice2 = player_b 
    else:
        choice2 = player_a #else choice2 is player_a if choice is player_b 

    return choice, choice2 #return a tuple 



