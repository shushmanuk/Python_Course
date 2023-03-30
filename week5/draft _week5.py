# date = "11/12/2019"
# numbers = date.replace("/", ",")
# result = (str(list(numbers)))
# print(result)

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
"""
"""
# lst = list(input("Please, enter a list of numbers: "))
# srt = input("Please, enter a sort of ordering:\n\"Asc\":a list in ascending order.\n\"Des\":a list in descending order.\n\"None\": a list without any modification.")
# srt = srt.capitalize()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

# print(x)


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# sample_dict["Paris"] = sample_dict.pop("New york") 

# rgb_color = ("white" = (255, 255, 255),"black":(0, 0, 0),)
# list_of_names = list(["Noah", "Adam", "Neriah", "Luna"])
# find_name = list_of_names
# print(find_name)


# lst = input("Please, enter a list of numbers: ")
# srt = input("Please, enter a sort of ordering:\n\"Asc\":a list in ascending order.\n\"Des\":a list in descending order.\n\"None\": a list without any modification.")
# srt = srt.capitalize()
# lst1 = lst.split()
# lst2 = int(lst1[0]), int(lst1[1]), int(lst1[2]), ... , int(lst1[-1])
# print(lst2)

# max_value = 255
# new_color = (123, 23, 100)
# color_invert = (max_value - new_color[0], max_value - new_color[1], max_value - new_color[2])
# print(tuple(color_invert))
""" sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict) """

# list_of_names = ["Noah", "Adam", "Neriah", "Luna"]
# find_name = list_of_names.pop("Bob", -1)
# print(find_name)
"""
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
print(sampleDict.get("marks"))"""

"""book_dict = {
    "Week1": 2,
    "Week2": 5,
    "Week3": 4,
    "Week4": 6
}
print("Readings' dictionary is:", book_dict)
books = book_dict.items()
book_list = list(books)
print("Readings' list is:", book_list)"""

# months = ["Navasard", "Hori", "Sahmi", "Tre"]
# ord_months = sorted(months, key=len)
# print(ord_months)

#6.
# student_dict = {
#     "Levon" : 1,
#     "Vahe" : 2,
#     "Anna" : 3,
#     "Aspram" : 4,
#     "Ori" : 5,
# }
# student_list = list(student_dict.keys())
# print(sorted(student_list))

"""5. Given two strings, create a function that returns the total number of unique characters from the combined string.
"""

# two_strings = ['Eyjafjallajökull', 'Reykjavik']
# one_string = ''.join(two_strings)
# result = one_string.lower()
# print(len(set(result)))

# 4.
# numbers = [7, 9, 14, -5, 22, 0, 7]
# unique_sort = list(set(numbers))
# print(sorted(unique_sort))


names = ["Noah", "Adam", "Neriah", "Luna"]
find_index = names.index("Bob")
condition = "Bob" in names
print((find_index * condition), (find_index * (not condition) * (-1)))

"""HELPFUL
# Sort string by integer value use key as int
strings = ['12','34','5','26','76','18','63']
strings.sort(key = int)
print(strings)

# Sorted string by integer value use key = int
strings = sorted(strings, key=int)
print(strings)

# Output:
# ['5', '12', '18', '26', '34', '63', '76']



# Sort in descending order 
technology = ['Java','Hadoop','Spark','Pandas','Pyspark','NumPy','Hyperion']
technology.sort(reverse = True)
print(technology)

# Sorted list of strings in descending order
technology = ['Java','Hadoop','Spark','Pandas','Pyspark','NumPy','Hyperion']
technology = sorted(technology, reverse=True)
print(technology)

# Output
# ['Spark', 'Pyspark', 'Pandas', 'NumPy', 'Java', 'Hyperion', 'Hadoop']
END"""