# [Lesson10-CountFactors]
import math
def solution(N):
    if N == 1:
        return 1

    answer = 0
    if math.sqrt(N) == int(math.sqrt(N)):
        half = int(math.sqrt(N))
    else:
        half = int(math.sqrt(N))+1
    half = int(math.sqrt(N))
    for x in range(1,half+1):
        if N%x == 0:
            answer += 1
    return 2*answer



# [Lesson10-1. CountFactors]
import math
def solution(N):
    mid = math.sqrt(N)
    count = 0
    if mid == int(mid):
        for i in range(1, int(mid)):
            if N%i == 0:
                count += 1
        count = count * 2 + 1
    else:
        for i in range(1, int(mid)+1):
            if N%i == 0:
                count += 1
        count *= 2
    return count

# [Lesson10-1. MinPerimeterRectangle]
import math
def solution(N):
    lst = []
    mid = math.sqrt(N)
    if mid == int(mid):
        for x in range(1, int(mid)):
            if N%x == 0:
                lst.append(x)
        lst.append(mid)
    else:
        for x in range(1, int(mid)+1):
            if N%x == 0:
                lst.append(x)

    min_value = N + 1
    for item in lst:
        if min_value > int(item + N/item):
            min_value = int(item + N/item)
    return min_value * 2
