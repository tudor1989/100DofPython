print("Welcome to the best Rollercoster Ride of your life")

height = int(input("How tall are you in cm? "))

bill = 0 

if height >= 120: 
  print("You can ride the awsome rollercoaster!")
  age = int(input("How old are you? "))
  if age < 12: 
    print("Your child ticket price is $5.")
    bill = 5
  elif age <= 18:
    print("Your teenager ticket price is $7.")
    bill = 7
  else: 
    print("Your adult ticket price is $12.")
    bill = 12

  want_photo = input("Do you want a photo? Y or N. ")

  if want_photo == "Y":
    # add $3 to their bill 
    bill += 3 
    print(f"Your final ticket price is {bill}")
    
else:
  print("You can't ride.")
