number = int(input("Enter a number: "))
number_modulus = number%2
if number_modulus == 0:
    print(f"{number} is an even number.")
else:
     print(f"{number} is an odd number.")
