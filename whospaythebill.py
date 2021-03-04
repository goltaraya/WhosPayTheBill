import random
import time

print("Who's paying the bill?")
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

group_lenght = len(names)

choice = random.randint(0,group_lenght)

print(f"{names[choice]} will pay the bill today!")

time.sleep(5)

# This could be solved by changing the len() to random.choice(). 
# Btw, it's just to exercise the brain and programming logic. 
# I hope you like this and don't be choosen to pay the bill :p hehe