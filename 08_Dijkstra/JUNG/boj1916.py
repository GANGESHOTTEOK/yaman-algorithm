import sys
import heapq
INF = sys.maxsize

def dijkstra(graph:dict, start:int, dist:list) -> None:
    pq = [] # 우선순위 큐
    dist[start] = 0
    heapq.heappush(pq, (dist[start], start))

    while pq:
        now_dist, now = heapq.heappop(pq)
        if dist[now] < now_dist:
            continue

        for weight, next in graph[now]:
            new_dist = now_dist + weight
            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(pq, (dist[next], next))


# 입력 부분
N = int(input()) # 정점의 개수
M = int(input()) # 버스의 개수 (간선의 개수)

dist = [INF] * (N + 1) # 각 정점의 시작 정점으로부터의 최소 경로 비용
graph = {i : [] for i in range(1, N + 1)} # 그래프

for _ in range(M):
    from_, to_, weight_ = map(int, sys.stdin.readline().split())
    graph[from_].append((weight_, to_)) # 방향 그래프

start, destination = map(int, input().split())
#

# 다익스트라 알고리즘을 사용하여 start부터 모든 정점까지의 최소 경로 비용을 구함
dijkstra(graph, start, dist)
print(dist[destination])