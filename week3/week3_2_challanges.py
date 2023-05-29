"""Week3_2"""
# 1. Emmy has written a function that returns a greeting to users.
# However, she's in love with Mubashir, and would like to greet him
# slightly differently. She added a special case in her function, but
# she made a mistake.
# Can you help her?
# Examples
# "Matt" ➞ "Hello, Matt!"
# "Helen" ➞ "Hello, Helen!"
# "Mubashir" ➞ "Hello, my Love!"

#version1
name = input("Hi! What's your name?")
others = "Hello," + name
LOVER = "Hello, my love!"
print((others * (name != "Mubashir")) + (LOVER * (name == "Mubashir")))

#version2
name = input("Hi! What's your name?")
res = name == "Mubashir"
print((("Hello, " + name) * (not res)) + (("Hello, my love") * res))

# 2. Create a function that takes two arguments.
# Both arguments are integers, a and b.
# Return True if one of them is 10 or if their sum is 10.
# Examples
# a,b = 9, 10 ➞ True
# a,b = 9, 9 ➞ False
# a,b = 1, 9 ➞ True

a = int(input("a = "))
b = int(input("b = "))
print((a + b == 10) or (a == 10) or (b == 10))

# 3. Create a function that returns True if
# an integer is evenly divisible by 5, and False otherwise.
# Examples
# 5 ➞ True
# -55 ➞ True
# 37 ➞ False

num = int(input("Please, enter a number evenly divisible by 5 "))
print(num % 5 == 0)

# 4. Extra Knowledge
# Create a function that takes two strings as arguments
# and return either True or False depending on whether
# the total number of characters in the first string is equal
# to the total number of characters in the second string.
# Examples
# "AB", "CD" ➞ True
# "ABC", "DE" ➞ False
# "hello", "edabit" ➞ False

# version1
NAME = "Shushanik"
SURNAME = "Manukyan"
print(len(NAME) == len(SURNAME))

# version2
your_name = input("Your name: ")
your_surname = input("Your surname: ")
print(len(your_name) == len(your_surname))

# 5. Given a string, return True if its length is even or
# False if the length is odd.

GIVEN_WORD = "Antananarivo"
print(((len(GIVEN_WORD)) % 2) == 0)

# version2
word = input("Please, type a word! ")
print(((len(word)) % 2) == 0)

# 6. Create a function that takes a string txt and a number n
# and returns the repeated string n number of times.
# If given argument txt is not a string, return Not A String !!
# Examples
# "Mubashir", 2 ➞ "MubashirMubashir"
# "Matt", 3 ➞ "MattMattMatt"
# 1990, 7 ➞ "Not A String !!"

#version1
text, repeat = "4", 12345
key = isinstance(text) == str
print(text * repeat * key, "Not a String!" * (not key))

#version2
text, repeat = "Dream", 42
print("Not a string!" * isinstance(text, int) + str(text * repeat) * isinstance(text, str))

#version3 is not working
text = input("Please, enter a text! ")
num = int(input("How many times to repeat? "))
key = isinstance(text) == str
output = text * num
print((output * key), ("Not a string!" * (output != key)))
