import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input("Do you want rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print('Tie! Computer chose ' + str(computer_choice))
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win! Computer chose ' + str(computer_choice))
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win! Computer chose ' + str(computer_choice))
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win! Computer chose ' + str(computer_choice))
else:
    print('You lose! Computer chose ' + str(computer_choice))