from collections import deque
import sys

n,m,v = map(int,input().split())
graph = [int(sys.stdin.readline()) for _ in range(m)] # 간선이 연결하는 두 정점의 번호
# DFS
visited = [False] * len(graph)
answer = []
def dfs(graph, v, visited):
    visited[v] = True # 방문 처리
    answer.append(v)
    for i in graph[v]:
        if not visited[v]:         # 
            dfs(graph, v, visited)
    
    
    

