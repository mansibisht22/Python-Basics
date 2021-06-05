# a program to find the greatest of 3numbers entered by the user.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))


if(a > b and a > c):
    print("the greatest number is: ", a)

elif(b > c and b > a):
    print("the greatest number is: ", b)

elif(c > b and c > a):
    print("the greatest number is: ", c)

# a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

marks_1 = int(input("Enter marks of sub1: "))
marks_2 = int(input("Enter marks of sub1: "))
marks_3 = int(input("Enter marks of sub1: "))

total = (marks_1 + marks_2 + marks_3)/300*100
print("your total percentage is: ", total)
if(total >= 40 and marks_1 >= 33 and marks_2 >= 33 and marks_3 >= 33):
    print("You've passed")

else:
    print("you've failed.")

# detecting spam text by user
user_inp = input("enter your message")

if(user_inp == "make money" or user_inp=="buy now" or user_inp=="buy now"):
    print("SPAM")




