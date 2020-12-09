from random import randrange

user_input = input("Hello, would you like to play dice? (y/n)").lower()
if user_input == 'y':
    while True:
        inner_input = input(f"Your dice landed on {randrange(1,7)} and {randrange(1,7)}. Would you like to try again? (y/n)")
        if inner_input == 'y':
            continue
        else:
            break
elif user_input == 'n':
    pass
else:
    print("I'm not sure what you mean, but I'll assume you don't want to play anymore :( Goodbye.")