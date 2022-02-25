from operator import truediv
from sys import stdin

def check():
    for i in range(n):
        temp = i
        for j in range(h):
            if ladder[j][temp] == 1:
                temp += 1
            elif temp > 0 and ladder[j][temp-1] == 1:
                temp -= 1
        if temp != i:
            return False
    return True

def dfs(y,x,cnt):
    global answer
    if check():
        answer = min(answer,cnt)
        return

    elif cnt == 3 or answer <= cnt: 
        return

    for i in range(x, h):
        if i == x: k = y 
        else: k = 0 
        for j in range(k, n- 1):
            if ladder[i][j]==0 and ladder[i][j + 1]==0:
                if j > 0 and ladder[i][j - 1]: continue 
                ladder[i][j] = True 
                dfs(j+2,i,cnt + 1) 
                ladder[i][j] = False

n,m,h = map(int,stdin.readline().split())
ladder = [[0] * n for _ in range(h)]
answer = 4
if m == 0:
    print(0)
else:
    for _ in range(m):
        y,x = map(int,stdin.readline().split())
        ladder[y-1][x-1] = 1
    
    dfs(0,0,0)
    print(answer if answer<4 else -1)