"""Practice"""
# 1. Create a function that takes a string and returns it as an integer.

# Examples
# "6" ➞ 6
# "1000" ➞ 1000

# Notes
# All numbers will be whole.
# All numbers will be positive.

string = input("Enter a number: ")
integer = int(string)
print(integer)
# print(type(integer))

# 2. Create a function that takes a boolean variable flag and returns it
# as a string.

# Examples
# True ➞ "True"
# False ➞ "False"

bool_flag = False
string_flag = str(bool_flag)
# print(type(bool_flag))
print(string_flag)
# print(type(string_flag))

# 3. Write a function that returns the string "something" joined with a
# space " " and the given argument a.

# Examples
# "is better than nothing" ➞ "something is better than nothing"

# "Bob Jane" ➞ "something Bob Jane"

# "something" ➞ "something something"

a = input("something ...")
STRING = "something"
print(f"{STRING} {a}")
print(STRING + " " + a)

# 4. Luke Skywalker has family and friends. Help him remind them who is who.
# Given a string with a name, return the relation of that person to Luke.

# Person	Relation
# Darth Vader	father
# Leia	sister
# Han	brother in law
# R2D2	droid

# Examples
# "Darth Vader" ➞ "Luke, I am your father."
# "Leia" ➞ "Luke, I am your sister."
# "Han" ➞ "Luke, I am your brother in law."

name = input("What is your name? ")
ANSWER = "Luke, I am your "
dad = "Darth Vader" == name
sis = "Leia" == name
bro = "Han" == name
dr = "R2D2" == name
print(ANSWER + (dad * "father" + sis * "sister" + bro * "brother in law" + dr * "droid"))


# 5. Create a function that takes a string and returns the number (count)
# of vowels contained within it.

# Examples
# "Celebration" ➞ 5
# "Palm" ➞ 1
# "Prediction" ➞ 4

# Notes
# a, e, i, o, u are considered vowels (not y).

word = input("Enter a word: ")
word = word.lower()
a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")
print(a + e + i + o + u)

# EXTRA Knowledge
# 6. Create a function that returns True if a given inequality expression
# is correct and False otherwise.

# Examples
# "3 < 7 < 11" ➞ True
# "13 > 44 > 33 > 1" ➞ False
# "1 < 2 < 6 < 9 > 3" ➞ True

exp = "3 < 7 < 11"
print(eval(exp))

# 7. Create a function that replaces all the vowels in a string with a specified character.

# Examples
# "the aardvark", "#" ➞ "th# ##rdv#rk"
# "minnie mouse", "?" ➞ "m?nn?? m??s?"
# "shakespeare", "*" ➞ "sh*k*sp**r*"

string = input("Please, enter a word: ")
string = string.replace("a", "^")
string = string.replace("A", "^")
string = string.replace("e", "^")
string = string.replace("E", "^")
string = string.replace("o", "^")
string = string.replace("O", "^")
string = string.replace("i", "^")
string = string.replace("I", "^")
string = string.replace("u", "^")
string = string.replace("U", "^")
print(string)

# 8. Write a function that takes a credit card number and only displays
# the last four characters. The rest of the card number must be replaced by ************.

# Examples
# "1234123456785678" ➞ "************5678"
# "8754456321113213" ➞ "************3213"
# "35123413355523" ➞ "**********5523"

card_num = input("Card Number: ")
cond = card_num.isdigit()
card_rep = card_num.replace(card_num[:-4], ((len(card_num) - 4) * "*"))
print(card_rep * cond + ((not cond) * "Please, enter only digits!"))

# 9. Create a function that takes a string (will be a person's first and
# last name) and returns a string with the first and last name swapped.

# Examples
# "Donald Trump" ➞ "Trump Donald"
# "Rosie O'Donnell" ➞ "O'Donnell Rosie"
# "Seymour Butts" ➞ "Butts Seymour"

name = input("Full name: ")
cond = name == name.title()
change_name = name.split(" ")
change_name = change_name[::-1]
note = "The first letters should be uppercase!"
change_name = " ".join(change_name)
print(change_name * cond + (not cond) * note)

# 10. An isogram is a word that has no duplicate letters.
# Create a function that takes a string and returns either
# True or False depending on whether or not it's an "isogram".

# Examples
# "Algorism" ➞ True
# "PasSword" ➞ False
# "Consecutive" ➞ False

# Not case sensitive.

word = input("Please, enter a word: ")
word = word.lower()
print(len(word) == len(word.set))

# 11. Create a function to test if a string is a valid pin or not.

# A valid pin has:
# *Exactly 4 or 6 characters.
# *Only numerical characters (0-9).
# *No whitespace.

# Examples
# valid("1234") -> True
# valid("45135") -> False
# valid("89abc1") -> False
# valid("900876") -> True
# valid(" 4983") -> False

# Notes
# Empty strings should return False when tested.

pin = input("Please, enter a pin: ")
cond_1 = len(pin) == 4 or len(pin) == 6
cond_2 = pin.isdigit()
cond_3 = pin.isspace()
print(bool(cond_1 * cond_2 * (not cond_3)))
