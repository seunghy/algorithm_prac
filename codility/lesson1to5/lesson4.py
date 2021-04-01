# [Lesson4-1. PermCheck]
def solution(A):
    if len(A) == 1 and A[0] != 1:
        return 0

    A = sorted(A)
    if A[0] != 1:
        return 0
        
    for x in range(len(A)-1):
        if A[x+1]-A[x] != 1:
            return 0
    
    return 1


# [Lesson4-1. MissingInteger]
def solution(A):
    temp = []
    for x in A:
        if x>0:
            temp.append(x)
    if len(temp) == 0:
        return 1
    else:
        temp = list(set(temp))
    
    temp = sorted(temp)
    if min(temp) == 1 and len(temp) == max(temp):
        return max(temp) + 1
    elif min(temp) > 1 and len(temp) != max(temp):
        return 1
    else:
        # return 1
        for i in range(len(temp)-1):
            if temp[i+1] - temp[i] != 1:
                return temp[i]+1
        
        return temp[-1]+1

