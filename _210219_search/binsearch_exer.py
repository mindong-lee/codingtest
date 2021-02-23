# 문제에서 탐색 범위가 넓게 나오면, Binary Search를 고려해봐야 한다.
import time
def MyMethod(len_list,N,M):
    len_list.sort(reverse=True)
    i=0
    for i in range(1,N):
        sum=0
        for j in range(i):
            sum+=len_list[j]-len_list[i]

        if sum==M:
            print(len_list[i])
            return
        elif sum > M:
            break

    start=len_list[i]
    end=len_list[i-1]

    while start <= end:
        mid=(start+end)//2
        sum=0
        for j in range(i):
            sum+=len_list[j]-mid
        if sum==M:
            print(mid)
            return
        elif sum < M:
            start=mid+1
        else:
            end=mid-1

    print("Not Found!!")
def NormMethod(array, N, m):
    start = 0
    end = max(array)

    # 이진 탐색 수행 (반복적)
    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in array:
            # 잘랐을 때의 떡볶이 양 계산
            if x > mid:
                total += x - mid
        # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
        if total < m:
            end = mid - 1
        # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1

    # 정답 출력
    print(result)
from random import randint, random

N, M = map(int, input().split())
#len_list = list(map(int,input().split()))
len_list = []
for i in range(N):
    len_list.append(randint(1,20000000))

starttime = time.time()
NormMethod(len_list,N,M)
endtime=time.time()
print(f"모범 답안 걸린 시간: {endtime-starttime}")

starttime = time.time()
MyMethod(len_list,N,M)
endtime=time.time()
print(f"내 답안 걸린 시간: {endtime-starttime}") # 답안이 틀림..ㅅㅂ



