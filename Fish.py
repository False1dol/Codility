# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    rem = 0
    stack = []
    for i in range(len(A)):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                rem += 1
        else:
            stack.append(A[i])
    rem += len(stack)
    return rem
