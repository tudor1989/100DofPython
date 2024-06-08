# Love calculator 

print("The Love Calculator is calculating your score...")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

# TRUE LOVE 
# To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs
# 2. Then check for the number of times the letters in the word LOVE occurs. 
# 3. Then combine these numbers to make a 2 digit number. 

######## Write Code below ########

# make one string out of both names 

big_string = name1 + name2 

#print(big_string)

# check for TRUE letters in big_string

a_upper = big_string.count("T")
a_lower = big_string.count("t")

b_upper = big_string.count("R")
b_lower = big_string.count("r")

c_upper = big_string.count("U")
c_lower = big_string.count("u")

d_upper = big_string.count("E")
d_lower = big_string.count("e")


first_digit = a_upper + a_lower + b_lower + b_upper + c_upper + c_lower + d_upper + d_lower

#print(first_digit)

E = big_string.count("L")
e = big_string.count("l")
F = big_string.count("O")
f = big_string.count("o")
G = big_string.count("V")
g = big_string.count("v")
H = big_string.count("E")
h = big_string.count("e")

second_digit = E+ e + F + f + G + g + H + h 

final_number = str(first_digit) + str(second_digit)

#print(final_number)    
#print(f"Your score is {final_number}")

if int(final_number) < 10 or int(final_number) > 90:
  print(f"Your score is {final_number}, you go togheter like coke and mentos!")
elif int(final_number) >= 40 and int(final_number) <= 50: 
  print(f"Your score is {final_number}, you are alright together.")
else:
  print(f"Your score is {final_number}")

