#Leap year check

year = int(input("Give the year to test: "))

# 1st condition: is it cleanly divisible by 4? 
# if NO > NOT a Leap Year
# if YES > test 2nd condition

  
# 2nd condition: is it cleanly divisible by 100? 
# if NO - Leap Year
#if YES - test 3rd condition
  
    
# 3rd condition: Is it cleanly divisible by 400? 
# if YES > Leap Year
# if NO > NOT a Leap Year


if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"Your year {year} is a leap year!")
    else:
      print(f"Your year {year} is not a leap year. ")
  else:
    print(f"Your year {year} is a leap year")
else:
  print(f"Your year {year} is not a leap year! ")
    
