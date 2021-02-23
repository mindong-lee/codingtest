# 퀵 정렬
# 가장 많이 사용되는 정렬 알고리즘 중 하나
# 병합 정렬(Merge Sort)과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘

def PythonicQuickSort(array): #기가 막히는구만..
    if len(array)<=1:
        return array
    
    pivot=array[0]

    left= [x for x in array[1:] if x<=pivot]
    right= [x for x in array[1:] if x>pivot]

    return PythonicQuickSort(left) + [pivot] + PythonicQuickSort(right)

def QuickSort(array):
    if len(array) <= 1:
        return array
        
    pivot=array[0]
    start = 0
    end = len(array)-1

    while start < end:
        for i in range(start+1, len(array)):
            start=i
            if array[i] > pivot:
                break

        for j in range(end, -1, -1):
            end=j
            if array[j] <= pivot:
                break

        if start < end:
            array[start], array[end] = array[end], array[start]
        else:
            array[0], array[end] = array[end], array[0]
    
    ans = QuickSort(array[:end])+[pivot]+QuickSort(array[end+1:])
    return ans

arr=QuickSort([0,1,9,7,3,5,6,2,4,8,10])
print(arr)
arr=PythonicQuickSort([0,1,9,7,3,5,6,2,4,8,10])
print(arr)