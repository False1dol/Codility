# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#Solution 1:
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

#Solution 2

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    seen = set()
    for i in A:
        if i < 1 or i > len(A) or i in seen:
            return 0
        seen.add(i)
    return 1
