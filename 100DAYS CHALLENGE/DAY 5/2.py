num = int(input("Enter a non-negative integer: "))

result=1

for i in range(num):
    result *=num
    num-=1

print(result)