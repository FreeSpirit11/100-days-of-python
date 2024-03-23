rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Welcome to Mansi's Rock Paper Scissors game\n")

choices = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

play = True

while play:
    user_choice = input("What do you want? Type rock, paper, or scissors: ").lower()

    if user_choice in choices:
        print("Computer chose:")
        computer_choice = random.choice(list(choices.values()))
        print(computer_choice)

        print("You chose:")
        print(choices[user_choice])

        if user_choice == "rock" and computer_choice != rock:
            if computer_choice == scissors:
                print("You win.")
            else:
                print("You lose.")
        elif user_choice == "paper" and computer_choice != paper:
            if computer_choice == rock:
                print("You win.")
            else:
                print("You lose.")
        elif user_choice == "scissors" and computer_choice != scissors:
            if computer_choice == paper:
                print("You win.")
            else:
                print("You lose.")
        else:
            print("No one wins.")

        play_again = input("\nIf you want to play again, type 'yes': ")
        if play_again.lower() == "yes":
            play = True
        else:
            play = False
    else:
        print("Invalid input. Please type again.")


