marksOfStudent= float(input("Enter your Marks! "))

if marksOfStudent>=90:
    print("Your Grade is O")

elif marksOfStudent<90 and marksOfStudent>=80:
    print("Your Grade is E")

elif marksOfStudent<80 and marksOfStudent>=70:
    print("Your Grade is A")

elif marksOfStudent<70 and marksOfStudent>=60:
    print("Your Grade is B")

elif marksOfStudent<60 and marksOfStudent>=50:
    print("Your Grade is C")

elif marksOfStudent<50 and marksOfStudent>=40:
    print("Your Grade is D")

else:
    print("You have failed the exam")


