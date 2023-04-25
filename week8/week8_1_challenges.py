"""1. Using .sort() method, create a lambda function that sorts the list 
in descending order. Refrain from using the reverse parameter.

(Hint: lambda will be passed to sort method's key parameter as argument)

Please check out Hint 0 below to be informed about a glitch regarding this 
exercise.

lst=[100, 10, 10000, 1, 9, 999, 99]"""



"""2. Using sorted() function, reverse parameter and lambda sort the tuples 
in the list based on the last character of the second items in reverse order.

lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), 
(626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.

Decorators, function inside function"""

def tuple_sort(final_list):
 
    lst = len(final_list)
    for i in range(0, lst):
 
        for j in range(0, lst-i-1):
            if (final_list[j][1] > final_list[j + 1][1]):
                temp = final_list[j]
                final_list[j] = final_list[j + 1]
                final_list[j + 1] = temp
    return final_list
 
 
final_list = [(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), 
(626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
 
print(tuple_sort(final_list))

"""3. Write function which take a function as an input and run it and print 
how count how many times I have run the input provide functions."""