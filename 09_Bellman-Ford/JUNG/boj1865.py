import sys
INF = sys.maxsize

def check_negative_cycle(graph, vertex_num, edge_num, start, dist):
    dist[start] = 0

    for i in range(vertex_num):
        for j in range(edge_num):
            now = graph[j][0]
            next = graph[j][1]
            weight = graph[j][2]

            if dist[now] + weight < dist[next]:
                dist[next] = dist[now] + weight

                if i == vertex_num - 1:
                    print("YES")
                    return
    print("NO")
    return

TC = int(input())
while TC:
    TC -= 1

    graph = []
    N, M, W = map(int, input().split())
    for _ in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int,sys.stdin.readline().split())
        graph.append((s, e, -t))

    dist = [INF] * (N + 1)
    check_negative_cycle(graph, N, 2*M + W, 1, dist)