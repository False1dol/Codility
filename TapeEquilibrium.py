def solution(A):
    # write your code in Python 3.6
    left, right = sum(A[:1]), sum(A[1:])
    min_difference = abs(left - right)
    for i in range(1, len(A)-1):
        left += A[i]
        right -= A[i]
        min_difference = min(min_difference, abs(left - right))
        
    return min_difference
