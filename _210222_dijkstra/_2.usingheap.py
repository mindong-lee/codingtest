import heapq

INF=int(1e+9)

graph = [
    [],
    [INF,0,2,5,1,INF,INF],
    [INF,INF,0,3,2,INF,INF],
    [INF,INF,3,0,INF,INF,5],
    [INF,INF,INF,3,0,1,INF],
    [INF,INF,INF,1,INF,0,2],
    [INF,INF,INF,INF,INF,INF,0]
]

table = [INF,0,INF,INF,INF,INF,INF]
visited = [INF,0,0,0,0,0,0]
start=1
h=[]

for i in range(len(table)-1):
    for j in range(1,len(table)):
        if graph[start][j] != INF:
            heapq.heappush(h,j)
print(table)