userInput = input("Enter a list of elemments separated by spaces   \n")

myList = userInput.split()

userInput = int (input("Enter a index   \n"))

try:
    element = myList[userInput]
    print(f"Element at {userInput} is {element}")
except:
    print(f"Index it out of range of the list ")


