# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    counter = [0] * N
    max = 0
    min = 0;
    for value in A:
        if value <= N:
            if counter[value-1] < min:
                counter[value-1] = min
            counter[value-1] += 1
            if max < counter[value-1]:
                max = counter[value-1]
        else:
            min = max
        ##print(counter)
        ##print(min)
    for key, val in enumerate(counter):
        if val < min:
            counter[key] = min
    return counter
