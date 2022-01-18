import sys

input = sys.stdin.readline
INF = sys.maxsize
# float('inf')는 음수를 더해도 갱신되지 않음

N, M = map(int, input().split())

costs = []
dist = [INF] * (N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    costs.append((A,B,C))
    
def bellman(start):
    dist[start] = 0
    for i in range(N):
        for cur, dest, cost in costs:
            if dist[cur] != INF and dist[dest] > dist[cur] + cost:
                dist[dest] = dist[cur] + cost
                if i == N-1:
                    return True
    return False

if bellman(1):
    print(-1)
else:
    for i in range(2,N+1):
        print(-1 if dist[i] == INF else dist[i]) 