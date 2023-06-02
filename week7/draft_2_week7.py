# 1
# name = input("What's your name? ")
# num = int(input("Enter 0 or 1: "))
# if num == 1:
#     return_value = "Hello" + " " + name.title()
# elif num == 0:
#     return_value = "Bye" + " " + name.title()
# print(return_value)
   
# element_list = ["ss", "ss", "ss", "ss"]
# for item in element_list:
#     if item == element_list[0]:
#         print("True")
#     else:   
#         print("False")

"""
lst = [1, 2, 3, 4]
new = []
for i in lst:
    new.append(i**2)
print(new)

# or

lst = [1, 2, 3, 4]
new = [i**2 for i in lst]
print(new) """

# def number(num: int, string: str):
#     return(num * string)
# print(number(3, "sun"))
"""
rna_text = "AUGGC"
rna_converted = (
    rna_text.replace("A", "B")
    .replace("U", "A")
    .replace("B", "U")
    .replace("C", "B")
    .replace("G", "C")
    .replace("B", "G")
)[::-1]

print(rna_converted) """

# rna_dict = {"A": "U", "U": "A", "C": "G", "G": "C"}
# rna_converted = ""

# for item in rna_dict:
#     rna_converted += rna_dict[item]

# print(rna_converted[::-1])

hacker_key = {"a": "4", "s": "5", "o": "0", "i": "1", "e": "3"}
hacker_text = "have you thought about this hack?"

for item in hacker_key:
    hacker_text = hacker_text.replace(item, )