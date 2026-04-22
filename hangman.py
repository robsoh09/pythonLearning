"""
How the Game Works
The program randomly selects a word from a list of secret words.
The player has limited chances to guess the word.
When a correct letter is guessed, it is revealed in its correct position.
The player wins if all letters are guessed before running out of chances.
For simplicity, the program gives word length + 2 chances.
Example: If the secret word is mango (5 letters), the player gets 7 chances.

"""
import random
def mask_word(word):
    
    return "*" * len(word)
    #replace the word with * by using the len of the word and multiply by len    



word_list = ["word", "sleepy", "happy", "money", "cheapo", "cooked", "bombastic"]

selected_word = (random.choice(word_list)) #random.choice from the list 
masked_word = mask_word(selected_word)
unmask_word = list(masked_word) #wrapping [masked_word] results in a single element ***** we want it to *, *, *, *, s
#this allows us to update the word everytime if we get it right. 
print(unmask_word)
chances = len(selected_word) + 2 

print("Welcome to the Hangman Game!")
print("This is a word guessing game.")
print(f"This is a {len(selected_word)} letters word")
print(f"You have {chances} chances to guess the word.")

while chances > 0:  #flag chance condition using chances

    letter = input("\nGuess the letters of the word: ").lower()
    if len(letter) == 1 and letter.isalpha() and chances > 0:
        chances -= 1
        print(f"You have {chances} tries left")

        if letter in selected_word: 
          for index, char in enumerate(selected_word):
                if char == letter:
                    unmask_word[index] = letter
                    #print("".join(unmask_word))  printing here will show two times if a letter appears twice
          print("".join(unmask_word)) #printing here shows the final output (outside of loop)

          final_word = "".join(unmask_word)
          if final_word == selected_word:
             print(f"You guessed the word and won! Word: {final_word}")
             break                                         

        else:
          print("You entered a wrong guess")                  
        

    else: 
        print("Please only enter single letter")
        
else: 
    print("No more chances!")
    print("game over")
    
        
