""" 1. Create a function that takes a string and returns it as an integer.

Examples
"6" ➞ 6
"1000" ➞ 1000

Notes
All numbers will be whole.
All numbers will be positive.
"""
#version1
num = "123"
print(int(num))

#version2
num = input("\nPlease, enter a number! ")
int_num = int(num)
print(int_num)


""" 2. Create a function that takes a boolean variable flag and returns it as a string.

Examples
True ➞ "True"

False ➞ "False"
"""

bool_flag = input("Enter True or False: ")
print(str(bool_flag == "False") and str(bool_flag == "True"))


""" 3. Write a function that returns the string "something" joined with a space " " and the given argument a.

Examples
"is better than nothing" ➞ "something is better than nothing"
"Bob Jane" ➞ "something Bob Jane"
"something" ➞ "something something"
"""
text_input = input("\nWrite something ")
text_given = "something"
output = f"{text_given} {text_input}"
print(output)


""" 4. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid

Examples
"Darth Vader" ➞ "Luke, I am your father."
"Leia" ➞ "Luke, I am your sister."
"Han" ➞ "Luke, I am your brother in law."
"""
relative_name = input("\nWhat's your name? ")
text = "Luke, I am your "
father = relative_name == "Darth Vader"
sister = relative_name == "Leia"
brother_in_law = relative_name == "Han"
droid = relative_name == "R2D2"
print(((text + "father") * father) + ((text + "sister") * sister) + ((text + "brother in law") * brother_in_law) + ((text + "droid") * droid))


""" 5. Create a function that takes a string and returns the number 
(count) of vowels contained within it.

Examples
"Celebration" ➞ 5

"Palm" ➞ 1

"Prediction" ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).

EXTRA Knowledge
"""
#version1
new_word = input("\nPlease, write a word! ")
word = new_word.lower()
a = word.count("a") 
e = word.count("e") 
i = word.count("i") 
o = word.count("o") 
u = word.count("u") 
print(a + e + i + o + u)


""" 6. Create a function that returns True if a given inequality 
expression is correct and False otherwise.

Examples
"3 < 7 < 11" ➞ True

"13 > 44 > 33 > 1" ➞ False

"1 < 2 < 6 < 9 > 3" ➞ True
"""

#version1
inequality = input("\nType an inquality test: ")
output = eval(inequality)
print(output)

#version2
inequality = (12 < 13 <= 13)
print(inequality)


""" 7. Create a function that replaces all the vowels in a string with 
a specified character.

Examples
"the aardvark", "#" ➞ "th# ##rdv#rk"

"minnie mouse", "?" ➞ "m?nn?? m??s?"

"shakespeare", "*" ➞ "sh*k*sp**r*"
"""
vowels_word = input("\nType your word here: ")
new_word = vowels_word.replace("A", "^").replace("a", "^").replace("I", "^").replace("i", "^").replace("U", "^").replace("u", "^").replace("E", "^").replace("e", "^").replace("O", "^").replace("o", "^")
print(new_word)


""" 8. Write a function that takes a credit card number and only displays 
the last four characters. The rest of the card number must be replaced 
by ************.

Examples
"1234123456785678" ➞ "************5678"

"8754456321113213" ➞ "************3213"

"35123413355523" ➞ "**********5523"
"""
card_number = input("\nPlease, enter a 16-digit number: ")
output = "************" + card_number[-4:]
limit = len(card_number) == 16
print((output * limit) + ("Please, try again" * (not limit)))


""" 9. Create a function that takes a string will be a person's first 
and last name) and returns a string with the first and last name swapped.

Examples
"Donald Trump" ➞ "Trump Donald"
"Rosie O'Donnell" ➞ "O'Donnell Rosie"
"Seymour Butts" ➞ "Butts Seymour"
"""
#version1
full_name = input("\nWhat's your name? ")
name = full_name.split()
print(name[1] + " " + name[0])

#version2
color = input("\nName a color, a drink, and a country: ")
c = color.split()
print(c[2] + " " + c[0] + " " + c[1])

#version3
first_name = input("\nPlease, enter your first name. ")
last_name = input("And, what is your last name? ")
name = f"{last_name} {first_name}"
print(name)


""" 10. An isogram is a word that has no duplicate letters. 
Create a function that takes a string and returns either 
True or False depending on whether or not it's an "isogram".

Examples
"Algorism" ➞ True
"PasSword" ➞ False
# Not case sensitive.
"Consecutive" ➞ False
"""
input_word = input("Type a word: ")
isogram = len(set(input_word)) >= len(input_word)
print(isogram)


""" 11. Create a function to test if a string is a valid pin or not.

A valid pin has:
*Exactly 4 or 6 characters.
*Only numerical characters (0-9).
*No whitespace.

Examples
valid("1234") -> True
valid("45135") -> False
valid("89abc1") -> False
valid("900876") -> True
valid(" 4983") -> False

Notes
Empty strings should return False when tested.
"""
password = input("\nEnter a 4 or 6-digit password with no whitespase: ")
p_word = password.isdigit()
valid_1 = password.isalnum()
valid_2 = len(password) == 4 or len(password) == 6
valid_3 = all(p_word.isdigit() for p_word in password)
print(valid_1 and valid_2 and valid_3)