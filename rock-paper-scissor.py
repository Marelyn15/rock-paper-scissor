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
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
elements = [rock, paper, scissors]
computer_choice = random.choice(elements)


#-----------------ROCK-----------------------------
if user_choice == 0:
    print("Computer chose",computer_choice)
    print("Your chose",rock)
    if computer_choice == computer_choice[0]:
        print("Tie")
    elif computer_choice == computer_choice[1]:
        print("You lose")
    else:
        print("You win")
#------------------PAPER----------------------------
elif user_choice == 1:
    print("Computer chose",computer_choice)
    print("Your chose",paper)
    if computer_choice == computer_choice[0]:
       print("You win")
    elif computer_choice == computer_choice[1]:
         print("Tie")
    else:
        print("You lose")
#------------------SCISSORS---------------------------
elif user_choice == 2:
    print("Computer chose",computer_choice)
    print("Your chose",scissors)
    if computer_choice == computer_choice[0]:
        print("You lose")
    elif computer_choice == computer_choice[1]:
        print("You win")
    else:
        print("Tie")
#------------------SCISSORS---------------------------
else:
    print("You put an invalid number, so you lose")