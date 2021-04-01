# [Lesson12-1. ChocolatesByNumbers]
def solution(N, M):
    if M == 1:
        return N
    rest = 1
    A = N
    B = M
    while B != 0:
        rest = A%B
        A = B
        B = rest
    
    return N//A
