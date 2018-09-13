# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    max_profit = 0
    min_day = 200000
     
    for day in A:
        min_day = min(min_day, day)
        max_profit = max(max_profit, day-min_day)
     
    return max_profit
