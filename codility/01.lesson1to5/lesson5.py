# [Lesson5-1. PassingCars]
def solution(A): #-----------timeout
    answer = 0
    zero_idx = [i for i in range(len(A)) if A[i]==0]
    one_idx = [i for i in range(len(A)) if A[i]==1]

    for i in zero_idx:
        answer += len([j for j in one_idx if i<j])
    
    return answer
##########

def solution(A):
    answer = 0
    zero_sum = 0
    for x in A:
        if x == 0:
            zero_sum += 1
        elif x == 1:
            answer += zero_sum
    
    if answer > 1000000000:
        return -1
    else:
        return answer


# [Lesson5-1. CountDiv]
# -- 처음 코드 -> time out #
# def solution(A, B, K):
#     count = 0
#     mid = (B-A+1)/2
#     for x in range(A, B+1):
#         if check_true(x, K):
#             count += 1
#     return count

# def check_true(x, K):
#     if x%K == 0:
#         return True
#     else:
#         return False

def solution(A, B, K):
    A_ = A//K
    B_ = B//K
    answer = B_ - A_

    if A%K == 0:
        answer += 1
    return answer

# [Lesson5-1. MinAvgTwoSlice]
def solution(A):
    min_avg = (A[0]+A[1]) / 2
    idx = 0

    for i in range(2,len(A)):
        if (A[i-2]+A[i-1]+A[i])/3 < min_avg:
            min_avg = (A[i-2]+A[i-1]+A[i])/3
            idx = i-2
        
        if (A[i-1]+A[i])/2 < min_avg:
            min_avg = (A[i-1]+A[i])/2
            idx = i-1
        
    return idx

