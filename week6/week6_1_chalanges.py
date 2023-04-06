"""1. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid
Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law." """

name = input("What's your name? ")
if name == "Darth Vader":
    print("Luke, I am your father.")
elif name == "Leia":
    print("Luke, I am your sister.")
elif name == "Han":
    print("Luke, I am your brother in law.")
elif name == "R2D2":
    print("Luke, I am your droid.")
else:
    print("We are not relatives")

"""2. Create a function that takes damage and speed (attacks per second) 
and returns the amount of damage after a given time.

Examples
damage(40, 5, "second") ➞ 200

damage(100, 1, "minute") ➞ 6000

damage(2, 100, "hour") ➞ 720000
Notes
Return "invalid" if damage or speed is negative."""

damage, speed, time = 140, 1, "hour"
total_damage = damage * speed
if total_damage >= 0:
    if time == "second":
        print(total_damage * 1)
    elif time == "minute":
        print(total_damage * 60)
    elif time == "hour":
        print(total_damage * 3600)
else:
    print("invalid")

"""
3. Create a function that takes a list of strings and integers, 
and filters out the list so that it returns a list of integers only.

Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

filter_list(["Nothing", "here"]) ➞ []"""

mixed_list = ["4", 13, "mm", 7, -9, "bb"]
# print(type(mixed_list))
for item in mixed_list:
    if isinstance(item, int):
        print(item)
    elif isinstance(item, str):
        print("")

"""4. Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.

Examples
is_symmetrical(7227) ➞ True

is_symmetrical(12567) ➞ False

is_symmetrical(44444444) ➞ True

is_symmetrical(9939) ➞ False

is_symmetrical(1112111) ➞ True"""
#version1
number = int(input("Type a symmetrical number: "))
if number == int(str(number)[::-1]):
    print("True")
else:
    print("False")

#version2
number = int(input("Type a symmetrical number: "))
number2 = int(str(number)[::-1])
print(number == number2)

"""
5. Create a function that changes all the elements in a list as follows:

Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and make the first letter of the word a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]

change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]

change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean 
and as readable as possible!"""
#is not complete yet
variable1, variable2, variable3 = "13", "2", "divide"
if variable3 == "add":
    print(int(float(variable1) + float(variable2)))
elif variable3 == "subtract":
    print(int(float(variable1) - float(variable2)))
elif variable3 == "multiple":
    print(int(float(variable1) * float(variable2)))
elif variable3 == "divide":
    print(int(float(variable1) / float(variable2)))
else:
    print("Undefined")

"""6. Create a function that takes a string s and returns a list of 
two-paired characters. If the string has an odd number of characters, 
add an asterisk * in the final pair.

See the below examples for a better understanding:

Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]

string_pairs("edabit") ➞ ["ed", "ab", "it"]

string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
Notes
Return [] if the given string is empty."""

#is not done yet

"""7. Create a function that takes two parameters and, if both parameters 
are strings, add them as if they were integers or if the two parameters 
are integers, concatenate them.

Examples
stupid_addition(1, 2) ➞ "12"

stupid_addition("1", "2") ➞ 3

stupid_addition("1", 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers."""

parameter1, parameter2 = 2, 5
if isinstance(parameter1, str) and isinstance(parameter2, str):
    print(int(parameter1) + int(parameter2))
elif isinstance(parameter1, int) and isinstance(parameter2, int):
    print(str(parameter1) + str(parameter2))
else:
    print("None")

"""8. Write a function that does the following operations: adding, subtracting, 
dividing, or multiplying values. It is simply referred to as variable 
operation variable. Of course, the variables have to be defined, 
but in this challenge the variables will be defined for you. 
All you have to do is look at the variables, do some string to integer 
conversions, use some if conditionals, and combine them based on the operation.

The numbers and operation will be given as strings, and you should return the 
value as a string as well.

Examples
operation("1", "2", "add" ) ➞ "3"

operation("4", "5", "subtract") ➞ "-1"

operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as strings, and you should also 
return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide, go ahead and round down to an integer."""

variable1, variable2, variable3 = "14", "2", "divide"
if variable3 == "add":
    print(int(float(variable1) + float(variable2)))
    # if float(variable1) / float(variable2)
elif variable3 == "subtract":
    print(int(float(variable1) - float(variable2)))
elif variable3 == "multiplied":
    print(int(float(variable1) * float(variable2)))
elif variable3 == "divide":
    print(int(float(variable1) / float(variable2)))
else:
    print("Undefined")

"""9. Check if the given string consists of only letters and spaces 
and if every letter is in lower case.

Examples
letters_only("PYTHON") ➞ False
letters_only("python") ➞ True
letters_only("12321313") ➞ False
letters_only("i have spaces") ➞ True
letters_only("i have numbers(1-10)") ➞ False
letters_only("") ➞ False
Notes
Empty arguments will always return False.
Input values will be mixed (symbols, letters, numbers)."""

string = input("Enter a string: ")

if all(item.isalpha() and item.islower() or item.isspace() for item in string):
    print("True")
else:
    print("False")

"""10. Write a function that takes a list and determines whether 
it's strictly increasing, strictly decreasing, or neither.

Examples
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
Input lists have a minimum length of 2."""

num_list = [-11, 1, 14, 17, 21, 49]
if all(i < j for i, j in zip(num_list, num_list[1:])):
    print("increasing")
elif all(i > j for i, j in zip(num_list, num_list[1:])):
    print("decreasing")
else:
    print("neither")