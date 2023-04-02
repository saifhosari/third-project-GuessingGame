import random

def guess_the_number():
    high_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        range_start = int(input("Enter the starting number of the range: "))
        range_end = int(input("Enter the ending number of the range: "))
        number = random.randint(range_start, range_end)
        guess = 0
        count = 0
        score = 0
        max_guesses = int(input("Enter the maximum number of guesses: "))

        print(f"Guess a number between {range_start} and {range_end}")

guess_the_number()