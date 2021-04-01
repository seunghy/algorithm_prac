# [Lesson7-1. Nesting]
def solution(S):
    stack = []
    for x in S:
        if x == "(":
            stack.append(x)
        elif len(stack) > 0:
            stack.pop()
        else:
            return 0

    if len(stack) > 0:
        return 0
        
    return 1


# [Lesson7-1. Brackets]
def solution(S):
    lst = []
    for x in S:
        if x in ["[","{","("]:  #open
            lst.append(x)
        else:
            if len(lst)== 0: #if opened
                return 0

            pop_value = lst.pop()
            if x == "]": #---------- check if properly closed
                if pop_value != "[":
                    return 0
            elif x == "}":
                if pop_value != "{":
                    return 0
            elif x == ")":
                if pop_value != "(":
                    return 0 #----------
    if len(lst) == 0: # if perfectly opened and closed->return 1
        return 1
    
    return 0


# [Lesson7-1. Fish]
def solution(A, B):
    fish = []
    count = 0
    for idx in range(len(B)):
        if B[idx] == 0:
            while fish:
                if fish[-1] > A[idx]:
                    break
                else:
                    fish.pop() #기존에 있던 fish 죽음
            else:
                count += 1 # 마주친 fish 없이 그냥 살아있음
        else:
            fish.append(A[idx]) # 올라온 fish라서 후보로 올림
    
    return count+len(fish)


