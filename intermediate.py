"""blah, blah, blah"""


# ? >>>===Exercise 34===<<<
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


# ? >>>===Exercise 35===<<<
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

# ? >>>===Exercise 36===<<<
# Write a program that calculates the sum of the digits of a
# number. The program should display the result on the console.
# E.g., for the number 149, the program should display 14.
# E.g., for the number 3018, the program should display 12.

# ? >>>===Exercise 37===<<<
# Write a function called calculateSum(L) that takes a list of
# integers as a parameter and returns the sum of the elements in the list.
# E.g., calculateSum([3,2,6,9,-1,5]) should return 24.
# E.g., calculateSum([-3,-6,0,1,2,7]) should return 1.

# ? >>>===Exercise 38===<<<
# Write a function removeDuplicates(L) that takes a list of integers
# L as a parameter and returns the List without any duplicate elements
# in ascending order.
# E.g., removeDuplicates([0,3,5,7,3,5,1,-1,0])
# should return [-1,0,1,3,5,7].
# E.g., removeDuplicates([0,5,9,10,3.2,1,-3])
# should return [-3,0,1,3.2,5,9,10].

# ? >>>===Exercise 39===<<<
# Write a function named addElementDict(key,value,d) that takes three
# parameters as input: a dictionary d, a key and its associated value.
# The function should add this key and value to the dictionary d.
# Finally, the function should return the modified dictionary d with
# the new key-value pair added.
# E.g., addElementDict("baptiste", 29, {"julien": 14, "laurent": 31})
# should return {"julien": 14, "laurent": 31, "baptiste": 29}
# E.g., addElementDict("weight", 65.3, {})
# should return {"weight": 65.3}

# ? >>>===Exercise 40===<<<
# Write a function maximum(L) that takes a list of integers as a
# parameter and returns the largest value.
# Note: The idea is not to use the already existing max() function.
# E.g., maximum([-9,2,4,1,8,0]) should return 8.
# E.g., maximum([-3,1,7,6,2,3]) should return 7.

# ? >>>===Exercise 41===<<<


# ? >>>===Exercise 42===<<<


# ? >>>===Exercise 43===<<<


# ? >>>===Exercise 44===<<<


# ? >>>===Exercise 45===<<<


# ? >>>===Exercise 46===<<<


# ? >>>===Exercise 47===<<<


# ? >>>===Exercise 48===<<<


# ? >>>===Exercise 49===<<<


# ? >>>===Exercise 50===<<<


# ? >>>===Exercise 51===<<<


# ? >>>===Exercise 52===<<<


# ? >>>===Exercise 53===<<<


# ? >>>===Exercise 54===<<<


# ? >>>===Exercise 55===<<<


# ? >>>===Exercise 56===<<<


# ? >>>===Exercise 57===<<<


# ? >>>===Exercise 58===<<<


# ? >>>===Exercise 59===<<<


# ? >>>===Exercise 60===<<<


# ? >>>===Exercise 61===<<<


# ? >>>===Exercise 62===<<<


# ? >>>===Exercise 63===<<<


# ? >>>===Exercise 64===<<<


# ? >>>===Exercise 65===<<<


# ? >>>===Exercise 66===<<<


# ? >>>===Exercise 67===<<<


# ? >>>===Exercise 68===<<<


# ? >>>===Exercise 69===<<<


# ? >>>===Exercise 70===<<<


# ? >>>===Exercise 71===<<<


# ? >>>===Exercise 72===<<<


# ? >>>===Exercise 73===<<<


# ? >>>===Exercise 74===<<<
