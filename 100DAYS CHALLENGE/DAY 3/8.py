toCheck = input("Enter c to convert celsius to fahrenheit or enter f to convert fahrenheit to celsius?  \n")

if toCheck=="c":
    celsius=float(input("Enter temparature in Celsius! \n"))

    fahrenheit = (9/5 *celsius)+32
    print(f" Temp in fahrenheit is {fahrenheit}")

elif toCheck=="f":
    fahrenheit = float(input("Enter temparature in fahrenheit!  \n"))

    celsius = (fahrenheit-32)*5/9
    print(f" Temp in celsius is {celsius}")

    
else:
    print("wrong choice")
