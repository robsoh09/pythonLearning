def check_answer(user_input, secrets):
    
    """
    helper function to validate user answer from input()
    """
       
    if not user_input.isdigit(): #checks for valid digit
      print("Please enter only numbers") 
      return None
      
    #if not  isinstance(user_input, int): # this wont work because input only outputs str and i called it before int(user_input)
     #  print("Please only enter number 1,2 or 3")
   
    if len(user_input) != len(secrets):
       print("you didn't enter the length of the guess correctly. Try again")
       return None
    
    else:
     #if valid input, proceed to mask the numbers and show onscreen
      user_input = int(user_input)    
      if 0 <= user_input <= 9999:
       user_input = str(user_input)             
       print(f"You have entered this guess: {user_input}")      
       return user_input      
