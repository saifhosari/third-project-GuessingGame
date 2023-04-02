import random


def guess_the_number():
    """
    Get starting and ening number.
    Run a while loop to play again when it is over and start the game anyways,
    work on Hints and help the player with odd and even numbers
    to make it easier.
    work on play again input.
    """
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
                print(f"You have reached the maximum number of guesses.\nthe number was {number}.")
                break

            hint_choice = input("Would you like a hint? (y/n): ")
            if hint_choice.lower() == "y":
                if number % 2 == 0:
                    print("Hint: The number is even.")
                else:
                    print("Hint: The number is odd.")

        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() == "no":
            print(f"Thanks for playing! Your high score was {high_score}.")


guess_the_number()
print("****************************")
