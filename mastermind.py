"""
mastermind 
Player 1 plays first by setting a multi-digit number.
Player 2 now tries his first attempt at guessing the number.
If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! 
If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
The game continues till Player 2 eventually is able to guess the number entirely.
Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
If not, then Player 2 wins the game.
"""

from getpass import getpass
from modules.player import choose_player
from modules.check_digits import check_number
from modules.check_ans import check_answer
from modules.compare_str import compare_element
from modules.mask import mask_number


#game states  ------
#storing usernames 
player_one = input("Enter your name: ").strip()
player_two = input("Enter your name: ").strip() #remove whitespace left & right 
#not required one_name = 
#not required two_name = 

#default game starting states 
#displaying the username, locking the name in a variable to be reused 
player_list, first_player, second_player = choose_player(player_one,player_two)

current_setter = first_player #set as first player (this is a dict return  player_list = [{"name":player_a, "playerid": 1, "tries": 0}
print("Current Set",current_setter["name"])
current_guesser = second_player
guess_player = second_player #when game starts, secondplayer makes the guess 
guess_number = "" #as a string as i want to compare element individually later. 


#game starts 
while True:  #outer loop for processing game 
 # lets start with the setter first 
    print(f"{current_setter['name']},")  #event - get setter-name
    secret_number = getpass(f"enter your secret numbers, up to 4 digits: ") #event - get number
    #this validates a proper input by setter 
    secret_number = check_number(secret_number)   #event data check 
    if secret_number is None: 
        continue #continue if check_number returns None so user didnt place a correct input
    else: #proceed with the next game logic check: 
    
        total_guess = 0 #set a in-game counter of how many tries before success
        correct_number = []
        while True: #inner loop to process game guess events 
            
            print(f"{current_guesser['name']}, Make a guess!")    #event get guess
            guess_number = input("Enter your guess: ") #input data event
            guess_number = check_answer(guess_number, secret_number)#validate data event: guess_input using secret_number passed as info to check_answer()
            if guess_number is None: #if not a valid input returned by check_answer(), ask current guesser to continue input a valid answer                 
                continue    
                
            else: 
                total_guess += 1                 
                match_s, match_g, wrong_pos_secret, wrong_pos_guess  = compare_element(guess_number, secret_number) #comparing the numbers 
                if len(match_g) == 0: #if no elements match 
                    print("Unfortunately none of the numbers are correct")
                    continue #try again                                 
                
                if match_g == match_s:  #if all match, guesser win                 
                    print(f"{current_guesser['name']}, You won and took {total_guess} tries!")
                    current_guesser["tries"] += total_guess #key must be encapsulated in "tries"
                    current_guesser, current_setter = current_setter, current_guesser
                    print(f"Switching roles! {current_setter['name']}, time for you to set!\n")                
                    break #reset to outer while Loop for next setter

      
               



        

    


