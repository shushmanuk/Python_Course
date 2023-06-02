# def solution(a, b):
#     list1 = sorted(a)
#     list2 = sorted(b)
#     return list1 == list2

# print(solution([1, 4, 7], [7, 1, 4]))


inputString = "mam(aaam(aam(a)))"
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
    print(solution(inputString))
 