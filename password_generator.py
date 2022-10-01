import random
from string import digits

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase_letters = uppercase_letters.lower()

digits = "123456789"

symbols = "!@#$%^&*()[]{}?></|;':.,+=-_"

upper , lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters

if nums:
    all += digits
    
if syms:
    all += symbols

lenght = 20
amount =int(input("How many passwords do you want to generate? "))

for x in range(amount):
    password = "".join(random.sample(all, lenght))
    print(password)
        
