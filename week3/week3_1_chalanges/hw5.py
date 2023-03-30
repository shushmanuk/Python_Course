#homework N5 Print the sum of seconds of inputed hours' and minutes'
#version N1
secondsofanhour = 3600
secondsofaminute = 60
hours = 5
minutes = 23
x = hours * secondsofanhour + minutes * secondsofaminute
print(x)

#version N2
print("How many seconds will be ... ?")
x = ((int(input("Hours:" )) * 3600 ) + (int(input("minutes:")) * 60))
print(x)
