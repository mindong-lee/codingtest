# 다익스트라 최단 경로 알고리즘

INF=int(1e+9)

graph = [
    [],
    [0,INF,2,5,1,INF,INF],
    [INF,0,INF,3,2,INF,INF],
    [INF,INF,3,0,INF,INF,5],
    [INF,INF,INF,3,0,1,INF],
    [INF,INF,INF,1,INF,0,2],
    [INF,INF,INF,INF,INF,INF,0]
]

table = [INF,0,INF,INF,INF,INF,INF]
visited = [INF,0,0,0,0,0,0]
start=1
for i in range(len(table)-1):
    for j in range(1,len(table)):
        min=1e+9
        if visited[j] == 0: # 방문하지 않았으면서
            if min >= table[j]: # 최단 거리인 노드 찾기
                min = table[j]
                visited[j] = 1
                break
    for k in range(1,len(table)):
        if table[j]+graph[j][k] < table[k]: # TODO
            table[k] = table[j] + graph[j][k]
        
print(table)