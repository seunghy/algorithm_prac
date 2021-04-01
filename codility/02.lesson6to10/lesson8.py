# [Lesson8-1. Dominator]
def solution(A):
    if len(A) == 0:
        return -1
        
    dic = {}

    for item in A:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    
    dominator_value = max(dic.values())

    #if dominator_value >= math.ceil(len(A)/2): #잘못 설정
    if dominator_value > len(A)//2:
        temp_dic = dict(map(reversed, dic.items()))
        dominator = temp_dic[dominator_value]
        for idx, x in enumerate(A):
            if x == dominator:
                return idx
    else:
        return -1


# [Lesson8-1. EquiLeader] 
def solution(A):  #--------------Timeout
    count = 0
    for x in range(len(A)-1):
        left = A[:x+1]
        right = A[x+1:]
        left_leader = find_leader(left)
        right_leader =find_leader(right)
        if left_leader != 'None' and right_leader != 'None':
            if left_leader == right_leader:
                count += 1
        else:
            pass
    return count 

def find_leader(lst):
    dic = {}
    for x in lst:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    
    lead_value = max(dic.values())
    temp_dic = dict(map(reversed, dic.items()))
    if dic[temp_dic[lead_value]] > (len(lst)//2):
        return temp_dic[lead_value]
    else:
        return 'None'

#--------------
# 수정 완성본
def solution(A):
    left_dict = {}
    right_dict = {}
    count = 0
    left_len = 0
    left_leader = A[0]
    left_leader_count = 0
    if len(A) == 1:
        return 0

    for x in A:
        if x in right_dict:
            right_dict[x] += 1
        else:
            right_dict[x] = 1

    right_len = len(A)
    
    for i in range(0, len(A)):
        # print("start//","L:",left_dict,"R:",right_dict)

        if A[i] in left_dict:
            left_dict[A[i]] += 1
        else:
            left_dict[A[i]] = 1
        left_len += 1
        
        right_dict[A[i]] -= 1
        right_len -= 1
        # print("mid//","L:",left_dict,"R:",right_dict)
        if left_dict[A[i]] > left_leader_count:
            left_leader = A[i]
            left_leader_count = left_dict[A[i]]

        
        # print("check",right_dict[left_leader] ,right_len,left_leader)
        if left_dict[left_leader] > left_len/2 and right_dict[left_leader] > max(0,right_len / 2):
            count += 1
        
        # print("after//","L:",left_dict,"R:",right_dict)  
        # print("count:",count)
        # print("-------------------------------")
    return count
