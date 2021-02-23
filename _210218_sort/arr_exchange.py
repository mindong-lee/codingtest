import time
from random import randint

N,K=map(int,input().split())
org_dstarr=[]
org_srcarr=[]

for _ in range(N):
    org_dstarr.append(randint(1,10000000))
    org_srcarr.append(randint(1,10000000))

# dstarr=org_dstarr.copy()
# srcarr=org_srcarr.copy()

# start=time.time()
# # k번의 교환
# for i in range(K):
#     dstarr[dstarr.index(min(dstarr))], srcarr[srcarr.index(max(srcarr))] = srcarr[srcarr.index(max(srcarr))], dstarr[dstarr.index(min(dstarr))]
# end=time.time()

# print("걸린 시간: {}".format(end-start))
# print(sum(dstarr))
# #위의 방법은 100000, 50000 입력 시 시간 초과. 
# #***정답을 도출하는 것도 중요하지만 문제에 명시된 시간 내에 해결하는 것도 중요***

dstarr2=org_dstarr.copy()
srcarr2=org_srcarr.copy()

start=time.time()
# 최대 k번의 교환
dstarr2.sort()
srcarr2.sort(reverse=True)

# 이 반복문에서 실수한 부분: 반복문을 중첩함. 잘 따져보면 중첩하지 않아도 됨. 생각하자.
for i in range(K):
    #for j in range(len(srcarr2)): => XXX
    if dstarr2[i] < srcarr2[i]:
        dstarr2[i],srcarr2[i] = srcarr2[i],dstarr2[i]
    else:
        break
end=time.time()

print("걸린 시간: {}".format(end-start))
print(sum(dstarr2))