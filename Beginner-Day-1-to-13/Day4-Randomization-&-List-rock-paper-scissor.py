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

#Write your code below this line 👇

import random as rd

game_choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice > 2 or player_choice < 0:
  print("You typed an invaild number, You Lose.")
else:
  print(game_choices[player_choice])
  # if player_choice == 0:
  #   print(rock)
  # elif player_choice == 1:
  #   print(paper)
  # elif player_choice == 2:
  #   print(scissors)
  # else:
  #   print("Incorrect Input")

  # game_choices = (rock, paper, scissors)
  # random_choice = len(game_choices)
  random_comp_choice = rd.randint(0, 2)

  computer_choice = random_comp_choice

  print("Computer chose:")
  print(game_choices[computer_choice])


  if player_choice == 0 and computer_choice == 2:
    print("You Wins!")
  elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
  elif computer_choice > player_choice:
    print("You Lose!")
  elif computer_choice < player_choice:
    print("You Win!")
  elif computer_choice == player_choice:
    print("It's a draw!")

 




    