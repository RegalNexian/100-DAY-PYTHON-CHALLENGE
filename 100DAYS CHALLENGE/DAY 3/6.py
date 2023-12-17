user_input = input("Enter 'yes' to continue or 'no' to stop: ")


if user_input.lower() == 'yes':
    
    while True:
        print("Message being printed...")
        next_input = input("Enter 'yes' to continue or 'no' to stop: ")
        if next_input.lower() != 'yes':
            break  
else:
    print("No message will be printed as per user input.")
