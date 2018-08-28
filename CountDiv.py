# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    x = B // K - (A - 1) // K
    #print(int(x))
    return x 
