# 삽입 정렬
# 데이터가 이미 정렬되어 있는 상태라면 매우 빠르게 동작
# but 반대로 정렬된 상태라면 매우 오래 걸림
# O(N^2)

from random import randint

def InsertionSort(array):
    for i in range(1,len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array[i],array[j]=array[j],array[i]
    return array
arr=InsertionSort([randint(1,100) for _ in range(100)])
print(arr)

def InsertionSort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j-1],array[j]=array[j],array[j-1]
            else:
                break # 이미 정렬된 데이터에서 시간 단축
    return array
arr=InsertionSort([11,0,1,9,7,3,5,6,2,4,8])
print(arr)