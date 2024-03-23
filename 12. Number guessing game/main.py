import random

answer = random.randint(1, 100)


def start_game():
    from art import logo
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        count = 5
    else:
        count = 10
    game_end = False
    while not game_end:
        print(f"you have {count} lives remaining.")
        guess = int(input("Make a guess: "))

        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        elif guess == answer:
            print(f"You got it! The answer was {answer}")
        count = count - 1

        if count == 0 or guess == answer:
            game_end = True
            if guess == answer:
                print("you win")
            else:
                print("You lose.")
        else:
            print("guess again")


start_game()
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while input("wanna play again type y ") == 'y':
    clear()
    start_game()













