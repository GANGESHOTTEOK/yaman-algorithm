import sys

input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())

costs = []
dist = [INF] * (N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    costs.append((A,B,C))
    
def bellman(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur = costs[j][0]
            dest = costs[j][1]
            cost = costs[j][2]
            
            if dist[cur] != INF and dist[dest] > dist[cur] + cost:
                dist[dest] = dist[cur] + cost
                if i == N-1:
                    return True
    return False

neg = bellman(1)
if neg:
    print('-1')
else:
    for i in range(2,N+1):
        print("-1") if dist[i] == INF else print(dist[i])