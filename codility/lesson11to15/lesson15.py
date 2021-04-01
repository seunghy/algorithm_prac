# [Lesson15-1. AbsDistinct]
def solution(A):
    lst = [x*(-1) if x<0 else x for x in A]
    lst = set(lst)
    return len(lst)

    # lst = []
    # for front in A:
    #     if front not in lst:
    #         if front < 0:
    #             lst.append(front*(-1))
    #         else:
    #             lst.append(front)
    #     else:
    #         pass
    # return len(lst)


