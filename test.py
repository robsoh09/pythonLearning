"""1. What am I storing? 2. What just happened?3. What should change? 
   4. Do I need:
   one if/else?
   one loop?
   nested loop?
   dictionary mapping?
   state swap?

"""
"""
items  = ["apple", "banana", "orange"]
prices = [2, 3, 4]

total_price = 0
for index in range(len(items)):
    total_price += prices[index]

print(total_price)
"""
def compare_element(secret, guess):
    secret = list(secret)
    guess = list(guess)    
    for element in guess:  #for every element in 1,2,3,4 i want to compare against secret               
        if element in range(len(secret)):
            print(f"There is a {element}")


secret = "1234"
secret = list(secret)
guess = "1111"
guess = list(guess)

#pause and think about the list here. if i am comparing against two lists and they compare to each index at same time, i probably dont need a nested loop
#nested loop is designed for one index comparing against 
#i do need to compare each element to the remaining one 

#because when we guess 1111, element 0 and element 0 of both lists match first, but the other 3(1) will also hit element 0(1) and create a false positive
#therefore we need to think of incorporating a rule for this. When both side matches, we store it in a config and refer to it. for instance, if secret is matched, exclude from search 
matched_secret = []  #config list has to be outside the loop else the data keeps reset and cannot match
matched_guess = []
"""
a flag is used to describe for every search process. If not found across the list, we update the flag to False hence if not match_found: print(.....)
"""
for index in range(len(guess)): 
    match_found = False #for every search, update whether we find a match, at the end of the search, if we didnt find a match across the 4 digits 
    print(f"Matching number {index+1} value: {guess[index]}.. searching the secret list") #index + 1 since its zero-index 
    for j_index in range(len(secret)):
        """
         File "/home/robs09/python/beginner/test.py", line 41, in <module>
        if guess[index] == secret[j_index]:  
        TypeError: list indices must be integers or slices, not str
        range(len(secret)) must be used, else if we use for j_index in secret, it pulls the string "1", "2" as the index e.g secret["1"] 
        This typeError list indices must be integers refer to the above issue 
        """
        #when we find a match and the positions are not matched before: 
        if guess[index] == secret[j_index] and index not in matched_guess and j_index not in matched_secret:
            matched_secret.append(j_index)
            matched_guess.append(index)     
            match_found = True #if found updated the flag to found        
            print(f"Updated - both indexes: {index + 1} matches {j_index +1}")        
            break

    if not match_found:
       print("No match for this digit") #we print this no match print 
        
            

print(matched_guess)

   

  