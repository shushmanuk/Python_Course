# def pair_one(sequence, k):
#     if 0 < k < len(sequence) - 1:
#         if sequence[k-1] >= sequence[k+1]:
#             return k-1
#     for i in range(k+1, len(sequence)-1):
#         if sequence[i] >= sequence[i+1]:
#             return i
#     return -1

# def solution(sequence):
#     j = pair_one(sequence, -1)
#     if j == -1:
#         return True  
#     if pair_one(sequence, j) == -1:
#         return True  
#     if pair_one(sequence, j+1) == -1:
#         return True  
#     return False  
"""
numbers = [18, 65, 789, 28, 83, 48, 57, 86, 79]

# the lambda function returns True for even numbers 
odd_numbers_iterator = filter(lambda x: (x%2 != 0), numbers)

# converting to list
odd_numbers = list(odd_numbers_iterator)

print(odd_numbers)"""

"""
def check_even(number):
    if number % 2 == 0:
        return True  

    return False


numbers = [18, 65, 789, 28, 83, 48, 57, 86, 79]

# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)"""


"""Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not."""

# n = 123060
# def solution(n):
#     num = list(map(int, str(n)))
#     first_sum, second_sum = 0, 0
#     if len(num) % 2 == 0:
#         for item in range(len(num) // 2):        
#             first_sum += num[item]
#             second_sum += num[item + len(num) // 2]
#             return first_sum == second_sum
#     return len(num) % 2 == 0  
    

# print(solution(n))

"""

inputString = "ba(bar)um"
def solution(inputString):
    st = []
 
    for i in range(len(inputString)):
 
        
        if (inputString[i] == '('):
            st.append(i)
 
        elif (inputString[i] == ')'):
            temp = inputString[st[-1]:i + 1]
            inputString = inputString[:st[-1]] + temp[::-1] + \
                   inputString[i + 1:]
            del st[-1]
 
    res = ""
    for i in range(len(inputString)):
        if (inputString[i] != ')' and inputString[i] != '('):
            res += (inputString[i])
    return res
 
if __name__ == '__main__':
    
    st = [i for i in inputString]
 
    print(solution(inputString))"""


picture = ["abc",
           "ded"]
def solution(picture):
    height = len(picture)
    length = len(picture[0]) 
    newpic = ['*' * (length + 2)] 
    
    for index,text in enumerate(picture):
        newpic[index + 1] = ('*' + text + '*') * height
        return newpic 
        
print(solution(picture))
 
    