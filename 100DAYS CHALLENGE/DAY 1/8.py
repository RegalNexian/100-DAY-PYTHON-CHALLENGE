num1 = float(input("Enter a number\n"))

num2 = float(input("Enter a number\n"))

num3 = float(input("Enter a number\n"))

sorted_numbers = sorted([num1, num2, num3])

if sorted_numbers[1]-sorted_numbers[0]==sorted_numbers[2]-sorted_numbers[1]:
    print(f"{num1},{num2},{num3} are in ap series")
else:
    print(f"{num1},{num2},{num3} are not in ap series")

largest_number = sorted_numbers[2]
smallest_number = sorted_numbers[0]

print(f"{largest_number} is the larget number\n{smallest_number} is the smallest number")