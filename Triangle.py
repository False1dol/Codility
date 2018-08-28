# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    def is_triangle(P,Q,R):
        return (P + Q > R) and (Q + R > P) and (R + P > Q)
    A.sort()
    for i in range(0,len(A)-2):
        if is_triangle(A[i], A[i+1], A[i+2]):
            return 1
    return 0
        
