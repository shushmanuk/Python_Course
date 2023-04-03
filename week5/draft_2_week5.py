# x = {5, 7, 23, 11, 7}
# print(x)
# print(x.pop())
"""
lst1, lst2, lst3 = [14, 7, 9, 6, 0], [3, 4, 14, 6, 7, 5, 3], [5, 6, 7, 0, 14, 6]
lst4 = list(set(lst1).intersection(lst2))
lst5 = list(set(lst4).intersection(lst3))
print(sum(lst5))
"""
# lst = [24, 12, 0, -9, 21, 8, 6, -1, 3]
# num = 0
# element1 = list((lst[0] % 2) == 0)
# print(element1)

# note_dict = {"name": "Daniel", "notes": [7, 6, 8]}
# top_note = note_dict.notes.max()
# print(top_note)


# num = int(input("Please, enter a number to check if it\'s harshad: "))
# temp = num
# length = []
# sum1 = 0
# while (num > 0):
#     sum2 = num % 10
#     length.append(sum2)
#     num = num // 10
# sum1 = sum(length)
# if(temp % sum1 == 0):
#     print("True")
# else:
#     print("False")

    
# set1 = {7, 14, 21, 28, 35}
# set2 = {12, 14, 22, 24, 26, 28}
# print(set1.union(set2))



# pin = input("Please, type 4 or 6-digit password /no whitespace/: ")
# valid_pin = pin.isdigit()
# validation1 = len(pin) == 4 or len(pin) == 6
# validation2 = pin.isalnum()
# validation3 = pin.isspace()
# print(validation1 and validation2 and (not validation3))


# set1 = {11, 22, 33, 44, 55, 66, 77}
# set2 = {10, 11, 30, 33, 50, 55, 60}
# print(set1.intersection(set2))

# set1 = {7, 17, 177, 1717}
# set2 = {15, 17, 150, 170}
# print(set1.difference(set2))

# new_string = input("Please, write a sentence: ")
# words = new_string.split(" ")
# string = []
# for word in words:
#     string.insert(0, word)
# print(" ".join(string))

# string = input("Please, write a sentence: ")
# words = string.split(" ")[::-1]
# print(" ".join(words))

# string = input("Please, write a sentence: ")
# words = string[::-1]
# print("".join(words))

# profit = {
#     "cost_price" : (float(input("Please, enter a cost price: "))),
#     "sell_price" : (float(input("Please, enter a sell price: "))),
#     "inventory" : (int(input("Please, enter an inventory: ")))
# }

# print(int((profit.get("sell_price") - profit.get("cost_price")) * (profit.get("inventory"))))

# note_dict = {
#     "name": "Mark",
#     "notes": [6, 8, 8]
# }
# max_note = note_dict.get("notes")
# max_note = max(max_note)
# del note_dict["notes"]
# note_dict["top_note"] = max_note
# print(note_dict)

# new_list = [12, 24, 33, 36, 11, 0, -9]
# even_list = [even for even in new_list if even % 2 != 0]
# odd_list = [odd for odd in new_list if odd % 2 == 0]
# print([sum(even_list), sum(odd_list)])

# letters, indexes = ["k", "o", "b", "o"], [2, 1, 3, 0]
# for i in indexes:
#     print(letters[i])

# letters, indexes = ["b", "k", "o", "o"], [0, 2, 3, 1]
# letters = [letters[i] for i in indexes]
# print(letters)          

# note_dict = {
#     "name": "Mark",
#     "notes": [6, 8, 8]
# }
# max_note = note_dict.get("notes")
# del note_dict["notes"]
# note_dict["top_note"] = max(max_note)
# print(note_dict)


# note_dict = {
#     "name": "Mark",
#     "notes": [6, 8, 8]
# }
# note_dict["top_note"] = max(note_dict.pop("notes")) 
# print(note_dict)