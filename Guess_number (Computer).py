import random


def computer_Guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is my guess:{guess} too high (h), too low (l) or correct(c)???: ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"I got it right, it was {guess}, computers rock!")


computer_Guess(1000)
