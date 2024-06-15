import random


print("Welcome to Heads or Tails!")
print("Toss the coin")

number = random.randint(0,1)

print(number)

if number == 0:
  print("Tails")
else:
  print("Heads")
