import random

# list of words the game can use
word_list = ['acres', 'advice', 'Autumn', 'breeze', 'customs', 'damage', 'constantly', 'discussion', 'fireplace', 'grandmother', 'independent', 'remarkable', 'slight', 'shaking', 'thumb', 'species', 'official']
random_word = word_list[random.randrange(0, len(word_list))]
censored_word = ['_' for x in random_word]
tries = 6
letters_used = []

while True:
    print(" ".join(censored_word))
    if tries == 0:
        print(f"Game over, you're out of tries. The word was '\u001b[36m{random_word}\u001b[0m'.")
        break
    elif '_' not in censored_word:
        print("Congratulations, you won the game!")
        break

    matched_letter = False
    print(f"\u001b[32mLetters used: {', '.join(letters_used)}\u001b[0m")
    user_input = input("Type one letter: ")
    if len(user_input) > 1:
        print("\u001b[31mThat was more than one letter, try again!\u001b[0m")
        continue

    if user_input not in letters_used:
        letters_used.append(user_input)
    else:
        print("\u001b[35mYou already tried this letter, try something else!\u001b[0m")
        continue

    for index, x in enumerate(random_word):
        if x == user_input:
            censored_word[index] = x
            matched_letter = True

    if not matched_letter:
        tries -= 1
        print(f"The word does not contain this letter. \u001b[36m{tries}\u001b[0m tries left.")
