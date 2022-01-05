from collections import deque

n = int(input())
k = int(input())

graph = {i : [] for i in range(1, n+1)}
for _ in range(k):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def virus_bfs(start_v):
    discovered = [start_v]
    queue = deque([start_v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(len(virus_bfs(1))-1)
