"""
letters = ["a", "b", "c", "d", "e", "f"]
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]]
fours = [4] * 12
combined = fours + letters
numbers = list(range(14))
chars = list("Hakuna, Matata")
print(chars)
print(len(chars))
print(combined)
print(numbers)
print(matrix)
print(matrix[0][1])
print(matrix[1][2])
letters = ["a", "b", "c", "d", "e", "f"]
letters[2] = "C"
print(letters[2:4])
print(letters[::-1])
new_list = list(range(24))
print(new_list)   
print(new_list[::3])
print(new_list[::-1])   
first, second, third, fourth, *other, last = new_list
print(fourth)
print(other)
print(first)
print(last)

letter = ["s", "m", "o", "x", "w", "c"]
for let in letter:
    print(let)

letter = ["s", "m", "o", "x", "w", "c"]
for let in enumerate(letter):
    print(let)

letter = ["s", "m", "o", "x", "w", "c"]
for index, let in enumerate(letter):
    print(index, let)

letter = ["s", "m", "o", "x", "w", "x", "c"]
letter.append("z")
letter.insert(3, "p")
# letter.pop()
# letter.pop(1)
# letter.remove("x")
# del letter[5]
# del letter[2:4]
# letter.clear()
print(letter)
print(letter.index("x"))
print(letter.count("x"))
copy = letter.copy()
print(copy)
"""
num = list(range(12))
print(num)
numm = num[::-1]
print(numm)
"""
num = 444
while num >= 0:
    print(num)
    num -= 111
"""
"""
weight = float(input())
height = float(input())
result = weight / height ** 2
if result < 18.5:
    print("Underweight")
elif result >= 18.5 and result < 25:
    print("Normal")
elif result >= 25 and result< 30:
    print("Overweight")
elif result >= 30:
    print("Obesity")
"""
"""
m = [
[1, 2, 3],
[4, 5, 6],
[8, 9, 10],
[12, 13, 14],
]
print(m[3][2])
"""
"""
things = ["text", 0, [1, 2, 8], 4.56, [1, 2, 3, 4, 5, 6, 7, 8], "6"]
things[1] = 10
print("10" in things)
print(str(things[1]) * 4)
print(things[4][3])
"""
"""
text = ["Hakuna, matata"]
if("Hakuna, matata" in text):
    print("Eurika!")
else:
    print("No")
"""