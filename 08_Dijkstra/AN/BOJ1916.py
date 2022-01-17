import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())

graph = [[] for j in range(N+1)]
distance = [INF for i in range(N+1)]
queue = []

for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    
start, end = map(int, input().split())

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
    
print(distance[end])