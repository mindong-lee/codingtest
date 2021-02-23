# 선택 정렬, N번 만큼 작은 수를 찾아서 맨 앞으로 보냄
# N + (N-1) + (N-2) + ... + 2
# O(N^2)
# 학습을 위한 알고리즘, 실제론 안 쓰는 게 좋다.

def SelectionSort(array):
    for i in range(len(array)-1):
        minidx=i
        for j in range(i+1,len(array)):
            if array[minidx] > array[j]:
                minidx=j
        array[i],array[minidx]=array[minidx],array[i] #SWAP

    return array
        
arr=SelectionSort([0,1,9,7,3,5,6,2,4,8])
print(arr)


# s=list(map(int,input().split(",")))
# for i in range(len(s)-1):
#     j=s.index(min(s[i:]))
#     s[i],s[j]=s[j],s[i]

# print(s)