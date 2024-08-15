import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_options = [rock, paper, scissors]

#Ask for user choice input

user_choice = input("What's your game option? ")

print(user_choice)

#match user input with options from the list 

user_choice_converted = user_choice

if user_choice == 'rock':
    user_choice_converted = game_options[0]
elif user_choice == 'paper':
    user_choice_converted = game_options[1]
else:
    user_choice_converted = game_options[2]


#generating PC random choice

computer_choice = random.choice(game_options)

#print User choice: 

print("Your game option is:\n")
print(user_choice_converted)


#print PC choice:

print("PC choice is\n")
print(computer_choice)


#decide Winner conditionals + catch draw condition

if user_choice_converted == game_options[0]:
    if computer_choice == game_options[0]:
        print("It's a draw! Redo game!")
        if computer_choice == game_options[2]:
            print("User wins! Congrats")
    else:
        print("Computer wins! You lost!")
elif user_choice_converted == game_options[1]:
    if computer_choice == game_options[1]:
        print("It's a draw! Redo game!")
        if computer_choice == game_options[0]:
           print("User wins! Congrats")
    else:
        print("Computer wins! You lost!")
elif user_choice_converted == game_options[2]:
    if computer_choice == game_options[2]:
        print("It's a draw! Redo game!")
        if computer_choice == game_options[1]:
            print("User wins! Congrats")
    else:
        print("Computer wins! You lost!")
else:
    print("Wrong game!")
