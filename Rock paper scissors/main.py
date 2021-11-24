import random

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


comp_wins = [[0, 1], [1, 2], [2, 0]]
user_wins = [[0, 2], [1, 0], [2, 1]]
game_choice = [rock, paper, scissors]

user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for paper and 2 for Scissors\n"))
user = game_choice[user_input]
print(user)

rand_num = random.randint(0, 2)
computer = game_choice[rand_num]
print("\n\nComputer chose: \n" + computer)

winner_eval = [user_input, rand_num]
if winner_eval in comp_wins:
    print("Computer wins")
if winner_eval in user_wins:
    print("User wins")
