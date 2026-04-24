import random 
def choose_player(player_a, player_b):
    player_list = [{}]
    player_list = [{1:player_a}, 
                   {2: player_b}]   
 
    choice = random.choice(player_list)   
    if choice == player_list[0]: #if random choice is player a, then choice2 must be player_b 
        choice2 = player_list[1] 
    else:
        choice2 = player_list[0] #else choice2 is player_a if choice is player_b

    return choice, choice2 #return a tuple 


player_a, player_b = choose_player("Rob", "Soh")
print(player_a, player_b)

