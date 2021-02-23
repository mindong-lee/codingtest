from collections import deque

# Breath First Search 너비 우선 탐색
def bfs(graph,i,visited):
    queue=deque([i])
    
    while queue:
        a=queue.popleft()
        visited[a]=True
        print(a, end=" ")
        for n in graph[a]:
            if not visited[n]:
                queue.append(n)
                visited[n]=True

# Depth First Search 깊이 우선 탐색
def dfs(graph,i,visited):
    if visited[i]==False:
        visited[i]=True
        print(i, end=" ")
        for n in graph[i]:
            dfs(graph,n,visited)
    

#그래프의 인접 행렬
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#방문한 노드
# visited=[False]*9
# dfs(graph, 1, visited)

visited=[False]*9
bfs(graph, 1, visited)