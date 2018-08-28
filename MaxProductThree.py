# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    if A[0] < 0 and A[1] < 0 and A[-1] > 0:
        return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
    else:
        return A[-3] * A[-2] * A[-1]
