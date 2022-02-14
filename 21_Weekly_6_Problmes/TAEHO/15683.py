from sys import stdin,maxsize
from copy import deepcopy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
directions = [[],
              [[0], [1], [2], [3]], 
              [[0, 1], [2, 3]], 
              [[0, 2], [2, 1], [1, 3], [3, 0]],
              [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]],
              [[0, 1, 2, 3]]]

def ISeeYou(temp,y,x,direction):
    temp_x,temp_y = x,y
    for i in direction:
        while True:
            x += dx[i]
            y += dy[i]
            if 0<=x<m and 0<=y<n and temp[y][x] != 6:
                temp[y][x] = 7
            else:
                break
        x,y = temp_x,temp_y

def dfs(room,cnt):
    global min_blind_spot
    if cnt == len(cctv):
        blind_spot = 0
        for i in range(n):
            blind_spot += room[i].count(0)
        min_blind_spot = min(blind_spot,min_blind_spot)
        return
    
    temp = deepcopy(room)
    direction,y,x = cctv[cnt]
    for i in directions[direction]:
        ISeeYou(temp,y,x,i)
        dfs(temp,cnt+1)
        temp = deepcopy(room)

n,m = map(int,stdin.readline().split())
room = []
cctv = []
min_blind_spot = maxsize
for i in range(n):
    data = list(map(int,stdin.readline().split()))
    room.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j],i,j])

cnt = 0
dfs(room,cnt)
print(min_blind_spot)