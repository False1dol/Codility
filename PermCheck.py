# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
   
    if not len(A):
        return 0

    dict = {}
    for item in A:

        if item in dict:
            return 0
        dict[item] = True

    if len(dict) != len(A):
        return 0

    for num in range(1, len(A) + 1):
        if num not in dict:
            return 0

    return 1
