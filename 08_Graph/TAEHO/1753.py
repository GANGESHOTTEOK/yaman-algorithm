import heapq
from sys import stdin,maxsize
import heapq as hq

def dijacstra(k):
    distances = {node:maxsize for node in range(1,V+1)}
    distances[k] = 0
    q = []
    hq.heappush(q,(distances[k],k))
    while q:
        current_distance, node = hq.heappop(q)
        if current_distance > distances[node]:
            continue

        for adjancancy_node, distance in graph[node].items():
            weighted_distance = distance + current_distance
            if weighted_distance < distances[adjancancy_node]:
                distances[adjancancy_node] = weighted_distance
                hq.heappush(q,(weighted_distance,adjancancy_node))

    return distances

V,E = map(int,stdin.readline().split())
k = int(stdin.readline())
graph = {node:{} for node in range(1,V+1)}
for _ in range(E):
    s,e,v = map(int,stdin.readline().split())
    if e in graph[s]:
        graph[s][e] = min(graph[s][e],v)
    else:
        graph[s][e] = v

result = dijacstra(k)

for ans in result.values():
    if ans == maxsize:
        print("INF")
    else:
        print(ans)
