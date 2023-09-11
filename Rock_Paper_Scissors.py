import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock, Paper, Scissors]
robot_choice = random.randint(0,2)
print("Welcome to Rock, Paper, Scissors")
User_Choice = int(input("Type 0 for Rock, 1 for Paper or for 2 Scissors \n"))
if(User_Choice > 2 or User_Choice < 0):
    print("Invalid Answer\n You Lose!")
else:
    print(game_images[User_Choice])
    Robot_Answer = game_images[robot_choice]
    print(f"The robot chose\n {Robot_Answer}")
    if (User_Choice == 0 and User_Choice ==1):
        print("You Lose!")
    elif (User_Choice == 0 and User_Choice ==0):
        print("Its A Tie!")
    elif (User_Choice == 0 and User_Choice ==2):
        print("You Win!")

    elif (User_Choice == 1 and User_Choice ==1):
        print("Its  A Tie!")
    elif (User_Choice == 1 and User_Choice ==0):
        print("You Win!")
    elif (User_Choice == 1 and User_Choice ==2):
        print("You Lose!")

    elif (User_Choice == 2 and User_Choice ==2):
        print("Its  A Tie!")
    elif (User_Choice == 2 and User_Choice ==1):
        print("You Win!")
    elif (User_Choice == 2 and User_Choice ==0):
        print("You Lose!")