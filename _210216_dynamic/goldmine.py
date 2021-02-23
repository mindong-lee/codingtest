T=int(input())
case=[]

for _ in range(T):
    N,M=map(int,input().split())
    gold=list(map(int,input().split()))
    goldmine=[]
    for j in range(M):
        goldmine.append([])
    
    for i in range(len(gold)):
        goldmine[i%4].append(gold[i])

max_course = goldmine.copy()

for i in range(1,M):
    for j in range(N):
        if j == 0:
            max_course[i][j]= max(max_course[i-1][0],max_course[i-1][1])+max_course[i][j]
        elif j == N-1:
            max_course[i][j]= max(max_course[i-1][N-2],max_course[i-1][N-1])+max_course[i][j]
        else: 
            max_course[i][j]= max(max(max_course[i-1][j-1],max_course[i-1][j]),max_course[i-1][j+1])+max_course[i][j]

print(max_course)
