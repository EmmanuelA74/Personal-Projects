import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a guess between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, too high!")
        elif guess < random_number:
            print("Sorry, too low!")
    print(f"Congratulations, you guessed #{random_number} right!")


guess(10)
