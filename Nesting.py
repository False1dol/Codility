# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    A = []
    for val in S:
        #print(val)
        if val == '(':
            A.append('(')
        elif val == ')' and A != []:
            A.pop()
        elif val == ')' and A == []:
            return 0
    #print(A)
    if A == []:
        return 1
    else:
        return 0
