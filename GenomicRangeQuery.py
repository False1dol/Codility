# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    sumC = [0]
    sumG = [0]
    sumT = [0]
    sumA = [0]
    array = []
    for i,key in enumerate(S):
        if key == 'C':
            sumC.append(sumC[i]+1)
            sumG.append(sumG[i])
            sumT.append(sumT[i])
            sumA.append(sumA[i])
        elif key == 'G':
            sumC.append(sumC[i])
            sumG.append(sumG[i]+1)
            sumT.append(sumT[i])
            sumA.append(sumA[i])
        elif key == 'T':
            sumC.append(sumC[i])
            sumG.append(sumG[i])
            sumT.append(sumT[i]+1)
            sumA.append(sumA[i])
        elif key == 'A':
            sumC.append(sumC[i])
            sumG.append(sumG[i])
            sumT.append(sumT[i])
            sumA.append(sumA[i]+1)
    ##print(sumA)
    #print(sumC)
    #print(sumG)
    #print(sumT)
    for i in range(0, len(P)):
        if sumA[P[i]+1] != sumA[Q[i]+1] or sumA[P[i]] != sumA[P[i]+1]:
            array.append(1)
        elif sumC[P[i]+1] != sumC[Q[i]+1] or sumC[P[i]] != sumC[P[i]+1]:
            array.append(2)
        elif sumG[P[i]+1] != sumG[Q[i]+1] or sumG[P[i]] != sumG[P[i]+1]:
            array.append(3)
        else:
            array.append(4)
    #print(array)
    return array
