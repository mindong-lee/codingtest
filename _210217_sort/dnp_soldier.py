# 2/16의 연장

N=int(input())
soldiers=list(map(int,input().split()))
soldiers.reverse()
max_length=1
tmp=1
max_array=[soldiers[0]]

for soldier in soldiers[1:]:
    if max_array[-1] > soldier:
        max_array.append(soldier)
        tmp += 1
        if tmp > max_length:
            max_length=tmp
    else:
        while(len(max_array)>0 and max_array[-1]<soldier):
            max_array.pop()
        max_array.append(soldier)
        tmp=len(max_array)
        

print(max_length)
        