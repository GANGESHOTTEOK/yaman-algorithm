from sys import stdin
from collections import deque

direction = [(0,1),(1,0),(0,-1),(-1,0)] #-> 우 하 좌 상
n = int(stdin.readline())
k = int(stdin.readline())
matrix = [[0]*n for _ in range(n)]
time,dir = 0,0
snake = deque([[0,0]])
rot = deque()
for _ in range(k):
    y, x = map(int,stdin.readline().split())
    matrix[y-1][x-1] = 1
l = int(stdin.readline())
for _ in range(l):
    x, d = stdin.readline().split()
    rot.append([int(x),d])
#--------------input -----------------#

matrix[0][0] = 2 #start snake

while True:
    new_y = snake[-1][0] + direction[dir][0]
    new_x = snake[-1][1] + direction[dir][1]
    time += 1

    if 0<=new_y<n and 0<=new_x<n:
        if matrix[new_y][new_x] == 0:
            del_y,del_x = snake.popleft()
            matrix[del_y][del_x] = 0

        if matrix[new_y][new_x] == 2: #자기자신에게 부딪히는 경우
            break

        snake.append([new_y,new_x])
        matrix[new_y][new_x] = 2

        if rot and time == rot[0][0]:
            _, rotation = rot.popleft()
            dir = (dir + 1)%4 if rotation == 'D' else (dir - 1)% 4  #회전

    else: #벽에 부딪히는 경우
        break

print(time)