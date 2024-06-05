# Write a program that interprets the BMI based on a user's weight and height. 

# It should tell them the interpretation of their BMI based on the BMI vallue: 

  # Under 18.5 they are underweight 
  # Equal to or over 18.5 but below 25 they have a normal weight 
  # Equal to or over 25 but below 30 they are slightly overweight 
  # Equal to or over 30 but below 35 they are obese
  # Equal to or over 35 they are clinically obese. 

# Enter your height in meters: 
height = float(input("What is your height? "))

# Enter your weight in kilograms: 
weight = int(input("What is your weight? "))

############# write code below################

BMI = weight / (height ** 2) 

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30: 
  print(f"Your BMI is {BMI}, you are slightly overwight.")
elif BMI < 35: 
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print((f"Your BMI is {BMI}, you are clinically obses."))
