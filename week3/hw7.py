#homework N7 Find out the inputed number is even number or odd number
#version1
num = -29
print("even" * (num % 2 == 0),"odd" * (num % 2 != 0))

#version2
num = 48
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")
    
#version3
y = ("Even", "Odd")
x = int(input("Enter a number:" ))
print(y[x % 2])