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
def calculateSum(L):
    """Calculate the sum of elements in list L"""
    total = 0  # Initialize total to 0
    for number in L:
        total += number  # Add each number to total
    return total  # Return the total sum


calculateSum([3, 2, 6, 9, -1, 5])
calculateSum([-3, -6, 0, 1, 2, 7])


# ? >>>===Ex 38: Removing Duplicates===<<<
# Write a function removeDuplicates(L) that takes a list of integers
# L as a parameter and returns the List without any duplicate elements
# in ascending order.
# E.g., removeDuplicates([0,3,5,7,3,5,1,-1,0])
# should return [-1,0,1,3,5,7].
# E.g., removeDuplicates([0,5,9,10,3.2,1,-3])
# should return [-3,0,1,3.2,5,9,10].
def removeDuplicates(L):
    """Remove duplicates from list L and return sorted list"""
    unique_elements = set(L)  # Convert list to set to remove duplicates
    sorted_list = sorted(unique_elements)  # Sort the unique elements
    return sorted_list  # Return the sorted list


removeDuplicates([0, 3, 5, 7, 3, 5, 1, -1, 0])


def removeDuplicatesB(L):
    for elt in L:
        elt_occ = L.count(elt)
        if elt_occ > 1:
            for i in range(elt_occ - 1):
                L.remove(elt)
    L.sort()
    return L


removeDuplicatesB([0, 3, 5, 7, 3, 5, 1, -1, 0])  # should return [-1,0,1,3,5,7]
removeDuplicatesB(
    [0, 5, 9, 5, 10, 5, 3.2, 1, 5, -3]
)  # should return [-3,0,1,3.2,5,9,10]


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
def addElementDict(key, value, d):
    """Add key-value pair to dictionary d"""
    d[key] = value  # Add key-value pair to dictionary
    return d  # Return modified dictionary


addElementDict("baptiste", 29, {"julien": 14, "laurent": 31})
addElementDict("weight", 65.3, {})


# ? >>>===Ex 40: Recreation of the max function===<<<
# Write a function maximum(L) that takes a list of integers as a
# parameter and returns the largest value.
# Note: The idea is not to use the already existing max() function.
# E.g., maximum([-9,2,4,1,8,0]) should return 8.
# E.g., maximum([-3,1,7,6,2,3]) should return 7.
def maximum(L):
    """Return the maximum value in list L"""
    max_value = L[0]  # Initialize max_value to the first element of L
    for number in L:
        if number > max_value:  # If current number is greater than max_value
            max_value = number  # Update max_value
    return max_value  # Return the maximum value


maximum([-9, 2, 4, 1, 8, 0])
maximum([-3, 1, 7, 6, 2, 3])


# ? >>>===Ex 41: Sum of a Sublist===<<<
# Write the code for the function sumSubList(L,i,j) which takes
# three parameters: a list L, a starting calculation index i, and an
# ending calculation index j. The function should return the sum of
# the numbers located between indices i and j in the list L.
# E.g., sumSubList([4,10,12,16,18],2,4) should return 46.
# E.g., sumSubList([2,4,6,8,10,12],0,2) should return 12.
def sumSubList(L, i, j):
    ## select the sub-list
    Lij = L[i : j + 1]  # Select sub-list from index i to j (inclusive)
    ## initialise the variable sum_ to 0
    sum_ = 0  # Initialize sum_ to 0
    ## loop through the sub-list and add each element to sum_
    for number in Lij:
        sum_ += number
    ## return the sum
    return sum_  # Return the total sum


sumSubList([4, 10, 12, 16, 18], 2, 4)  # should return 46
sumSubList([2, 4, 6, 8, 10, 12], 0, 2)  # should return 12


# ? >>>===Ex 42: Pattern Creation===<<<
# Write a program that displays the pyramid below:
# ^
# ^^
# ^^^^
# ^^^^^^
# ^^^^^^^^
for nbr_star in range(1, 11):
    if nbr_star % 2 == 0 or nbr_star == 1:
        print("*" * nbr_star)


# ? >>>===Ex 43: Recreation of the min function===<<<
# Write a function minimum(L) that takes a list of integers as a
# parameter and returns the smallest value.
# Note: The idea is not to use the already existing min() function.
# E.g., minimum([-9,2,4,1,8,0]) should return -9.
# E.g., minimum([-3,1,7,6,2,3]) should return -3.
def minimum(L):
    """Return the minimum value in list L"""
    min_value = L[0]  # Initialize min_value to the first element of L
    for number in L:
        if number < min_value:  # If current number is less than min_value
            min_value = number  # Update min_value
    return min_value  # Return the minimum value


minimum([9, 2, 4, 1, -8, 0])  # should return -9
minimum([-3, 1, 7, 6, 2, 3])  # should return -3

# ? >>>===Ex 44: Recreation of the len function===<<<
# Write a function length(L) that takes a list as a parameter and
# returns the number of elements in the list.
# Note: The idea is not to use the already existing len() function.
# E.g., length([3,6,7,"abcd", [1,3,57],True]) should return 6.
# E.g., length([]) should return 0.

# ? >>>===Ex 45: Calculating the average of a list of numbers===<<<
# Write a function averageList(L) that takes a list of integers
# as a parameter and returns the average of the elements in the list.
# E.g., averageList([1,2,3,4,5,6,7]) should return 4.0
# E.g., averageList([3,0,-1,5,6,9,17]) should return 5.571428571428571


# ? >>>===Ex 46: Divisors of an integer===<<<
# Write a function divisor(n) that takes an integer n as a parameter
# and returns a list containing all the positive divisors of n in
# ascending order.
# E.g., divisor(3) should return [1,3]
# E.g., divisor(9) should return [1,3,9]


# ? >>>===Ex 47: Capitalisation Check===<<<
# Write a function checkCapitals(sentence) that takes a sentence
# as a parameter and checks if the sentence contains at least one
# uppercase letter. If that is the case, the function should return
# True, otherwise it should return False.
# E.g., checkCapitals("Hello World") should return True.
# E.g., checkCapitals("hello world") should return False.


# ? >>>===Ex 48: List Concatenation===<<<
# Write a function concatList(L1, L2, L3) that takes three lists
# L1, L2 and L3 as parameters and returns the concatenation
# of the three lists.
# E.g., cocatList([0,9,8],[2,6,9],[True,False,"abc"])
# should return [0,9,8,2,6,9,True,False,"abc"]
# E.g., concatList([[38,-1],3,-9],["xz","France"],[])
# should return [[38,-1],3,-9,"xz","France"]


# ? >>>===Ex 49: Calculating the Number of Values in a Dictionary===<<<
# Write a function valueCountDict(d) that takes a dictionary as a
# parameter and returns the number of values contained in the lists
# associated with the keys of the dictionary.
# Note: for the purpose of this exercise, it is assumed that all
# values associated with keys are in the form of lists.
# E.g., valueCountDict({"a":[1,2,3],"b":[3,"p"], "c":[8]})
# should return 6
# E.g., valueCountDict({"Julie":[12,60.1],"Fred":[26,75.6], "David":[]})
# should return 4


# ? >>>===Ex 50: Concatenation of dictionaries===<<<
# Write a function concatDict(d1,d2) that takes two dictionaries
# d1 and d2 as parameters and returns the concatenation of the two
# dictionaries.
# E.g., concatDict({"a":3,"b":6},{"c":2,"d":-1})
# should return {"a":3,"b":6,"c":2,"d":-1}
# E.g., concatDict({"d":[2.9,4.1]},{"p":[]})
# should return {"d":[2.9,4.1],"p":[]}


# ? >>>===Ex 51: Calculating the factorial of a number===<<<
# Write a function computeFactorial(n) that calculates the factorial
# of a number (in the mathematical sense) and returns the result
# obtained after this calculation.
# E.g., computeFactorial(3) should return 6
# E.g., computeFactorial(9) should return 362880
# E.g., computeFactorial(0) should return 1


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
