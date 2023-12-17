weight = int(input("Enter your Weight \n"))

height = int(input("Enter your Height \n"))

bmi=(weight**2)/(height)

print(bmi)

if bmi <= 18.28678:
    print("You are underweight")

elif bmi>= 18.28678 and bmi < 28.50572:
    print("You have a normal weight")

elif bmi >=28.50572 and bmi < 32.56189:
    print("You are slighty overweight")

elif bmi >=32.56189 and bmi< 37.500000:
    print("You are obese")

else:
    print("You are clinically obese")