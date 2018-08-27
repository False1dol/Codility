# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    missing = 1
    for elem in sorted(A):
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing
