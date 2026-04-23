"""
21 Number Game (also known as Bagram or Twenty Plus One) is a simple counting game in which players take turns to count numbers from 1 to 21. The player who calls "21" loses the game. It can be played between multiple players, but here we demonstrate a player vs computer version using Python. For Example:

Player says: 1 2
Computer says: 3 4 5
Player says: 6 7
Computer says: 8 9
...
Player says: 21

Since the Player says 21, the Player loses the game.

Game Rules
The game is played between two players who take turns one after another.
On each turn, a player can call 1 to 3 numbers.
The numbers must be consecutive (for example, 5 6 7) skipping numbers leads to disqualification.
The counting always starts from 1 and continues upward.
The one who calls 21, loses the game.

"""
from modules.validation import input_validation
from modules.player import choose_player

last_number = 0
#start with input validation first 
  

#player regisration 
player_a = input("Enter your name: ")
player_b = input("Enter your name: ")

first_player, second_player = choose_player(player_a,player_b)
#tracking player turn 
current_player = first_player
print(f"{first_player} will start first. Followed by {second_player}")
print("\nHere we go! First to 21 loses!")
#game logic 
while True: 
    
    call_numbers = input(f"{current_player}, Enter your numbers separated by spaces: ")
   
   #input validation 
    status, results = input_validation(call_numbers)

    if status == "retry":
       continue #restarts the while loop 

    if status == "lose":
        print(f"{current_player}, You entered more than 3 guesses, you lose!")
        break

    numbers = [int(value) for value in results] #converting values to int a number[]
    expected = list(range(last_number + 1, last_number + len(numbers) + 1 )) 
    #if lastnumber = 3 , using range(4,5)
    #matching to expected at least 3 consecutive numbers 
    if numbers != expected: 
        print(f"Wrong Sequence detected.")
        print(f"{current_player} loses")
        break

    last_number = numbers[-1] #get last number of numbers[] 
    if last_number == 20:
        
        if current_player == first_player:
            current_player = second_player
            
        print(f"{current_player} hits 21 and loses!")
        break

    #change current_player 
    #if its player1, convert to player2 after entering seq. 
    #else if its player2, switch to player1 
    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player
 

        
   
    

        

    
    





