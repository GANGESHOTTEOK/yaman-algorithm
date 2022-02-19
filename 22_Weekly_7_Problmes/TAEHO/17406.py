from sys import stdin,maxsize
from copy import deepcopy

def rotating(matrix,r,c,s):
    while s > 0:
        temp = matrix[r-s][c-s]
        for y in range(r-s+1,r+s+1):
            matrix[y-1][c-s] = matrix[y][c-s]
        for x in range(c-s+1,c+s+1):
            matrix[r+s][x-1] = matrix[r+s][x] 
        for y in range(r+s,r-s,-1):
            matrix[y][c+s] = matrix[y-1][c+s]
        for x in range(c+s,c-s,-1):
            matrix[r-s][x] = matrix[r-s][x-1]
        matrix[r-s][c-s+1] = temp
        s -= 1

def BT(cnt,perm):
    global ans
    if cnt == k:
        matrix = deepcopy(A)
        for p in perm:
            r,c,s = p
            rotating(matrix,r-1,c-1,s)
        ans= min(ans,min(map(sum,matrix)))
        return

    for i in range(len(rotate)):
        if visit[i] == 0: 
            visit[i] = 1
            perm.append(rotate[i])
            BT(cnt+1,perm)
            perm.pop()
            visit[i] = 0
        
n,m,k = map(int,stdin.readline().split())
A = [list(map(int,stdin.readline().split())) for _ in range(n)]
rotate = [list(map(int,stdin.readline().split())) for _ in range(k)]
visit = [0]*len(rotate)
ans = maxsize

BT(0,[])
print(ans)