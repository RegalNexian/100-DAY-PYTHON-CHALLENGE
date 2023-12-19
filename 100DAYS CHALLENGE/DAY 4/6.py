import random

userInput = input ("Enter a lst a element separated by space!   \n")

myList = userInput.split()

random.shuffle(myList)

print(myList)