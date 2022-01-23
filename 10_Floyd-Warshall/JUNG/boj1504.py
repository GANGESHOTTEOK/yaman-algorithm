import sys, heapq
INF = sys.maxsize

def dijkstra(graph:dict, start:int, vertex_num:int) -> list:
    dist = [INF] * (vertex_num + 1)
    heap = []

    dist[start] = 0
    heapq.heappush(heap, (dist[start], start))

    while heap:
        now_dist, now = heapq.heappop(heap)
        if dist[now] < now_dist:
            continue
        for weight, next in graph[now]:
            if now_dist + weight < dist[next]:
                dist[next] = now_dist + weight
                heapq.heappush(heap, (dist[next], next))

    return dist


# 입력 부분 #
N, E = map(int, input().split())
graph = {i : [] for i in range(N+1)}
for _ in range(E):
    from_, to_, weight_ = map(int, sys.stdin.readline().split())
    graph[from_].append((weight_, to_))
    graph[to_].append((weight_, from_))
v1, v2 = map(int, input().split())
#

dist_from_1  = dijkstra(graph,  1, N)
dist_from_v1 = dijkstra(graph, v1, N)
dist_from_v2 = dijkstra(graph, v2, N)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

if dist_from_1[N] == INF:
    print(-1)
else:
    print(min(path1, path2))