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
        while guess != number and count < max_guesses:
            count += 1
            guess = int(input("Enter your guess: "))

            if guess < number:
                print("Your guess is too low, try again.")
            elif guess > number:
                print("Your guess is too high, try again.")
            else:
                print("Congratulations, you guessed the number!")
                score = max_guesses - count
                print(f"Your score is {score}/{max_guesses}")
                if score > high_score:
                    high_score = score
                    print("New high score!")
                break

            if count == max_guesses:
                print(
                    f"You have reached the maximum number of guesses. The number was {number}.")
                break

            hint_choice = input("Would you like a hint? (y/n): ")
            if hint_choice.lower() == "y":
                if number % 2 == 0:
                    print("Hint: The number is even.")
                else:
                    print("Hint: The number is odd.")

guess_the_number()