userInput = input("Enter a list of elements separated by space!  \n")
myList = userInput.split()


print(f"Initial list is {myList}")


while True:
    
    user_input = input("Enter a element to append or enter exit to quit:   \n")

    if user_input.lower() =='exit':
        break

    myList.append(user_input)


    print(f"Updated list is {myList}")