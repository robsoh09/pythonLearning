def input_validation(user_input):
    """
    helper function to validate user inputs
    Status return to the main game logic helps to end or proceed the game. 

    """
    if "," in user_input: 
      print("Please ") 
      return "retry", None # returning a status for game to continue its logic 
    
    results = user_input.split() #splitting the whitespace if there is no , detected
    
    if len(results) > 3: #len(user) checks for whitespace inclusive.. n
       #we using .split to get the numbers in a list so if len > 3 
       print("You have entered more than 3 numbers!")   
       return "loss" , None  #returning loss for the game 
    
    if "21" in user_input:
       print("21! You have lost!")
       return "endgame", None
       
    return "ok", results #if validation passes, return ok status and the results to the game
    
 

  