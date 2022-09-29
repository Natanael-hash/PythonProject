import random

while True:
    print(random.randint(1, 6))
    another_role = input("Want to roll the dice again (y/n)? ").lower()
    if another_role == "y":
        continue
    else:
        break
    
print("See you later!")
    