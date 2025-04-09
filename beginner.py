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


# >>>===Exercise 17===<<<


# >>>===Exercise 18===<<<


# >>>===Exercise 19===<<<


# >>>===Exercise 20===<<<


# >>>===Exercise 21===<<<


# >>>===Exercise 22===<<<


# >>>===Exercise 23===<<<


# >>>===Exercise 24===<<<


# >>>===Exercise 25===<<<


# >>>===Exercise 26===<<<


# >>>===Exercise 27===<<<


# >>>===Exercise 28===<<<


# >>>===Exercise 29===<<<


# >>>===Exercise 30===<<<


# >>>===Exercise 31===<<<


# >>>===Exercise 32===<<<


# >>>===Exercise 33===<<<
