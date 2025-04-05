#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Random Module functions to use 

random.random(): This function returns a random floating-point number in the range of [0.0, 1.0). It is useful for generating random numbers for simulations or other applications.

random.randint(a, b): This function returns a random integer between a and b, inclusive. It is helpful for selecting a random element from a list or generating random numbers within a specific range.

random.choice(seq): This function returns a random element from a sequence, such as a list, tuple, or string. It is convenient for selecting random items from a collection.

random.shuffle(seq): This function shuffles the elements of a sequence in place, meaning it modifies the original sequence directly. It is commonly used to randomize the order of items in a list.

random.sample(population, k): This function returns a k length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.


######################################################################
#generate the number of letters 

letter_list = random.choices(letters, k = nr_letters)

#generate the numbers list 

num_list = random.choices(numbers, k = nr_numbers)

#generate the symbols list

symbol_list = random.choices(symbols, k = nr_symbols)

#concatenate results into a new list 

password_list = letter_list + num_list + symbol_list 

print(password_list)

your_pass = random.shuffle(password_list)
