import re

cnt = 0
match = []
visited = []
l = 0
s = set()

def dfs(x):
    global cnt, visited, s
    if(x == l):
        s.add(tuple(visited))
        return
    
    for m in match[x]:
        if(visited[m] == True): continue
        visited[m] = True
        dfs(x+1)
        visited[m] = False

def solution(user_id, banned_id):
    global visited, l
    answer = 0
    l = len(banned_id)
    visited = [False for _ in range(len(user_id))]
    for b in banned_id:
        m = []
        b = b.replace('*','.')
        p = re.compile(b)
        for i, u in enumerate(user_id):
            if len(u) == len(b) and p.search(u):
                m.append(i)
        match.append(m)
        
    dfs(0)
    
    return len(s)
