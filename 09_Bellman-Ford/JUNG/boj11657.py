import sys
INF = sys.maxsize

def get_shortest_path(graph, start, dist) -> bool:
    dist[start] = 0

    for i in range(len(graph)): # 정점 개수 N만큼 반복
        for from_, neighbors in graph.items():
            for weight_, to_ in neighbors:
                if dist[from_] != INF and dist[from_] + weight_ < dist[to_]:
                    dist[to_] = dist[from_] + weight_
                    # N-1번째에도 값이 갱신된다면 음수 사이클이 존재
                    if i == len(graph) - 1:
                        return True

    # 음수 사이클이 존재하지 않음
    return False

# 입력 부분 #
N, M = map(int, input().split())
graph = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    from_, to_, weight_ = map(int, sys.stdin.readline().split())
    graph[from_].append((weight_, to_))
#

dist = [INF] * (N + 1) # 시작 정점으로부터 각 정점까지의 최단 경로 비용

if get_shortest_path(graph, 1, dist):
    # 음수 사이클이 존재한다면
    print(-1)
else:
    for i in range(2, len(dist)):
        # 해당 도시로 가는 경로가 없다면 -1을 출력
        print(-1 if dist[i] == INF else dist[i])