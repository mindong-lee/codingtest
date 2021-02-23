N=int(input())
power = list(map(int,input().split()))

longest=[power[0]]
tmp=[]
num=1

for i in power[1:]:
    for j in longest[::-1]:
        if power[i] > power[i-1]:
            longest.pop()
            longest.pop(power[i])
