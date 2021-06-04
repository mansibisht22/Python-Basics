# program to create a dictionary of Hindi words with values as their English translation.
dict = { 'khushi' : 'happiness' , 'dukh': 'sadness' , 'ansoo' : 'tears'}
word = input("Enter Keyword to find meaning: ")
print(dict.get(word))

#program to input eight numbers from the user and display all the unique numbers (once).

my_set = {1, 2, 0, 1, 5, 6, 3, 9, 11, 11, 22, 9}
print(my_set)

#3.	Can we have a set with 18(int) and “18”(str) as a value in it?
new_set = {18, "18"}
print(new_set)

#length of S after the above operations?
S = set()
S.add(20)
S.add(20.0)
S.add("20")
print(len(S))




