"""
Helper function to compare elements in a Mastermind-style 4-digit string.

Pass 1:
Check correct digit + correct position.

Pass 2:
Check correct digit + wrong position.
"""

def compare_element(secret, guess):
    secret = list(secret)
    guess = list(guess)

    matched_secret = []
    matched_guess = []

    wrong_pos_secret = []
    wrong_pos_guess = []

    # -------------------------
    # PASS 1: Exact position
    # -------------------------
    # secret and guess have the same shape.
    # So one shared index can compare both lists.
    for index in range(len(guess)):
        if guess[index] == secret[index]:
            matched_secret.append(index)
            matched_guess.append(index)

            print(f"Position {index + 1}: {guess[index]} is correct and in the correct position")

    # -------------------------
    # PASS 2: Correct digit, wrong position
    # -------------------------
    # Now we only check positions that were NOT already matched in Pass 1.
    for guess_index in range(len(guess)):

        # If this guess position was already exact matched, skip it.
        if guess_index in matched_guess:
            continue

        # Search the secret list for this guessed digit.
        for secret_index in range(len(secret)):

            # If this secret position was already used, skip it.
            if secret_index in matched_secret:
                continue

            # If the digit matches here, it means:
            # correct digit, but wrong position.
            if guess[guess_index] == secret[secret_index]:
                wrong_pos_guess.append(guess_index)
                wrong_pos_secret.append(secret_index)

                # Mark this secret position as used too,
                # so another guess digit cannot reuse it.
                matched_secret.append(secret_index)
                matched_guess.append(guess_index)

                print(
                    f"Position {guess_index + 1}: {guess[guess_index]} "
                    f"is correct but in the wrong position"
                )

                # Stop searching for this guess digit once matched.
                break

    return matched_secret, matched_guess, wrong_pos_secret, wrong_pos_guess