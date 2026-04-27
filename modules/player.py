import random 
"""
player selection updated with key:pair dict in a list. 
This provides an easier route to collect players, give them an number and compare them even if the name is the same. 
main.py needs to change to reflect the output change. 

choose_player updates the player names 
"""
def choose_player(player_a, player_b):
    #player_list = [{}] define as a list with dict
    player_list = [{"name":player_a, "playerid": 1, "tries": 0},                    
                   {"name":player_b, "playerid": 2, "tries": 0}]   
 
    choice = random.choice(player_list)   
    if choice == player_list[0]: #if random choice is player a, then choice2 must be player_b 
        choice2 = player_list[1] 
    else:
        choice2 = player_list[0] #else choice2 is player_a if choice is player_b

    return player_list, choice, choice2 #return a tuple 

