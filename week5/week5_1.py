"""Practice"""
# 1. Given a list, rotate the values clockwise by one
# (the last value is sent to the first position).
# Check the examples for a better understanding.

# Examples
# [1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
# [6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
# [20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]

lst = [24, 34, 44, 54, 14]
lst1 = [lst[-1]]
print(lst1 + lst[:-1])

# 2. Create a function that inverts the rgb values of a given tuple.

# Examples
# color_invert((255, 255, 255)) ➞ (0, 0, 0)
# # (255, 255, 255) is the color white.
# # The opposite is (0, 0, 0), which is black.
# color_invert((0, 0, 0)) ➞ (255, 255, 255)
# color_invert((165, 170, 221)) ➞ (90, 85, 34)
# Notes
# Must return a tuple.
# 255 is the max value of a single color channel.

color_invert = (255, 205, 55)
print((255 - color_invert[0], 255 - color_invert[1], 255 - color_invert[2],))

# 3. Write a function that searches a list of names
# (unsorted) for the name "Bob" and returns the location in the list.
# If Bob is not in the list, return -1.

# Examples
# find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
# find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
# find_bob(["Jimmy", "Layla", "James"]) ➞ -1
# Notes
# Assume all names start with a capital letter and are lowercase thereafter
# (i.e. don't worry about finding "BOB" or "bob").

find_bob = ["Mag", "Bob", "Simon", "Sam", "Jack", "Tom"]
bob_is = "Bob" in find_bob
bob_index = bob_is and find_bob.index("Bob")
cond = isinstance(bob_is, bool)
print(((not bob_is) and cond * -1) + bob_index)

# EXTRA Knowledge
# 4. Given a list of numbers, write a function that returns a list that...

# Has all duplicate elements removed.
# Is sorted from least to greatest value.
# Examples
# unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
# unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
# unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]

unique_sort = [10, 11, 20, 21, 8, 10, 11]
unique_sort = set(sorted(unique_sort))
print(list(unique_sort))

# EXTRA Knowledge
# 5. Given two strings, create a function that returns the total number of
# unique characters from the combined string.

# Examples
# count_unique("apple", "play") ➞ 5
# # "appleplay" has 5 unique characters:
# # "a", "e", "l", "p", "y"
# "sore", "zebra" ➞ 7
# "a", "soup" ➞ 5

count_unique = ("a", "sooouuuulmup")
combined = "".join(count_unique)
total_number = len(set(combined))
print(total_number)

# #when we have only two strings
# count_unique = ("a", "sooouuuulmup")
# combined = list(count_unique[0] + count_unique[1])
# total_number = len(set(combined))
# print(total_number)

# 6. Create a function that takes a dictionary of student names and returns
# a list of student names in alphabetical order.

# Examples
# {
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# } ➞ ["Becky", "John", "Steve"]

students = {
    "Student 1" : "Max",
    "Student 2" : "Alice",
    "Student 3" : "Noah",
    "Student 4" : "Neriah",
}
student_list = students.values()
sorted_list = list(sorted(student_list))
print(sorted_list)

# 7. Create a function that returns a list of strings sorted by length in ascending order.

# Examples
# sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
# sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
# sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
# sort_by_length([]) ➞ []
# Notes
# Strings will have unique lengths, so don't worry about comparing two strings with
# identical length.
# Return an empty array if the input array is empty

sort_by_length = ["mama", "mayrik", "mam", "mamulik", "ma"]
sorted_list = sorted(sort_by_length, key=len)
print(sorted_list)


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
# }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]

dict_to_list = {
    "M": 1,
    "M2": 2,
    "M3": 3,
}
print(list(dict_to_list.items()))

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
print(sampleDict["class"]["student"]["marks"]["history"])


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

# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york",
}
val = sample_dict.get("city")
del sample_dict["city"]
sample_dict["location"] = val
print(sample_dict)
