"""
1. Given a list, rotate the values clockwise by one
(the last value is sent to the first position).
Check the examples for a better understanding.
Examples
[1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
[6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
[20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8] """

list_of_numbers = [4, 8, 14, 18, 24, 28]
final_list = list_of_numbers[-1:] + list_of_numbers[:-1]
print(final_list)

# """
# 2. Create a function that inverts the rgb values of a given tuple.
# Examples
# color_invert((255, 255, 255)) ➞ (0, 0, 0)
# # (255, 255, 255) is the color white.
# # The opposite is (0, 0, 0), which is black.
# color_invert((0, 0, 0)) ➞ (255, 255, 255)
# color_invert((165, 170, 221)) ➞ (90, 85, 34)
# Notes
# Must return a tuple.
# 255 is the max value of a single color channel. """

max_value = 255
color = (123, 23, 100)
color_invert = (max_value - color[0], max_value - color[1], max_value - color[2])
print(tuple(color_invert))

# """
# 3. Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.
# Examples
# find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
# find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
# find_bob(["Jimmy", "Layla", "James"]) ➞ -1
# Notes
# Assume all names start with a capital letter and are lowercase thereafter
# (i.e. don't worry about finding "BOB" or "bob")."""

names = ["Noah", "Adam", "Neriah", "Luna"]
condition = "Bob" in names and names.index("Bob")
print((not condition and isinstance(condition, bool) * -1) + condition)

# """
# EXTRA Knowledge
# 4. Given a list of numbers, write a function that returns a list that...
# Has all duplicate elements removed.
# Is sorted from least to greatest value.
# Examples
# unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
# unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
# unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7] """

numbers = [7, 9, 14, -5, 22, 0, 7]
unique_sort = list(set(numbers))
print(sorted(unique_sort))

# """
# EXTRA Knowledge
# 5. Given two strings, create a function that returns the total number
# of unique characters from the combined string.
# Examples
# count_unique("apple", "play") ➞ 5
# # "appleplay" has 5 unique characters:
# # "a", "e", "l", "p", "y"
# "sore", "zebra" ➞ 7
# "a", "soup" ➞ 5 """
#version1
two_strings = ['Eyjafjallajökull', 'Reykjavik']
result = two_strings[0] + two_strings[1]
print(set(result))
#version2
two_strings = ['Baraboom', 'Reykjavik']
one_string = ''.join(two_strings)
result = one_string.lower()
print(len(set(result)))
#version3
two_strings = ['Eyjafjallajökull', 'Reykjavik']
result = two_strings[0] + two_strings[1]
print(len(dict.fromkeys(result)))

# """
# 6. Create a function that takes a dictionary of student names and returns
# a list of student names in alphabetical order.
# Examples
# {
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# } ➞ ["Becky", "John", "Steve"] """

student_dict = {
    "Levon" : 1,
    "Vahe" : 2,
    "Anna" : 3,
    "Aspram" : 4,
    "Ori" : 5,
}
student_list = list(student_dict.keys())
print(sorted(student_list))

# """
# 7. Create a function that returns a list of strings sorted by length in ascending order.
# Examples
# sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
# sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
# sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
# sort_by_length([]) ➞ []
# Notes
# Strings will have unique lengths, so don't worry about comparing two strings with
# identical length.
# Return an empty array if the input array is empty """

months = ["Navasard", "Hori", "Sahmi", "Tre"]
ord_months = sorted(months, key=len)
print(ord_months)

# """
# 8. Write a function that converts a dictionary into a list of keys-values tuples.
# Examples
# dict_to_list({
#   "D": 1,
#   "B": 2,
#   "C": 3
# }) ➞ [("B", 2), ("C", 3), ("D", 1)]

# dict_to_list({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]"""

book_dict = {
    "Week1": 2,
    "Week2": 5,
    "Week3": 4,
    "Week4": 6
}
print("Readings' dictionary is:", book_dict)
books = book_dict.items()
book_list = list(books)
print("Readings' list is:", book_list)

# """
# 9. Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# """
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict.get("class").get("student").get("marks").get("history"))

# """
# 10. Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
# Given:
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# Expected output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'} """

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)
