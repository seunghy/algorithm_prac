# [Lesson6-1. Triangle]
def solution(A):
    if len(A) == 0:
        return 0
    A = sorted(A)

    for i in range(len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0        

# [Lesson6-1. MaxProductOfThree]
def solution(A):
    A = sorted(A)

    negative = [x for x in A if x<0]
    positive = [x for x in A if x>0]
    v = 1
    w = 1

    if len(positive) == 0 :
        if 0 in A:
            return 0
        else:
            for x in negative[-3:]:
                v *= x
            return v
    
    max_value1 = max_value2 = A[0] * A[1] * A[2]
    if len(negative)>=2 and len(positive)>=1:
        for x in negative[:2]:
             v *= x
        max_value1 = v * max(positive)
    if len(positive) >= 3:
        for y in positive[-3:]:
            w *= y
        max_value2 = w

    if max_value1 > max_value2:
        return max_value1
    else:
        return max_value2
