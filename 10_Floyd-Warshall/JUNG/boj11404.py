import sys
INF = sys.maxsize

def floyd_warshall(graph, vertex_num):
    for mid in range(1, vertex_num + 1):
        for start in range(1, vertex_num + 1):
            for end in range(1, vertex_num + 1):
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

# 입력 부분 #
n = int(input())
m = int(input())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)] # 인접 행렬 그래프
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0 # graph[i][i] = 0

for _ in range(m):
    from_, to_, weight_ = map(int, sys.stdin.readline().split())
    if graph[from_][to_] > weight_:
        graph[from_][to_] = weight_
#

# 플로이드-워셜 알고리즘으로 모든 정점 사이의 최단거리를 구함
floyd_warshall(graph, n)

# 출력 부분 #
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if graph[i][j] == INF else graph[i][j], end=' ')
    print()
#