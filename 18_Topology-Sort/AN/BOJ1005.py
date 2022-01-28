from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,K = map(int, input().split())
    D = [0]+list(map(int,input().split()))
    
    craft = [[] for i in range(N+1)]
    indegree = [0]*(N+1)
    dp = [time for time in D]
    for i in range(K):
        X,Y = map(int, input().split())
        craft[X].append(Y)
        indegree[Y] += 1
    
    que = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = D[i]
    while que:   
        x = que.popleft()
        for k in craft[x]:
            indegree[k] -= 1
            dp[k] = max(dp[k],dp[x]+D[k])
            if indegree[k] == 0:
                que.append(k)
    
    print(dp[int(input())])