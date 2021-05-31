# Python program to display a user-entered name followed by Good Afternoon using input() function

inp = input("Enter your name!-")
print("Good Afternoon " + inp)

# Write a program to fill in a letter template given below with name and date.
name = input("Enter Name: ")
date = input("Enter Date:")
print("Dear " + name + " You are selected \n" + date)

# Write a program to detect double spaces in a string. Replace the double spaces from problem 3 with single spaces.
user_input = input("Enter any string")
print(user_input.replace("  ", "   "))

# Write a program to format the following letter
# using escape sequence characters.
# letter = “Dear Harry, This Python course in nice. Thanks!!”

print("Dear Harry, This Python course is nice. \n Thanks!!")
