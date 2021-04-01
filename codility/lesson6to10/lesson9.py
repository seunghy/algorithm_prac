# [Lesson9-1. MaxSliceSum]
def solution(A): #다이나믹 프로그래밍 - Kadane’s Algorithm(카데인 알고리즘)
    localmax = A[0]
    answermax = A[0]

    for i in range(1,len(A)):
        localmax = max(A[i], localmax+A[i])
        answermax = max(answermax, localmax)

    return answermax

# [Lesson9-1. MaxProfit]
def solution(A): #다이나믹 프로그래밍 활용
    if len(A) == 0:
        return 0
    maxprofit = A[1] - A[0]
    localprofit = A[1] - A[0]
    for i in range(1, len(A)-1):
        localprofit = max(A[i+1]-A[i],A[i+1]-A[i]+localprofit)
        maxprofit = max(localprofit, maxprofit)
    
    if maxprofit < 0:
        return 0
    return maxprofit
