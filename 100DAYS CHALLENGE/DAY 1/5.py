number = int(input("Enter a number \n"))
sum = 0
temp = number 

while temp > 0:
    digit = temp%10
    sum+=digit
    temp//=10

print(f"the sum of digits in {number} is {sum}")