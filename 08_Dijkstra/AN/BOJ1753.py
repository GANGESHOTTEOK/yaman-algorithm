import sys
import heapq

INF = float('inf')

V,E = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(V+1)]
distance = [INF for _ in range(V+1)]
queue = []

for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v,w))

distance[start] = 0
heapq.heappush(queue, [distance[start], start])

while queue:
    curDis, curDest = heapq.heappop(queue)
    
    if distance[curDest] < curDis:
        continue
    
    for newDest, newDis in graph[curDest]:
        dist = curDis + newDis
        if dist < distance[newDest]:
            distance[newDest] = dist
            heapq.heappush(queue, [dist, newDest])
  
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])