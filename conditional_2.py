# program that finds out whether a given name is present in a list or not
my_list = ["Mansi", "Bisht", " Shreya", "Abhishek"]

if("Mansi" in my_list):
    print("YES")

# program to calculate the grade of a student
# from his marks from the following scheme:

marks = int(input("Enter your marks: "))

if(marks > 90 and marks <= 100):
    print("Ex")

elif(marks > 80 and marks <= 90):
    print("A")

elif(marks > 70 and marks <= 80):
    print("B")

elif(marks > 60 and marks <= 70):
    print("C")

elif(marks > 50 and marks <= 60):
    print("D")

else:
     print("F")


#a program to find out whether a username has less than 10 spaces
user_input = input("username: ")
word = user_input.count(" ")

if(word > 10):
    print("Too many spaces!")

else:
    print("Correct!")