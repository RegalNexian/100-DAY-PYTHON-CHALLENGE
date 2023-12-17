number= int(input("Enter a number\n"))
iterations = number
factorial =1

for i in range (1, iterations):
    factorial *= number
    number -= 1

print(factorial)


    
