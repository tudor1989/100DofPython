 # If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00/5) * 1.12 - 33.6 
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this. 

#Write your code below this line: 

print("Welcome to your Tip Calculator!\nLet's begin\n")

#amount of the bill
bill = input("How much was the bill?\n")

#how many people attended 
people = input("How many of you were there?\n")

#how much tip would you like to leave 10, 12 or 15 ? 
tip = input("How much tip would you like to leave 10, 12 or 15?\n")

# convert data type from "str" to "float" & "int" to do math 
bill = float(bill)
people = int(people)
tip = int(tip)

# alternative can be bill = int(input())

# calculate amount to pay per person rounded to 2 decimal points.
to_pay = (bill + bill * tip/100) / people 

print(f"You have to pay ${round(to_pay,2)}")

