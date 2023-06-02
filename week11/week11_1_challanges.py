"""
1. Simple OOP Calculator
Create methods for the Calculator class that can do the following:

Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.
Examples
calculator = Calculator()

calculator.add(10, 5) ➞ 15

calculator.subtract(10, 5) ➞ 5

calculator.multiply(10, 5) ➞ 50

calculator.divide(10, 5) ➞ 2
Notes
The methods should return the result of the calculation.
Don't worry about needing to handle division by zero errors.
See the Resources tab for some helpful tutorials on Python classes."""

""" 2. Ones, Threes and Nines (Version #1)
Given an int, figure out how many ones, threes and nines you could fit 
into the number. You must create a class. You will make variables 
(self.ones, self.threes, self.nines) to do this.

Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0

n1.ones ➞ 5

n1.threes ➞ 1
Notes
Do not use the math module.
See version #2 of this series."""

"""
3. Classes For Fetching Information on a Sports Player
Create a class that takes the following four arguments for a particular 
football player:

name
age
height
weight
Also, create three functions for the class that returns the following strings:

get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"
Examples
 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"
Notes
name will be passed in as a string and age, height, weight will be integers."""

"""
4. Fullname and Email
Create the instance attributes fullname and email in the Employee class. 
Given a person's first and last names:

Form the fullname by simply joining the first and last name together, 
separated by a space.

Form the email by joining the first and last name together with a . 
in between, and follow it with @company.com at the end. Make sure the 
entire email is in lowercase.

Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"
emp_2.email ➞ "mary.sue@company.com"
emp_3.firstname ➞ "Antony"
Notes
The attributes firstname and lastname are already made for you.
See the Resources tab for some helpful tutorials on Python classes!"""

"""
5. Count Number of Instances
Create a class named User and create a way to check the number of users 
(number of instances) that were created, so that the value can be accessed 
as a class attribute.

Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"
Notes
Feel free to check out the resources provided in the Resources tab for some
helpful information on Python classes!"""

"""
6. Name Classes
Write a class called Name and create the following attributes given a first
name and last name (as fname and lname):

An attribute called fullname which returns the first and last names.
An attribute called initials which returns the first letters of the first and
last name. Put a . between the two letters.
Remember to allow the attributes fname and lname to be accessed individually
as well.

Examples
a1 = Name("john", "SMITH")
a1.fname ➞ "John"

a1.lname ➞ "Smith"

a1.fullname ➞ "John Smith"

a1.initials ➞ "J.S"
Notes
Make sure only the first letter of each name is capitalised.
Check the Resources tab for some helpful tutorials on Python classes."""

"""
7. Counting Instances Created from a Class
Write a Composer class that has three instance variables:

name
dob
country
Add an additional class variable .count which counts the total number of 
instances created.

Examples
# Just finished writing the Composer class
Composer.count ➞ 0

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
Composer.count ➞ 1

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
Composer.count ➞ 3
Notes
N/A"""

"""
8. Book Shelf
Create a Book class that has two attributes:

.title
.author
and two methods:

A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:

Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"
Notes
Read more about Python classes in Resources.
Remember, after you've finished writing the class and its methods, 
you must instantiate it through the creation of new objects."""

"""
9. Food for Everyone!
Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste():

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"
Notes
A person can have an empty list for foods they hate and/or love.
Check the Resources for some helpful tutorials on Python classes."""

"""
10. Big Countries
A country can be said as being big if it is:

Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. 
Set it to True if either criterea are met:

Population is greater than 250 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to 
another country object. Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}
Examples
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than
Australia"
Notes
Population density is calculated by dividing the population by the area.
Area is given in square km.
The input will be in the format (name_of_country, population, size_in_km2),
where name_of_country is a string and the other two inputs are integers."""