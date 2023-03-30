#homework N1 Finding the sum of digits of a two-digit number
#version1
num = 68
n1 = 6
n2 = 8
print(n1 + n2)

#version2
num = int(input("Enter a two-digit number, please" ))
print ((num // 10) + (num % 10))
#but if someone enters more then two digits, it should not be correct)