predefinedEmail="p.soumyasundars@gmail.com"

predefinedPass = "030502"

eMail =input("Enter your E-mail address ? \n")

password = input("Enter your password ?  \n")

if eMail==predefinedEmail:
    if password==predefinedPass:
        print("User Authorized")
    else:
        print("Enter your Passord correctly")
else:
    print("User not authorized")

