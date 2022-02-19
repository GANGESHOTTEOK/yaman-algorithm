from sys import stdin
from copy import deepcopy
from collections import deque

def bfs(y,x,game_map):
    game_map_visit = [[0]*m for _ in range(n+1)]
    dx = [-1,0,1]
    dy = [0,-1,0]
    q = deque()
    q.append([y,x,0])
    start = y
    game_map_visit[y][x] = 1
    min_y,min_x,min_length = 100,100,d+1
    while q:
        y, x, length = q.popleft()
        if min_length > length and length != 0 and game_map[y][x] == 1:
            min_y,min_x = y, x
            break
        for i in range(3):
            new_y,new_x = y+dy[i], x+dx[i]
            if 0<=new_y<start and 0<=new_x<m and length+1 <= d and game_map_visit[new_y][new_x] == 0:
                q.append([new_y,new_x,length+1])
                game_map_visit[new_y][new_x] = 1
    return min_y,min_x

def start(archer):
    temp = deepcopy(game_map)
    kill = 0
    shoot = set()
    standing = n
    while standing != 0:
        enemy = False
        for i in range(standing):
            for j in range(m):
                if temp[i][j] == 1:
                    enemy = True
        if not enemy:
            break
        else:
            for ar in archer:
                y,x = bfs(standing,ar,temp)
                if y != 100 and x != 100:
                    shoot.add((y,x))
            while shoot:
                y,x = shoot.pop()
                temp[y][x] = 0
                kill += 1
            standing -= 1
    return kill

def BT(cnt):
    global max_kill
    if cnt == 3:
        max_kill = max(max_kill,start(archer))
        return
    for i in range(cnt,m):
        if cnt == 0 or archer[-1] < i:
            archer.append(i)
            BT(cnt+1)
            archer.pop()
    
n,m,d = map(int,stdin.readline().split())
game_map = []
max_kill = 0
archer = []

for _ in range(n):
    game_map.append(list(map(int,stdin.readline().split())))

BT(0)
print(max_kill)
