from collections import deque
N,M=map(int,input().split())
mat=[]
queue = deque()
answer = 0
for i in range(N+2):
    mat.append([1]*(M+2))

for i in range(N):
    str=input()
    for j in range(M):
        mat[i+1][j+1]=int(str[j])

for i in range(1,N+1):
    for j in range(1,M+1):
        if mat[i][j]==0:
            queue.append((i,j))
            mat[i][j]=1
            while queue:
                row,col=queue.popleft()
                if mat[row+1][col]==0:
                    queue.append((row+1,col))
                    mat[row+1][col]=1
                if mat[row][col+1]==0:
                    queue.append((row,col+1))
                    mat[row][col+1]=1
                if mat[row-1][col]==0:
                    queue.append((row-1,col))
                    mat[row-1][col]=1
                if mat[row][col-1]==0:
                    queue.append((row,col-1))
                    mat[row][col-1]=1
            answer += 1
print(answer)