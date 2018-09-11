# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

CLOSING = {
    ']' : '[',
    ')' : '(',
    '}' : '{'
    }

def solution(S):
    # write your code in Python 3.6
    stack = []
    for val in S:
        if val in CLOSING:
            if not stack:
                #found closing bracket but stack's empty!
                return 0
            last = stack.pop()
            if last != CLOSING[val]:
                #found opening bracket in the wrong place!
                return 0
        else:
            stack.append(val)
    if stack:
        #checking if there are still open brackets in the stack
        return 0
    else:
        return 1
