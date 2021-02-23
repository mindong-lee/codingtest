#감이 아니라 논리로 풀어야 해..
#답에 확신을 가질 수 있게
N=int(input())

table=[0]*(N+1)

for i in range(2,N+1):
    table[i]=table[i-1]+1

    #i가 2로 나누어 떨어지면,
    if i%2==0:
        table[i]=min(table[i],table[i//2]+1)

    #i가 3으로 나누어 떨어지면,
    if i%3==0:
        table[i]=min(table[i],table[i//3]+1)

    #i가 5로 나누어 떨어지면,
    if i%5==0:
        table[i]=min(table[i],table[i//5]+1)

print(table[N])