# 1st input: enter height in meters e.g. 1.65
height = input("Enter your height: ")
# 2nd input: enter weight in kilograms e.g.: 72 
weight = input("Enter your weight ")

############################

# calculate BMI formula and changing data type to float

BMI = float(weight) / float(height) ** 2 

# show result without floating point
print("Your BMI is " + str(int(BMI)))
