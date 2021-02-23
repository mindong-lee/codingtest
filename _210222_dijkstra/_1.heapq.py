# Priority Queue
# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

import heapq

# min heap
def minheapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def maxheapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result=minheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

result=maxheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)