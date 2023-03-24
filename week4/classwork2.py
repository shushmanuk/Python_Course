# 1.
"""
name = ("ShushManuk") 
print(len(name)) #10
print(name[5]) #M sixth character
print(name[0]) #S first character
print(name[-2]) #u second from the end
print(name[0:5]) #Shush starts from the first, takes four characters
print(name[:5]) #Shush starts from the first, takes four characters
print(name[0:]) #ShushManuk starts from the first to the end of the line
print(name[:]) #ShushManuk a copy of the original string
"""
# print(name[3:2]) #sh starts from the fourth character, takes two characters

text = "Shushanik is the author \nof the book \"Python programmer\"" #\' or \" inputs quotes in text, \\ inputs backslash(\) \n for new line
# print(text)

"""
my_name = "Shushanik"
my_surname = "Manukyan"
full_name = my_name + " " + my_surname
full_name = f"{my_name} {my_surname}"
full_name = f"{len(my_name)} {my_surname}"
full_name = f"{my_name} {3 + 6}"
print(full_name)
"""
n = "shdcjskhqhfougfodhsalknaljcbdvudgoujsxbc"
# print(n.split())


m = "Booba"
# print(len(m))

"""
version2 ???
text = input("Please, enter a text! ")
num = int(input("How many times to repeat? "))
key = type(text) == str
output = text * num
print(output * key + ("Not a string!" * (output != key)))
"""
#version2
# text, repeat = input("Please, type a text! "), int(input("How many times to repeat? "))
# print("Not a string!" * isinstance(text, int) + str(text * repeat) * isinstance(text, str))
"""
work = "A new black shoe met an old pair of black boots and asked for black brash for shoes."
print(work.upper())
print(work.count("black"))
print(work.find("k"))
print(work.index("c"))

print("One", "two", "three", sep = ", ")
"""
6. 
#version2
ineq = ("3 > 2 > 0")
change = ineq.split(" ")
#համեմատում ենք զույգ տեղերում եղած տարրերը, ստուգում համեմատության տարրերը
10.
input_word = input("Type a word: ")
isogram = len(set(input_word)) >= len(input_word)
# print(isogram)
#uppers and lowers are not the same

new_word = input("\nPlease, write a word! ")
word = new_word.lower()
a = word.count("a") 
e = word.count("e") 
i = word.count("i") 
o = word.count("o") 
u = word.count("u") 
print(a + e + i + o + u)
