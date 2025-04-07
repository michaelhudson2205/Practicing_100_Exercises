# ===Exercise 1===
# Write a sequence of Python instructions to declare 3 variables a,b, and
# c, assigning them the values 1, 'France', and 36.2 respectively, then
# display the values of thes variables on the console.
a = 1
b = "France"
c = 36.2
print(a)
print(b)
print(c)

# ===Exercise 2===
# Write a sequence of Python instructions to declare 1 variable ch and
# initialize it with the value 'hello', then modify this same variable to
# contain the value 'how are you'. The program should display the
# content of the variable on the console after modification.
ch = "hello"
ch = "how are you"
print(ch)

# ===Exercise 3===
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

# ===Exercise 4===
# Write a program that asks the user for their weight in kilograms, then
# stores it in a variable. The program should display the weight entered by the user at the end.
weight = input("What is your weight in kilograms? ")
print("The user's weight is:", weight)

# ===Exercise 5===
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

# ===Exercise 6===
# Write a program that declares the variable d and assigns it the value 5,
# then checks whether this variable is greater or less than 0. If the
# variable is greater than 0, the program should display 'Positive',
# otherwise, it should display 'Negative'.
d = 0
if d >= 0:
    print("Positive, or zero")
else:
    print("Negative")

# ===Exercise 7===
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
