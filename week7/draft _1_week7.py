# numm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# for i in numm:
#     print(i, "->", i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11)

# name = input("What's your name? ")
# if name == "Darth Vader":
#     print("Luke, I am your father.")
# elif name == "Leia":
#     print("Luke, I am your sister.")
# elif name == "Han":
#     print("Luke, I am your brother in law.")
# elif name == "R2D2":
#     print("Luke, I am your droid.")
# else:
#     print("We are not relatives")

# damage, speed, time = 140, 1, "hour"
# total_damage = damage * speed
# if total_damage >= 0:
#     if time == "second":
#         print(total_damage * 1)
#     elif time == "minute":
#         print(total_damage * 60)
#     elif time == "hour":
#         print(total_damage * 3600)
# else:
#     print("invalid")

# my_list = ["s", 0, 4, 14, "m", -11, "h", 41]
# for item in my_list:
#     if isinstance(item, int):
#         print(item)

# number = int(input("Type a symmetrical number: "))
# if number == int(str(number)[::-1]):
#     print("True")
# else:
#     print("False")

# change_list = [False, "book", 5, 6, "hey", True, "true"]
# for item in change_list:
#     if item % 2 == 0:
#         print(item + 1)
#     elif item % 2 != 0:
#         print(item)
    # elif item: isinstance(item, str) print(item.title + "!")
    # elif item: isinstance(item, bool)

# variable1, variable2, variable3 = "13", "2", "divide"
# if variable3 == "add":
#     print(int(float(variable1) + float(variable2)))
#     # if float(variable1) / float(variable2)
# elif variable3 == "subtract":
#     print(int(float(variable1) - float(variable2)))
# elif variable3 == "multiple":
#     print(int(float(variable1) * float(variable2)))
# elif variable3 == "divide":
#     print(int(float(variable1) / float(variable2)))
# else:
#     print("Undefined")

# string = input("Enter a string: ")

# if all(item.isalpha() and item.islower() or item.isspace() for item in string):
#     print("True")
# else:
#     print("False")


# num_list = [-11, 1, 14, 14, 17, 21, 49]
# if all(i < j for i, j in zip(num_list, num_list[1:])):
#     print("increasing")
# elif all(i > j for i, j in zip(num_list, num_list[1:])):
#     print("decreasing")
# else:
#     print("neither")

# 7.
# parameter1, parameter2 = 2, 5
# if isinstance(parameter1, str) and isinstance(parameter2, str):
#     print(int(parameter1) + int(parameter2))
# elif isinstance(parameter1, int) and isinstance(parameter2, int):
#     print(str(parameter1) + str(parameter2))
# else:
#     print("None")


# 3.
# mixed_list = ["4", 13, "mm", 7, -9, "bb"]
# # print(type(mixed_list))
# for item in mixed_list:
#     if isinstance(item, int):
#         print(item)
#     elif isinstance(item, str):
#         print("")


# 6.
# string = "antananarivo"
# str_list = list(string)
# if len(string) % 2 == 0:
#     print([i + j for i, j in zip(str_list[::2], str_list[1::2])])
# else:
#     str_list.append("*"[-1])
#     print([i + j for i, j in zip(str_list[::2], str_list[1::2])])

# var1, var2, oper = "13", "0", "divide"
# if oper == "add":
#     print(str(int(var1) + int(var2)))
# elif oper == "subtract":
#     print(str(int(var1) - int(var2)))
# elif oper == "multiple":
#     print(str(int(var1) * int(var2)))
# elif oper == "divide":
#     if int(var2) != 0:
#          print(str(int(int(var1) / int(var2))))
#     else: 
#         print("Undefined")




# var1, var2, oper = "13", "2.04", "divide"
# if not(var1.isnumeric() and var2.isnumeric()):
#     print("Please, enter numeric values!")
#     exit()
# var1, var2 = int(var1), int(var2)
# return_value = "Undefined"
# if oper == "add":
#     return_value = var1 + var2
# elif oper == "subtract":
#     return_value = var1 - var2
# elif oper == "multiple":
#     return_value = var1 * var2
# elif oper == "divide" and var2 != 0:
#     return_value = var1 // var2
# elif oper == "divide" and var2 == 0:
#     return_value = "var2 != 0"
# else: 
#     return_value = "Please, correct the operator name!"
# print(str(return_value))

change_list = ["0", 14, 22, True, "True", 11, "11"]

return_value = []

for item in change_list:
    if isinstance(item, str):
        return_value.append(item.capitalize()+ "!")
    elif isinstance(item, bool):
        return_value.append(not item)
    elif isinstance(item, int):
        if item % 2:
            return_value.append(item)
        else:
            return_value.append(item + 1)
print(return_value)    