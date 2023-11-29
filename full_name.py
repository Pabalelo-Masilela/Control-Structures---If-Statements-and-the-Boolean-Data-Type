full_name = input("Enter your full name: ")
char_legnth = int(len(full_name))
if char_legnth == 0:
    print("You have not entered anything. Please enter your name.")
if char_legnth > 0 and char_legnth < 4:
    print("You have entered less than 4 charecters.Please make sure that you have entered your name and surname.")
if char_legnth > 25:
    print("You have entered more that 25 charecters.Please make sure that you have only entered your full name.")
else:
    print("Thank you for enetring your name.")



