# [Lesson3-TapeEquilibrium]
def solution(A):
    if len(A) == 1:
        return abs(A[0])

    standard = None
    right = sum(A)
    left = 0

    for x in range(len(A)-1):
        right -= A[x]
        left += A[x]
        value = left - right   
        if standard == None:
            standard = abs(value)
        elif standard > abs(value):
            standard = abs(value)

    return standard

# [Lesson3-1. FrogJmp]
import math
def solution(X, Y, D):
    diff = Y-X
    if diff == 0:
        return 0
    else:
        value = math.ceil(diff / D)
    
    return value

