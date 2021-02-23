from bisect import bisect_left,bisect_right
import sys

def count_target(array,target):
    left_index=bisect_left(array, target)
    right_index=bisect_right(array, target)
    
    result = right_index-left_index
    if result>0:
        return result
    else:
        return -1

N, target = map(int, input().split())
array = list(map(int, sys.stdin.readline().split()))
print(count_target(array,target))
