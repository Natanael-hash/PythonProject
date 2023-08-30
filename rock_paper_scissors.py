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

case = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
options = [rock, paper, scissors]
len_list = len(options)
random_case = random.randrange(len_list)
computer_case = options[random_case]

if case == "0" and computer_case == paper:
    print("You chose:")
    print(rock)
    print("Computer chose:")
    print(computer_case)
    print("Computer wins!")
elif case == "0" and computer_case == rock:
    print("You chose:")
    print(rock)
    print("Computer chose:")
    print(computer_case)
    print("It's draw!")
elif case == "0" and computer_case == scissors:
    print("You chose:")
    print(rock)
    print("Computer chose:")
    print(computer_case)
    print("You win!")
elif case == "1" and computer_case == scissors:
    print("You chose:")
    print(paper)
    print("Computer chose:")
    print(computer_case)
    print("Computer wins!")
elif case == "1" and computer_case == paper:
    print("You choose:")
    print(paper)
    print("Computer choose:")
    print(computer_case)
    print("It's draw!")
elif case == "1" and computer_case == rock:
    print("You chose:")
    print(paper)
    print("Computer chose:")
    print(computer_case)
    print("You win!")
elif case == "2" and computer_case == rock:
    print("You chose:")
    print(scissors)
    print("Computer chose:")
    print(computer_case)
    print("Computer wins!")
elif case == "2" and computer_case == scissors:
    print("You chose:")
    print(scissors)
    print("Computer chose:")
    print(computer_case)
    print("It's draw!")
elif case == "2" and computer_case == paper:
    print("You chose:")
    print(scissors)
    print("Computer chose:")
    print(computer_case)
    print("You win!")
else:
    print("You press an invalid character!Please select one of this number!")
        
        
        

    
    
