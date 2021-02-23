#일정 범위의 데이터 개수 구하기
from bisect import bisect_left, bisect_right
def count_by_range(array,min,max):
    right_index = bisect_right(array,max)
    left_index = bisect_left(array,min)
    return right_index-left_index

#Iterative Binary Search
def iBinarySearch(array,target):
    arrlen=len(array)
    start=0
    end=arrlen-1

    #등호 조심.
    while start <= end:
        mid=(start+end)//2
        if arr[mid]==target:
            print(f"Got it!! It's in {mid}")
            return mid
        elif arr[mid]>target:
            end=mid-1
            continue
        else:
            start=mid+1
            continue

    print("There isn't Target in array!")
    return
#Recursive Binary Search
def rBinarySearch(array,target):
    arrlen=len(array)
    if arrlen <= 0:
        print("There isn't Target in array!")
        return
    pivot_idx = arrlen//2

    if(array[pivot_idx]==target):
        print(f"Got it!! It's in {pivot_idx}")
        return pivot_idx
    elif (array[pivot_idx]>target):
        rBinarySearch(array[:pivot_idx],target)
    else:
        rBinarySearch(array[pivot_idx+1:],target)

arr=list(range(100))
rBinarySearch(arr,25)
iBinarySearch(arr,25)
rBinarySearch(arr,101)
iBinarySearch(arr,101)

print(count_by_range(arr,1,100))