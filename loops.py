# program to print the multiplication table
# of a given number using for loop

n = int(input("Enter no. to obtain table: "))

for j in range(1, 11):
    prod = n*j
    j = j+1
    print(n, "*", j, "=", prod)


# a program to greet all the person names stored in a list l1 and which starts with S.
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("hello", name)

    else:
        print("no.")

# program to print the multiplication table
# of a given number using while loop

num = int(input("Enter no. to obtain table: "))
i = 1
while(i <= 10):
    prod = num*i
    i = i+1
    print(num, "*", i, "=", prod)

# Write a program to find whether a given
# number is prime or not

x = int(input("Enter a number: "))

if x > 1:
    for y in range(2, x):
        if (x % i) == 0:
            print(x, "is not a prime number")
            break
    else:
        print(x, "is a prime number")

else:
    print(x, "is not a prime number")

# Write a program to find the sum of first
# n natural numbers using a while loop.

a = int(input("Enter no. to obtain sum of first n natural nos: "))
sum = 0
while (x>0): 
        sum = sum + i
        a-=1

print(sum)

#Write a program to calculate the factorial of
# a given number using for loop.

p = int(input("enter no. to obtain factorial"))
fac = 1
for i in range(1, p+1):
    fac = fac*i
    i+=1
print("factorial of", p, "is", fac)
