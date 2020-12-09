import random
rge = 100
random_number = random.randrange(1, rge+1)
score = 100


def hint1():
    if random_number % 3 == 0 and random_number % 5 == 0:
        return "The random number is divisible by 3 and 5"
    elif random_number % 3 == 0:
        return "The random number is divisible by 3"
    elif random_number % 5 == 0:
        return "The random number is divisible by 5"
    else:
        return "The random number is not divisible by 3 nor 5"


hints = {
    0: hint1(),
    1: f"The number is greater than {int(rge/2)}" if random_number > rge/2 else f"The number is lower or equal to {int(rge/2)}",
    2: f"The number is close to the number {random_number + random.randrange(-10,11)}",
    3: f"The number multiplied by itself is {random_number**2}",
}
i = 0
while True:
    try:
        user_input = int(input(f"Guess a number between 1 and {rge}: "))
    except ValueError:
        print("I said a number....")
        continue

    if user_input == random_number:
        print(f"You guessed correctly! The random number was {random_number}. Your score is {score}")
        break
    elif score <= 0:
        print(f"Game Over! The random number was {random_number}")
        break
    elif i < len(hints):
        print(hints[i])
        i += 1
        score -= 10
    else:
        print("Keep guessing!")
        score -= 10
