# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A) + 1
    total_sum = (n * (n + 1))//2
    return total_sum - sum(A)
