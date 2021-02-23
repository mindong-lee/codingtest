# 내 풀이
def solution(warehouse):
    if len(warehouse)==1:
        return warehouse[0]

    elif len(warehouse)==2:
        return warehouse[0] if (warehouse[0]>warehouse[1]) else warehouse[1]

    elif len(warehouse)==3:
        if (warehouse[0]+warehouse[2]) > warehouse[1]:
            return warehouse[0]+warehouse[2]
        else:
            return warehouse[1]
    else:
        a=warehouse[0]+solution(warehouse[2:])
        b=warehouse[1]+solution(warehouse[3:])
        if a>b:
            return a
        else:
            return b

#모범 답안        
N=int(input())
warehouse = list(map(int, input().split()))

table=[0]*100

table[0]=warehouse[0]
table[1]=max(warehouse[0],warehouse[1])
#table[1]=warehouse[1] if warehouse[1]>warehouse[0] else warehouse[0]

for i in range(2,N):
    table[i]=max(table[i-1],table[i-2]+warehouse[i])

print(table[N-1])
