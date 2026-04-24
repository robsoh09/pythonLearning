"""
Winning Rules as follows:
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins

"""
"""
two players will input their choice of Rock Scissor Stone 

"""
from modules.player import choose_player
from modules.checknumber import check_number 
#player regisration 
player_a = input("Enter your name: ").strip()
player_b = input("Enter your name: ").strip()
"""
using the name in player_x causes a bug where both usernames are the same. 
in this case we can actually use index to represent the users

The bug issue happens when the name is used in comparison 
first_player = player_a and player_b has the same name the loop if else player keeps looping...
  

"""

first_player, second_player = choose_player(player_a,player_b)
first_choice = 0 
second_choice = 0
player_a_sign = ""
player_b_sign = ""
#tracking player turn 
current_player = first_player
print(f"{first_player} will start first. Followed by {second_player}")

while True: #condition if game is in play 
    #Game will run 
    #collect input from first player 
    
    print("Enter 1 for Rock, 2 for Scissors, 3 for Paper: ")
    choice = input(f"{current_player}, Enter your choice: ").strip() #strip whitespace left and right 
    
    response = check_number(choice)  #store choice after validation completed      
    print(f"{current_player} has entered {response}")
    
    #switch player state into player 2 
    if current_player == first_player:
        first_choice = response #update player choice state into first_choice variable 
        current_player = second_player
        print(first_player, first_choice)
    
    else:
        current_player == second_player
        second_choice = response
        print(second_player, second_choice)
        break

signs = {

1: "Rock",
2: "Scissors",
3: "Paper"

}

player_a_sign = signs[first_choice] 
print(player_a_sign)
player_b_sign = signs[second_choice]
print(player_b)

comparison = {

"Rock":"Scissors", 
"Scissors": "Paper",
"Paper":"Rock"

}
#using mappings below 


"""
When many if statements are checking exact values, we can use dictionary to attempt to 

using the mappings the signs are mapped to the choices. 
1:Rock for example. since its a dictionary, i can use the call out to compare 
the signs here rock:scissors is a mapping of who wins e.g rock wins scissors scissors win rock 

so when comparison[player_a_sign] == play_b_sign 
it is using the sign mapping of player a eg "Rock" will map to comparison dict row 1 "rock": "scissors" this will compare to a win and declare 
winner for that player

next work - helper functions optimization 
"""
if player_a_sign == player_b_sign:
    print("Draw Game! ")
elif comparison[player_a_sign] == player_b_sign:
    print(f"{player_a} has {player_a_sign}, {player_b}, {player_b_sign}, {player_a} wins! ")
else: 
    print(f"{player_b} has {player_b_sign}, {player_a}, {player_a_sign}, {player_b} wins! ")

