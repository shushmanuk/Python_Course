"""1. For this challenge, you are supposed to find the sum of the digits of a 
two-digit number.
45 ➞ 9
38 ➞ 11
67 ➞ 13 """

num = int(input("What is you two digit number? "))
print(num // 10 + num % 10)

"""Need extra knowledge!! 
2. A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
44 ➞ True
45 ➞ False
-44 ➞ False"""

num = int(input("Enter a two-digit integer. "))
print(num // 10 == num % 10)

"""3. Write a function that takes an integer minutes and converts it to seconds.
5 ➞ 300
2 ➞ 120"""

minute = int(input("minutes = "))
print(min * 60)

"""4. Create a function that takes the age in years and returns the age in days.
65 ➞ 23725
0 ➞ 0
20 ➞ 7300"""

age = int(input("Your age: "))
print(age * 365 + age // 4)

"""5. Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
1,3 ➞ 3780
2,0 ➞ 7200"""

hours, minutes = int(input("hours: ")), int(input("minutes: "))
print(hours * 3600 + minutes * 60)

"""6. Create a function that accepts a measurement value in inches and returns 
the equivalent of the measurement value in feet."""

inches = int(input("inches: "))
print(inches * 1/12)

"""7. Create a function that takes a number as an argument and returns "even" 
for even numbers and "odd" for odd numbers."""

num = int(input("number: "))
print((num % 2 == 0) * "even" + (num % 2 != 0) * "odd")
