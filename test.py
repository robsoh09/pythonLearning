from modules.validation import input_validation

current_number = []
call_numbers = input("\nEnter your numbers separated by spaces: ")


#input validation 
results = ((input_validation(call_numbers)))
for value in results:
    current_number.append(value)

print(current_number)