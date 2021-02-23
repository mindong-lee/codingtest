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

arr=PythonicQuickSort([0,1,9,7,3,5,6,2,4,8,10])
print(arr)