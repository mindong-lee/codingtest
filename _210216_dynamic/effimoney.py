N, M= map(int,input().split())
money=[]
table=[-1]*(10001)

for i in range(N):
    n=int(input())
    table[n]=1
    money.append(n)

for i in range(min(money)*2,M+1):
    for j in money:
        if table[i-j]!=-1:
            if table[i]==-1:
                table[i]=table[i-j]+1
            else:
                table[i]=min(table[i],table[i-j]+1)
print(table[:M+1])

