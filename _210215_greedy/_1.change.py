# 1. 거스름 돈 문제
# 금액이 큰 동전부터 세면 최적의 해가 나온다고 보장할 수 있을까?
# 만약 500, 400, 100원의 동전들로 거슬러준다고 하면?

N=int(input())

l=[]
for i in [500,100,50,10]:
    count, N = divmod(N, i)
    l.append(count)

print(l,sum(l))
