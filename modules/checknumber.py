def check_number(user_input):
    """
    helper function to validate user choice of 1 ,2 ,3 from input()
    input returns str ! 
    isdigit() checks for str with digits eg "7" isdigit()
    """
   
    if "," in user_input: 
      print("Please enter 1, 2 or 3") 
      return None #return 

    if not user_input.isdigit(): #checks for valid digit
      print("Please enter 1, 2 or 3") 
      return None
      
    #if not  isinstance(user_input, int): # this wont work because input only outputs str and i called it before int(user_input)
     #  print("Please only enter number 1,2 or 3")
    
    if user_input not in ["1","2","3"]:
       print("Please enter 1, 2 or 3") 
       return None 

    user_input = int(user_input) #return int to function caller 
    return user_input

  