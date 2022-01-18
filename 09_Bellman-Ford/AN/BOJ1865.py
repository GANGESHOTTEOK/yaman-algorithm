import sys

input = sys.stdin.readline
INF = 2000000000

def bellman(V, E, costs):
    dist = [INF] * (V+1)
    dist[1] = 0
    for i in range(V):
        for j in range(E):
            cur = costs[j][0]
            dest = costs[j][1]
            cost = costs[j][2]
            if dist[dest] > dist[cur] + cost:
                dist[dest] = dist[cur] + cost
                if i == V-1:
                    return True
    return False

TC = int(input())

for _ in range(TC):
    N,M,W = map(int, input().split())
    times = []
    for i in range(M):
        S,E,T = map(int, input().split())
        times.append((S,E,T))
        times.append((E,S,T))
    for j in range(W):
        S,E,T = map(int, input().split())
        times.append((S,E,T*(-1)))
        
    print("YES" if bellman(N,W+2*M,times) else "NO")
    
