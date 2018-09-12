from collections import Counter
def solution(A):
    # write your code in Python 3.6
    c = Counter(A)
    #print(c.most_common(1)[0][0])
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        return 0
    if c.most_common(1)[0][1] > len(A)/2:
        return A.index(c.most_common(1)[0][0])
    else:
        return -1
