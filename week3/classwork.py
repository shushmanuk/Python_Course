thisyear = 2023
yearofbirth = 1995
age = thisyear - yearofbirth
daysofyears = 365 * age
liveddays = (daysofyears + (age // 4))
# print(liveddays)

thisyear = 2023
yearofbirth = 1950
age = thisyear - yearofbirth
# print(age >= 20 and age <= 30)

#version1
thisyear = 2023
yearofbirth = 1932
age = thisyear - yearofbirth
print("Enjoy!" * (age >= 20 and age < 30))
print("We'll meet later" * (age < 20 or age >= 50))
print("It's too late!" * (age >= 30 and age < 50))

#version2
thisyear = 2023
yearofbirth = 2002
age = thisyear - yearofbirth
# print(("Enjoy!" * (age >= 20 and age < 30)) + ("We'll meet later" * (age < 20 or age >= 50)) + ("It's too late!" * (age >= 30 and age < 50)))