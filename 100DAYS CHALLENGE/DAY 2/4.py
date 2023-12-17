binary_digit = input("Enter a binary number \n")

if not all(bit in'01'for bit in binary_digit):
    print("Invalid Binary Number! Enter a valid binary digit")

else:
    decimal = 0
    power = len(binary_digit)-1

    for bit in binary_digit:
        if bit =='1':
            decimal+=2**power

        power-=1


print(f"The decimal equivalent of {binary_digit} is {decimal}")

