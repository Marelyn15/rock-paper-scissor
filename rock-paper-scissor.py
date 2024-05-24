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
answer = 0
while answer == 0:
    try:
        #Write your code below this line 👇
        elements = [rock, paper, scissors]
        print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
        user_choice = int(input())
        print(elements[user_choice])
        computer_choice = random.choice(elements)
        print("Computer chose",computer_choice)


        #-----------------ROCK-----------------------------
        if user_choice == 0:
            if computer_choice == elements[0]:
                print("It's a draw")
            elif computer_choice == elements[1]:
                print("You lose")
            else:
                print("You win")
        #------------------PAPER----------------------------
        elif user_choice == 1:
            if computer_choice == elements[0]:
                print("You win")
            elif computer_choice == elements[1]:
                print("It's a draw")
            else:
                print("You lose")
        #------------------SCISSORS---------------------------
        elif user_choice == 2:
            if computer_choice == elements[0]:
                print("You lose")
            elif computer_choice == elements[1]:
                print("You win")
            else:
                print("It's a draw")
    except:
        print("You put an invalid number, so you lose")
    #----------------------START AGAIN----------------------------------
    answer = input("Do you want to play again? Y/n ").lower()
    if answer == "y":
        answer = 0
    else:
        answer += 1

