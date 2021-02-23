# 병합 정렬
# 나누는 데 logN, 합치는 데 N해서 O(NlogN)

from random import randint
import time


def PythonicQuickSort(array): #기가 막히는구만..
    if len(array)<=1:
        return array
    
    pivot=array[0]

    left= [x for x in array[1:] if x<=pivot]
    right= [x for x in array[1:] if x>pivot]

    return PythonicQuickSort(left) + [pivot] + PythonicQuickSort(right)

def CountingSort(array):
    arrlen = max(array)+1 # 0과 최대값 사이 정수 개수
    CountArr = [0]*(arrlen)
    result=[]
    for i in array:
        CountArr[i] += 1
    for idx in range(arrlen):
        for j in range(CountArr[idx]):
            result.append(idx)
    return result

def merge_sort(array):
    arrlen=len(array)
    if arrlen <= 1:
        return array
    left = merge_sort(array[:arrlen//2])
    right = merge_sort(array[arrlen//2:])
    
    result=[]

    while len(left)>=1 and len(right)>=1:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left)==0:
        while len(right)>0:
            result.append(right.pop(0))
    else:
        while len(left)>0:
            result.append(left.pop(0))

    return result
    
array = []
for _ in range(10000):
    array.append(randint(1,100))
start=time.time()
result=merge_sort(array)
end=time.time()

print("구현한 merge sort 정렬에 걸린 시간: {}".format(end-start))

array = []
for _ in range(10000):
    array.append(randint(1,100))
start=time.time()
result=sorted(array)
end=time.time()
print("sorted 정렬에 걸린 시간: {}".format(end-start)) # 겁나 빠르다. c로 구현, Tim Sort

array = []
for _ in range(10000):
    array.append(randint(1,100))
start=time.time()
result=CountingSort(array)
end=time.time()
print("CountingSort 정렬에 걸린 시간: {}".format(end-start))

array = []
for _ in range(10000):
    array.append(randint(1,100))
start=time.time()
result=PythonicQuickSort(array)
end=time.time()
print("PythonicQuickSort 정렬에 걸린 시간: {}".format(end-start))
