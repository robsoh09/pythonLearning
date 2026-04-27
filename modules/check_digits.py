from modules.mask import mask_word

def check_number(user_input):
    
    """
    helper function to validate user input from input()
    input returns str ! 
    isdigit() checks for str with digits eg "7" isdigit()
    """
       
    if not user_input.isdigit(): #checks for valid digit
      print("Please enter only numbers") 
      return None
      
    #if not  isinstance(user_input, int): # this wont work because input only outputs str and i called it before int(user_input)
     #  print("Please only enter number 1,2 or 3")

     #if valid input, proceed to mask the numbers and show onscreen
    user_input = int(user_input)    
    if 0 <= user_input <= 9999:
       user_input = str(user_input)
              
       print(f"You have entered a  secret number: {mask_word(user_input)}") 
       return user_input
  