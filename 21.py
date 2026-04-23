import random

def choose_player(player_a, player_b):
    if random.choice([True, False]):
        return player_a, player_b
    else:
        return player_b, player_a


def input_validation(user_input):
    if "," in user_input:
        print("Please use spaces, not commas.")
        return "retry", None

    results = user_input.split()

    if len(results) > 3:
        return "lose", None

    return "ok", results


player_a = input("Enter player A name: ")
player_b = input("Enter player B name: ")

first_player, second_player = choose_player(player_a, player_b)
current_player = first_player
last_number = 0

print(f"{first_player} starts first. {second_player} goes second.")

while True:
    call_numbers = input(f"\n{current_player}, enter 1 to 3 consecutive numbers: ")

    status, results = input_validation(call_numbers)

    if status == "retry":
        continue

    if status == "lose":
        print(f"{current_player} entered more than 3 numbers and loses.")
        break

    numbers = [int(value) for value in results]

    expected = list(range(last_number + 1, last_number + len(numbers) + 1))

    if numbers != expected:
        print(f"Wrong sequence. You should have entered: {expected}")
        print(f"{current_player} loses.")
        break

    last_number = numbers[-1]
    print(f"Last number is now {last_number}")

    if last_number >= 21:
        print(f"{current_player} said 21 and loses.")
        break

    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player