import heapq
import sys
INF = sys.maxsize

# 정점의 개수 V, 간선의 개수 E
V, E = map(int, sys.stdin.readline().split())
# 시작 정점의 번호 K
K = int(input())
distance = [INF] * (V+1)

graph = {i:[] for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start:int):
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        now_dist, now = heapq.heappop(pq)
        if distance[now] < now_dist:
            continue

        for next, weight in graph[now]:
            new_dist = now_dist + weight
            if new_dist < distance[next]:
                distance[next] = new_dist
                heapq.heappush(pq, (new_dist, next))

dijkstra(K)
for i in range(1, V+1):
    print("INF" if distance[i] == INF else distance[i])
