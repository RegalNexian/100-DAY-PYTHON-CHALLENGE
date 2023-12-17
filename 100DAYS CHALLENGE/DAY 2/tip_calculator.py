print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?  $"))

percent = int(input("What percent tip would you like to give ? 10, 12,or 18?  "))

totalAmount = (percent/100*bill)+bill

numOfPeople=int(input("Enter the number of people to split the bill? "))

splitBillForSinglePerson = totalAmount/numOfPeople

splitBillForSinglePerson = "{:.2f}".format(splitBillForSinglePerson)

print(f"Each person to pay ${splitBillForSinglePerson}")
