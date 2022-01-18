import sys

input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())

costs = []
distances = [INF] * (N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    costs.append((A,B,C))
    
def bellman(start):
    distances[start] = 0
    for i in range(N):
        for j in range(M):
            cur = costs[j][0]
            dest = costs[j][1]
            cost = costs[j][2]
            
            if distances[cur] != INF and distances[dest] > distances[cur] + cost:
                distances[cur] = distances[cur] + cost
                if i == N-1:
                    return True
    return False

neg = bellman(1)

if neg:
    print('-1')
else:
    for i in range(2,N+1):
        if distances[i] == INF:
            print("-1")
        else:
            print(distances[i])
    