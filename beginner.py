# >>>===Exercise 1===<<<
# Write a sequence of Python instructions to declare 3 variables a,b, and
# c, assigning them the values 1, 'France', and 36.2 respectively, then
# display the values of thes variables on the console.
a = 1
b = "France"
c = 36.2
print(a)
print(b)
print(c)

# >>>===Exercise 2===<<<
# Write a sequence of Python instructions to declare 1 variable ch and
# initialize it with the value 'hello', then modify this same variable to
# contain the value 'how are you'. The program should display the
# content of the variable on the console after modification.
ch = "hello"
ch = "how are you"
print(ch)

# >>>===Exercise 3===<<<
# Write a sequence of Python instructions to declare 2 variables x and y,
# assigning them the values 3 and 8.5 respectively, then convert the type
# of these variables to strings. The program should display the type of these # variables after conversion at the end.
x = 3
y = 8.5
print(type(x))
print(type(y))
x = str(x)
y = str(y)
print(type(x))
print(type(y))

# >>>===Exercise 4===<<<
# Write a program that asks the user for their weight in kilograms, then
# stores it in a variable. The program should display the weight entered by the user at the end.
weight = input("What is your weight in kilograms? ")
print("The user's weight is:", weight)

# >>>===Exercise 5===<<<
# Write a sequence of Python instructions to declare a variable var and
# assign it the value "Hello", then the program should check whether the
# variable var is an integer or a string. If it is an integer, the program
# should display "Interger" on the console. If it is a string, the program
# will display "String".
var = 16
if type(var) == str:
    print("The variable is a String")
elif type(var) == int:
    print("The variable is an Integer")
else:
    print("The variable is not a String or an Integer")

# >>>===Exercise 6===<<<
# Write a program that declares the variable d and assigns it the value 5,
# then checks whether this variable is greater or less than 0. If the
# variable is greater than 0, the program should display 'Positive',
# otherwise, it should display 'Negative'.
d = 0
if d >= 0:
    print("Positive, or zero")
else:
    print("Negative")

# >>>===Exercise 7===<<<
# Write a program that asks the user for their age, then stores it in a
# variable. The program should check whether the user is older or
# younger than 18 years. If the user's age is greater than or equal to 18,
# the program should display "The user is a legal adult", otherwise "The
# user is a minor".

# Request user age
age = input("How old are you?")

# Convert age to int
age = int(age)

# Case distinction
if age >= 18:
    print("The user is a legal adult")
else:
    print("The user is a minor")

# >>>===Exercise 8===<<<
# Write a Python program that displays the numbers from 1 to
# 20 inclusive on the console. Create two versions, one with
# the for loop and the other with the while loop.

# for loop
for i in range(1, 21):
    print(i)

# while loop
counter = 1
while counter <= 20:
    print(counter)
    counter += 1

# >>>===Exercise 9===<<<
# Write a Python program that displays only the odd numbers between 10
# and 20 inclusive. Create two versions, one with the for loop and the
# other with the while loop.

# for loop
for i in range(10, 21):
    if i % 2 == 1:
        print(i)

# while loop
counter = 10
while counter <= 20:
    if counter % 2 == 1:
        print(counter)
    counter += 1

# >>>===Exercise 10===<<<
# Write the instruction that creates a list of numbers from 1 to 10
# using list comprehension.
L = [i for i in range(1, 11)]
print(L)

# >>>===Exercise 11===<<<
# Write the instruction that creates a list of even numbers from 1
# to 10 using list comprehension.
L = [i for i in range(1, 11) if i % 2 == 0]
print(L)

# >>>===Exercise 12===<<<
# Write the instructions that create the list L and assign it the value
# [6, 8, 3, 4, 1, 12, 2, 9.2], then sort the numbers in the list in
# ascending order. The program should display the list L after sorting
# the numbers

# Declaration of the list L
L = [6, 8, 3, 4, 1, 12, 2, 9.2]
L.sort()
print(L)

# to do descending order
L.sort(reverse=True)
print(L)

# >>>===Exercise 13===<<<
# Write the instructions that create the list L and assign it the value
# [3, 2, 2, 1, 9, 1, 2, 3, 7], then calculate the number of occurrences
# of the number 1 in the list L.

# Declaration of the list L
L = [3, 2, 2, 1, 9, 1, 2, 3, 7]
L.count(1)

# >>>===Exercise 14===<<<
# Write the instructions that create an empty list L and then add the
# intergers 10, 25, 30, 45, 90, and the strings "ab", "cd", "ef" to it.

# >>>===Exercise 15===<<<
# Write a program that creates the list L and assigns it the value
# [1,2,3,4,5,6,7,8,9,10], then creates a new list that takes every
# third element from the list L. In this case we should end up with
# the following list: [1,4,7,10]

# 1st method
# Empty list
L1 = []

# adding elements
L1 += [10, 25, 30, 45, 90, "ab", "cd", "ef"]
print(L1)

# 2nd method
# Empty list
L2 = []
elt_to_add = [11, 22, 33, 44, 99, "gh", "ij", "kl"]
for elt in elt_to_add:
    L2.append(elt)
print(L2)

# >>>===Exercise 16===<<<
# Write the instructions to sort a string in ascending alphabetical order.
# For testing, take the string c = "france".
# The program should output "acefnr"

# string declaration
c1 = "france"

# order the string in ascending order
c2 = sorted(c)

# take a look
print(c2)

# convert the resulting list into a string
c3 = "".join(c2)
print(c3)

# order the original string in descending order etc.
c4 = sorted(c, reverse=True)
print(c4)
c5 = "".join(c4)
print(c5)

# >>>===Exercise 17===<<<
# Write a program that, given two lists L1 and L2, returns a list L3
# containing the common elements between L1 and L2.
# For testing, we will take the lists:
# L1 = [9,8,7,14,3,2,"a","p","hello","b"]
# L2 = ["b",1,9.2,6,3,9,"p"]

# Declaration of lists
L1 = [9, 8, 7, 14, 3, 2, "a", "p", "hello", "b"]
L2 = ["b", 1, 9.2, 6, 3, 9, "p"]

# convert lists to sets
# then take intersection of these two sets
L3 = set(L2).intersection(set(L1))

# take a look
print(L3)

# convert L3 to a list
L3 = list(L3)
print(L3)

# >>>===Exercise 18===<<<
# Write a program that sorts a list of tuples, L, in ascending order
# based on the second element of each tuple.
# The list is:
# L = [("Apple", 15), ("Banana", 8), ("Strawberry", 12),
# ("Kiwi", 9), ("Peach", 2)]
# The resulting list L after sorting should be:
# L = [("Peach", 2), ("Banana", 8), ("Kiwi", 9),
# ("Strawberry", 12), ("Apple", 15)]

# creation of a list of tuples
L = [("Apple", 15), ("Banana", 8), ("Strawberry", 12), ("Kiwi", 9), ("Peach", 2)]

# sort the list of tuples in ascending order
# according to the second element of the tuples
L.sort(key=lambda x: x[1])
print(L)

# >>>===Exercise 19===<<<
# Write a program that allows you to reverse a string.
# The program should reverse the variable ch containing
# the phrase "Hello everyone"
ch = "Hello everyone"

# reverse the string ch
ch_reverse = ch[::-1]
print(ch_reverse)

# >>>===Exercise 20===<<<
# Write a program that displays on the console the values of the
# keys "Apple" and "Banana" from the dictionary
# {"Apple": 3, "Banana": 7, "Kiwi": 1}

# declaration of the dictionary d
d = {"Apple": 3, "Banana": 7, "Kiwi": 1}

# select the value of the key 'Apple'
print(d["Apple"])

# select the value of the key 'Banana'
print(d["Banana"])

# >>>===Exercise 21===<<<
# Write a program that calculates the sum of the values in the
# following dictionary:
# {"Apple": 15, "Banana": 8, "Strawberry": 12, "Kiwi": 9, "Peach": 2}
d = {"Apple": 15, "Banana": 8, "Strawberry": 12, "Kiwi": 9, "Peach": 2}
sum(d.values())

# >>>===Exercise 22===<<<
# Write a program that truncates a decimal number to 2 digits after
# the decimal point. For example, if we take the decimal number
# 187.632587 the program should display 187.63.
float("{:.2f}".format(187.637878))

# >>>===Exercise 23===<<<
# Write a program that formats the string "My name is myName
# and I am age years old. I am learning the language
# languageName". The program should format this string by
# assigning the content of the following variables:
# myName = "Julien", age = 32, languageName = "Python"
myName = "Julien"
age = 32
languageName = "Python"

ch = f"My name is {myName} and I am {age} years old. I am learning \
the language {languageName}.".format(
    myName, age, languageName
)

print(ch)

# >>>===Exercise 24===<<<
# Write a program that displays the multiplication table
# of the number 8.
for i in range(0, 11):
    print("8 x", i, "=", 8 * i)

# >>>===Exercise 25===<<<
# Write a program that displays the directory where the
# current Python script is located.
import os

print(os.getcwd())

# >>>===Exercise 26===<<<
# Write a program that allows you to remove an element from a list.
# From the list L = [1,2,3,4,5] remove the number 1.
L = [1, 2, 3, 4, 5]
L.remove(1)
L

# >>>===Exercise 27===<<<
# Write a program that allows you to retrieve the extension of a file.
import os

file_path = r"C:\Users\billy.blogs\some_notebook.ipynb"

# retrieve file name
file_name = os.path.basename(file_path)

# convert the file name to a list, and retrieve the
# last element of this list which represents the extension
extension_file = file_name.split(".")[-1]

print("File extension:", extension_file)

"France is a beautiful country".split(" ")
"some_notebook.ipynb".split(".")

# >>>===Exercise 28===<<<
# Write a program that calculates the execution time of a script.
# Use the script from exercise 24 as an example. The program
# should display the multiplication table from exercise 24 and
# the execution time at the end.
import time

# store start time of the program
start = time.time()

#### THE CODE ###
for i in range(0, 11):
    print("8 x", i, "=", 8 * i)
#################

# calculate execution time of the program
end = time.time()

# Calculate execution time
print("Code execution time:", end - start)

# >>>===Exercise 29===<<<
# Write a program that randomly shuffles the elements of a
# list L. For example, L = [3,6,8,7,2,'s','ch','d'].
import random

L = [3, 6, 8, 7, 2, "s", "ch", "d"]

# randomly mix elements of the L list
random.shuffle(L)
print(L)

# >>>===Exercise 30===<<<
# Write a program that randomly returns a number between 20 and 30.
import random

# choose a random number between 20 and 30
random_number = random.randint(20, 30)
print(random_number)

# >>>===Exercise 31===<<<
# Write a program that displays 8 lines of 16 consecutive numbers.

# first loop to define the number of lines
for i in range(8):
    # second loop to display each line
    # numbers from 5 to 20
    for j in range(5, 21):
        print(j, end=" ")
    # to return to the line
    print()

# >>>===Exercise 32===<<<
# Write a program that creates the list L = [3,6,9,12,15,18,21,24],
# then creates a new list L1 using list comprehension that contains
# the numbers from L divided by 3. Display L1 on the console.
L = [3, 6, 9, 12, 15, 18, 21, 24]
L1 = [l / 3 for l in L]
print(L1)

# >>>===Exercise 33===<<<
# Write a program that creates a list L = [-6,5,-3,-1,2,8,-3.6],
# then creates a new list L1 using list comprehension that contains
# the numbers from L that are strictly greater than 0. Display L1.
L = [-6, 5, -3, -1, 2, 8, -3.6]
L1 = [l for l in L if l > 0]
print(L1)
