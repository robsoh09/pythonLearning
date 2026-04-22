import random

actual_number = random.randint(1,100)
print("Play the Guessing Game!")
#outside of while loop 
total_guess = 0 

while True: 
    
    user_input = input("\nEnter your guess between 1 and 100: ") 
    """
    try except to validate input - if its not a whole INT tell the user
    """
    try: 
        user_input = int(user_input)

    except ValueError: 
        print("Invalid Input. Please enter a whole number.")
        continue

    total_guess += 1 #putting this year, means we increase the guess count after each attempt 
    #so if attempt 1 hits the jackpot, we will count it too!
    if user_input < actual_number:
        
        print(f"Guess {total_guess}: {user_input}--> Too small")
    elif user_input > actual_number:
        
        print(f"Guess {total_guess}: {user_input}--> Too high")
    else:
        
        print(f"Guess {total_guess}: {user_input}--> Correct!")
        print(f"Total Guesses: {total_guess}")
        break
