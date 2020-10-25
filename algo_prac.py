# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:32:53 2020

@author: seunghyeon
"""

import numpy as np

##Bubble 정렬
#메모: 결론적으로 반복하면서 주어진 리스트 내에서 가장 작은 숫자를 차례대로 앞으로 옮기는 과정
def bubble(data):

    data_len = len(data)
    
    for j in range(data_len-1): #저울로 순서바꾸는 것을 한 단계라고 할 때 단계를 반복하는 수
        for i in range(data_len-1): #저울로 순서 바꿈
            if data[data_len-i-2] > data[data_len-i-1]:
                data[data_len-i-2], data[data_len-i-1] = data[data_len-i-1], data[data_len-i-2]

            
    return data

value = [5,6,3,2,9,1]

bubble(value)
##END

##선택 정렬
#메모: 해당 리스트 내에서 최소값을 찾아내어 가장 앞으로 옮김 
#(최소값을 앞으로 옮길때 버블정렬과 차이:버블정렬은 2개씩 비교하며 자리바꾸지만, 
#선택정렬은 min값을 찾기 위해 1:N으로 비교 후 min값찾으면 그때 자리바꿈)
def selection(data):
    data_len = len(data)
    
    for i in range(data_len-1):
        min_index = i #처음에 일단 min_index를 0,1,2...로 설정해놓음
        
        for j in range(i+1, data_len): #min_index update
            if data[min_index]>data[j]:
                min_index = j
        
        if min_index != i: #초기설정한 min_index에서보다 min값이 존재한다면 min값을 해당 min_index위치로 옮김
            data[min_index], data[i] = data[i], data[min_index]
            
    return data

value = [5,6,3,2,9,1]

selection(value)
##END

##삽입 정렬 -복습필요
def insertion(data):
    data_len = len(data)
    
    for i in range(1, data_len):
        unsorted = data[i]
        j = i
        while j>0 and data[j-1] > unsorted:
            data[j] = data[j-1]
            j -= 1
            
        data[j]=unsorted    
                
    return data

#메모: 0번째 데이터 고정이라 가정 후 i번째 데이터(i>=1)부터 n<i인 데이터를 비교해가면서 반복문 탐
def insert(data): 
    data_len = len(data)
    
    for i in range(1, data_len):
        while i>0 and data[i] < data[i-1]:
            data[i], data[i-1] = data[i-1], data[i]
            i -= 1
            
    return data

value = [5,6,3,2,9,1]
insertion(value)
insert(value)

##END

##heap정렬
##END

##병합정렬
#메모: 중앙위치값을 기준으로 왼쪽, 오른쪽 array 내에서 정렬 후 합침
def mergeSort(arr):
    if len(arr)<=1:
        print("데이터는 1개")
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left_sub = mergeSort(left)
    right_sub = mergeSort(right)
    
    return mergeArr(left_sub, right_sub)


def mergeArr(left, right):
    i=0
    j=0 
    sorted = []
    while len(left)>i and len(right)>j:
        if left[i]>right[j]:
            sorted.append(right.pop(j))
        else:
            sorted.append(left.pop(i))         
    
    if len(left)>0:
        sorted.extend(left)
    
    if len(right)>0:
        sorted.extend(right)
        
    return sorted
                
mergeArr([1,3,6],[2,4,5])

mergeSort([1,3,6,2,7,4,2,5])

##END

##퀵 정렬
#메모: 중앙위치값을 기준으로 작은값, 큰값으로 나누어 위치시킨 후 해당 작은값arr, 큰값arr 내에서 반복문 탐
def quickSort(arr):
    if len(arr)<=1:
        return arr
    
    key = arr[len(arr)//2]
    small, big, equal = [],[],[]
    for i in arr:
        if i<key:
            small.append(i)
        elif i>key:
            big.append(i)
        else:
            equal.append(i)
    
    return quickSort(small)+equal+quickSort(big)

quickSort([1,3,6,2,7,4,2,5])         
##END   
    
##선형 탐색
def linearSearch(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return None

linearSearch([1,4,62,6,3],6)
##END

##이진 탐색
def binarySearch(arr, n):
    arr.sort()
    key = arr[len(arr)//2]
    minn = 0
    maxx = len(arr) - 1
    while minn <= maxx:
        mid_index = (minn + maxx) // 2
        if arr[mid_index] == n:
            return mid_index
            break        
        elif arr[mid_index] < n:
            minn = mid_index
        elif arr[mid_index] > n:
            maxx = mid_index
            
binarySearch([1,4,6,2,65,2,7,11,3,53], 11)
##END

##너비 우선 탐색 (BFS)

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    visited = []
    need_visit = []
    
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
        
    return visited

bfs(graph, 'A')
##END

##깊이 우선 탐색 (DFS)
def dfs(graph, start_node):
    visited = []
    need_visit = []
    
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
        
    return visited


dfs(graph, 'A')
##END
