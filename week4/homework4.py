"""
1. Create a function that takes a list containing only numbers and return the first element.
Examples
[1, 2, 3] ➞ 1
[80, 5, 100] ➞ 80
[-500, 0, 50] ➞ -500
"""
numbers = [23, 25, 2, 27, 8, 29, 30, 1]
print(numbers[0])

"""
2.  Create a function that takes a list of numbers. Return the largest number in the list.

Examples
[4, 5, 1, 3] ➞ 5
[300, 200, 600, 150] ➞ 600
[1000, 1001, 857, 1] ➞ 1001
"""
numbers = [14, 12, -95, 47, 20, 10, 1, 3, 12, -47, 90]
print(max(numbers))

"""
3. Create a function that takes a list of numbers and returns the smallest number in the list.

Examples
[34, 15, 88, 2] ➞ 2
[34, -345, -1, 100] ➞ -345
[-76, 1.345, 1, 0] ➞ -76
[0.4356, 0.8795, 0.5435, -0.9999] ➞ -0.9999
[7, 7, 7] ➞ 7
"""
numbers = [14, 12, -95, 47, 20, 10, 1, 3, 12, -47, 90]
print(min(numbers))

"""
4. Create a function that takes a list and returns the difference between the biggest and smallest numbers.

Examples
[10, 4, 1, 4, -10, -50, 32, 21] ➞ 82
# Smallest number is -50, biggest is 32.

[44, 32, 86, 19] ➞ 67
# Smallest number is 19, biggest is 86.
"""
numbers = [14, 12, -95, 47, 20, 10, 1, 3, 12, -47, 90]
print(max(numbers) - min(numbers))

"""
5. Create a function to concatenate two integer lists.

Examples
[1, 3, 5], [2, 6, 8] ➞ [1, 3, 5, 2, 6, 8]

[7, 8], [10, 9, 1, 1, 2] ➞ [7, 8, 10, 9, 1, 1, 2]

[4, 5, 1], [3, 3, 3, 3, 3] ➞ [4, 5, 1, 3, 3, 3, 3, 3]
"""
list_one = [10, 72, 12, 1, 1, -5]
list_two = [24, 84, 4, 11, -7, 0, -8, 6, 3]
print(list_one + list_two)
"""

6. Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.

Examples
[5, 57] ➞ True

[77, 30] ➞ False

[0] ➞ True
"""
numbers = [10, 20, -6, 9, -82, 60, 28]
print(sum(numbers) <= 100)

"""
7. Given a list of integers, determine whether the sum of 
its elements is even or odd.
The return value should be a string "odd" or "even".
If the input list is empty, consider it as a list with a zero [0].

Examples
[0] ➞ "even"
[1] ➞ "odd"
[] ➞ "even"
[0, 1, 5] ➞ "even"
"""
numbers = []
result = sum(numbers) % 2 == 0
print("odd" * (not result) + "even" * result)

"""
8. Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
Examples
"11/12/2019" ➞ "20191211"

"12/31/2019" ➞ "20193112"

"01/15/2019" ➞ "20191501"
"""
date = "14/06/1995"
date = date.replace("/", "")
day, month, year = date[:2], date[2:4], date[4:]
print(year, month, day)

"""
EXTRA Knowledge
9. Create a function that takes two numbers as arguments num, length and returns a list of multiples of num until the list length reaches length.

Examples
7, 5 ➞ [7, 14, 21, 28, 35]
12, 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
17, 6 ➞ [17, 34, 51, 68, 85, 102]
"""
numbers, lengths = 3, 12
while numbers <= 10:
    print(numbers * lengths)
    numbers += 1
"""
10. Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:

"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification.
Examples
[4, 3, 2, 1], "Asc"  ➞ [1, 2, 3, 4]
[7, 8, 11, 66], "Des" ➞ [66, 11, 8, 7]
[1, 2, 3, 4], "None" ➞ [1, 2, 3, 4]
"""
#version1 is not complete !!!
# lst = list(input("Please, enter a list of numbers: "))
# srt = input("Please, enter a sort of ordering:\n\"Asc\":a list in ascending order.\n\"Des\":a list in descending order.\n\"None\": a list without any modification.")
# srt = srt.capitalize()
# lst2 = sorted(lst)
# lst3 = sorted(lst2, reverse = True)
# lst = [2, 4, 1, 3, 2, 1, 0, 6]
# print(((srt == "Asc") * lst2) + (srt == "Des" * lst3))
# srt = srt == "Des"
# lst.reverse()
# print(lst2 * srt)
# print(((sort == "Asc") * asc) + ((sort == "Des") * des) + ((sort == "None") * input_l)) 
# version2
lst = [41, 83, -7, 19, 0, 24, 7.3]
s = list("kapkulibrary")
print(sorted(lst, key=lambda x: x))
