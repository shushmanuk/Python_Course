""" 
1. Emmy has written a function that returns a greeting to users. 
However, she's in love with Mubashir, and would like to greet him 
slightly differently. She added a special case in her function, but 
she made a mistake.
Can you help her?
Examples
"Matt" ➞ "Hello, Matt!"
"Helen" ➞ "Hello, Helen!"
"Mubashir" ➞ "Hello, my Love!" 
"""

name = input("Hi! What's your name?" )
print(("Hello," + name) * (name != "Mubashir"))
print(("Hello, my love!") * (name == "Mubashir"))

""" 
2. Create a function that takes two arguments. 
Both arguments are integers, a and b. 
Return True if one of them is 10 or if their sum is 10.
Examples
a,b = 9, 10 ➞ True
a,b = 9, 9 ➞ False
a,b = 1, 9 ➞ True
"""
a = int(input("a = " ))
b = int(input("b = " ))
print((a + b == 10) or (a == 10) or (b == 10))

"""
3. Create a function that returns True if 
an integer is evenly divisible by 5, and False otherwise.
Examples
5 ➞ True
-55 ➞ True
37 ➞ False
"""
num = int(input("Please, enter a number evenly divisible by 5 "))
print(num % 5 == 0)

"""
4. Extra Knowledge 
Create a function that takes two strings as arguments 
and return either True or False depending on whether 
the total number of characters in the first string is equal 
to the total number of characters in the second string.
Examples
"AB", "CD" ➞ True
"ABC", "DE" ➞ False
"hello", "edabit" ➞ False
"""
#version1
my_name = "Shushanik"
my_surname = "Manukyan"
print(len(my_name) == len(my_surname))

#version2
your_name = input("Your name: ")
your_surname = input("Your surname: ")
print(len(your_name) == len(your_surname))
"""
5. Given a string, return True if its length is even or 
False if the length is odd.
""" 
given_word = "Antananarivo"
print((int(len(given_word)) % 2) == 0)

#version2
word = input("Please, type a word! ")
print((int(len(word)) % 2) == 0)

"""
6. Create a function that takes a string txt and a number n 
and returns the repeated string n number of times.
If given argument txt is not a string, return Not A String !!
Examples
"Mubashir", 2 ➞ "MubashirMubashir"
"Matt", 3 ➞ "MattMattMatt"
1990, 7 ➞ "Not A String !!" 
"""

text = input("Please, enter a text! ")
num = int(input("How many times to repeat? "))
print(text * num)