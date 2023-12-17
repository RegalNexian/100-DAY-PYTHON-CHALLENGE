number= int(input("Enter a number \n"))
sum = 0
count =0
digit =0
temp = number
while temp > 0:
    digit=temp%10
    sum+=digit
    count+=1
    temp//=10

print(f"{number} has {count} digits and total is {sum}")
