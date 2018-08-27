# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    east = 0
    pair = 0
    for value in A:
        if value == 0:
            east += 1
        else:
            pair += east
        if pair > 1000000000:
            return -1
    return pair
            
