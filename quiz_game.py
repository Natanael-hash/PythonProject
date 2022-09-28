print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("Whats does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    
answer = input("What is GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    
answer = input("What is RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    
answer = input("What is PSU stand for? ")

if answer.lower() == "power supply unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    
print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4) * 100) + "%.")
