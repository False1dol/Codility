# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    step = {}
    for second in range(0, len(A)):
        step[A[second]] = True
        if len(step) == X:
            return second
    return -1
