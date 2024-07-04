line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#isolate column and row from user input
column = position[0]
row = int(position[1])


column_list = ["A","B","C"]

x = column_list.index(column)

row_list = [1, 2, 3]

y = row_list.index(row)

#print(type(row))

map[y][x] = 'X'


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
