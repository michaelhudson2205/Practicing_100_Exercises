"""blah, blah, blah"""


# ? >>>===Ex 34: Mathematical function===<<<
# Write a function named f(a,b,x) that takes three integers a, b and x as
# parameters and returns the result of the following function:
# f(a,b,x) = a*(x**3) + 2*a(x**2) + b
# Verification tests:
# f(3,0,1) should return 9
# f(0,2,2) should return 2
def f(a, b, x):
    return a * (x**3) + 2 * a * (x**2) + b


f(3, 0, 1)  # should return 9
f(0, 2, 2)  # should return 2


# ? >>>===Ex 35: Presence of an element in a list===<<<
# Write a function named CheckPresence(a,L) that takes a list L and an
# element a as parameters. The function returns True if the element a
# exists in the list L, and False if the element a does not exist in the list L.
# Verification tests:
# CheckPresence(2,[1,2,3,4,5,6]) should return True
# CheckPresence(-1,[3,6,9,7,"abcr"]) should return False
def CheckPresence(a, L):
    """Check if element a is in list L"""
    if a in L:
        return True
    else:
        return False


CheckPresence(2, [1, 2, 3, 4, 5, 6])  # should return True
CheckPresence(-1, [3, 6, 9, 7, "abcr"])  # should return False

# ? >>>===Ex 36: Calculation of the sum of digits===<<<
# Write a program that calculates the sum of the digits of a
# number. The program should display the result on the console.
# E.g., for the number 149, the program should display 14.
# E.g., for the number 3018, the program should display 12.
number = 3018
number_str = str(number)
sum_of_digits = 0  # Initialize sum_of_digits to 0
for digit in number_str:
    sum_of_digits += int(digit)  # Convert digit to int and add to sum_of_digits
print(sum_of_digits)  # Display the result on the console

number = 149
number_str = str(number)
sum_of_digits = 0  # Initialize sum_of_digits to 0
for digit in number_str:
    sum_of_digits += int(digit)  # Convert digit to int and add to sum_of_digits
print(sum_of_digits)  # Display the result on the console

# ? >>>===Ex 37: Sum of a list===<<<
# Write a function called calculateSum(L) that takes a list of
# integers as a parameter and returns the sum of the elements in the list.
# E.g., calculateSum([3,2,6,9,-1,5]) should return 24.
# E.g., calculateSum([-3,-6,0,1,2,7]) should return 1.

# ? >>>===Ex 38: Removing Duplicates===<<<
# Write a function removeDuplicates(L) that takes a list of integers
# L as a parameter and returns the List without any duplicate elements
# in ascending order.
# E.g., removeDuplicates([0,3,5,7,3,5,1,-1,0])
# should return [-1,0,1,3,5,7].
# E.g., removeDuplicates([0,5,9,10,3.2,1,-3])
# should return [-3,0,1,3.2,5,9,10].

# ? >>>===Ex 39: Adding elements to a dictionary===<<<
# Write a function named addElementDict(key,value,d) that takes three
# parameters as input: a dictionary d, a key and its associated value.
# The function should add this key and value to the dictionary d.
# Finally, the function should return the modified dictionary d with
# the new key-value pair added.
# E.g., addElementDict("baptiste", 29, {"julien": 14, "laurent": 31})
# should return {"julien": 14, "laurent": 31, "baptiste": 29}
# E.g., addElementDict("weight", 65.3, {})
# should return {"weight": 65.3}

# ? >>>===Ex 40: Recreation of the max function===<<<
# Write a function maximum(L) that takes a list of integers as a
# parameter and returns the largest value.
# Note: The idea is not to use the already existing max() function.
# E.g., maximum([-9,2,4,1,8,0]) should return 8.
# E.g., maximum([-3,1,7,6,2,3]) should return 7.

# ? >>>===Ex 41: Sum of a Sublist===<<<


# ? >>>===Ex 42: Pattern Creation===<<<


# ? >>>===Ex 43: Recreation of the min function===<<<


# ? >>>===Ex 44: Recreation of the len function===<<<


# ? >>>===Ex 45: Calculating the average of a list of numbers===<<<


# ? >>>===Ex 46: Divisors of an integer===<<<


# ? >>>===Ex 47: Capitalisation Check===<<<


# ? >>>===Ex 48: List Concatenation===<<<


# ? >>>===Ex 49: Calculating the Number of Values in a Dictionary===<<<


# ? >>>===Ex 50: Concatenation of dictionaries===<<<


# ? >>>===Ex 51: Calculating the factorial of a number===<<<


# ? >>>===Ex 52: Divisors & Multiples===<<<


# ? >>>===Ex 53: Presence of a Vowel in a String===<<<


# ? >>>===Ex 54: Removing Spaces in a Sentence===<<<


# ? >>>===Ex 55: Position of an Element in a List===<<<


# ? >>>===Ex 56: Filter words by length===<<<


# ? >>>===Ex 57: Reverse the Order of Words===<<<


# ? >>>===Ex 58: Number of Occurrences in a List===<<<


# ? >>>===Ex 59: Union of lists without duplication===<<<


# ? >>>===Ex 60: Calculation of the GCD===<<<


# ? >>>===Ex 61: Reading a file===<<<


# ? >>>===Ex 62: Number of Occurrences of a Word in a File===<<<


# ? >>>===Ex 63: Delete a Character from a File===<<<


# ? >>>===Ex 64: Presence of a number in a file===<<<


# ? >>>===Ex 65: Number of files in a folder===<<<


# ? >>>===Ex 66: Write in a file===<<<


# ? >>>===Ex 67: The key with the maximum number of unique values===<<<


# ? >>>===Ex 68: Ask the user for a list===<<<


# ? >>>===Ex 69: Number of days and hours===<<<


# ? >>>===Ex 70: Generate a Password Randomly===<<<


# ? >>>===Ex 71: Trigonometric function===<<<


# ? >>>===Ex 72===<<<


# ? >>>===Ex 73===<<<


# ? >>>===Ex 74===<<<
