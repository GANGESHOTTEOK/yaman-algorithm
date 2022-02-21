from sys import stdin,maxsize
from collections import deque

def bfs(g):
    visit_bfs = [0]*(n+1)
    q = deque()
    q.append(g[0])
    visit_bfs[g[0]] = 1
    num = people[g[0]]
    length = 1
    while q:
        node = q.popleft()
        for adj_node in graph[node]:
            if adj_node in g and visit_bfs[adj_node] == 0:
                num += people[adj_node]
                visit_bfs[adj_node] = 1
                length += 1
                q.append(adj_node)
    return num,length

def BT(cnt,idx,e):
    global ans
    if cnt == e:
        graph1 = [i for i in range(1,n+1) if visit[i] == 1]
        graph2 = [i for i in range(1,n+1) if visit[i] == 0]
        num1,length1 = bfs(graph1)
        num2,length2 = bfs(graph2)
        if length1 + length2 == n:
            ans = min(ans,abs(num1-num2))
        return
        
    for i in range(idx,n+1):
        if visit[i]:
            continue
        visit[i] = 1
        BT(cnt+1,i,e)
        visit[i] = 0
    return ans

n = int(stdin.readline())
graph = {node:set() for node in range(1,n+1)}
people = [0] + [i for i in map(int,stdin.readline().split())]
visit = [0]*(n+1)
for i in range(1,n+1):
    adj_v = list(map(int,stdin.readline().split()))[1:]
    for v in adj_v:
        graph[i].add(v)
        graph[v].add(i)

ans = maxsize
for i in range(1,n//2+1):
    BT(0,1,i)

print(-1 if ans==maxsize else ans)