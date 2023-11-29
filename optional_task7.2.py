temperature_hot= True
weekend_day = True
sunny_day = True
print("Answer the following questions using 'yes' or 'no' only")

question_1 = input("Is the temperature above 20 degrees today?: ")
question_2 = input("Is today a weekend day?: ")
question_3 = input("Is it sunny today?: ")

if question_1 == "no":
    temperature_hot = False
if question_2 == "no":
    weekend_day = False
if question_3 == "no":
    sunny_day = False

if temperature_hot == False:
    item_1 = "a long sleeved shirt"
else:
    item_1 = "a short sleeved shirt"

if weekend_day == False:
    item_2 = "a pair of jeans"
else:
    item_2 = "a pair of shorts"

if sunny_day == False:
    item_3 = "a raincoat."
else:
    item_3 = "a cap"

print(f"Today's outfit should include: a {item_1}, {item_2} and {item_3}.")