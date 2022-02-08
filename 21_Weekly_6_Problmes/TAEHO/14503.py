from sys import stdin
from collections import deque
direction = [(-1,0),(0,1),(1,0),(0,-1)] #북 동 남 서

n,m = map(int, stdin.readline().split())
r,c,d = map(int,stdin.readline().split())
loca = []
for _ in range(n):
    loca.append(list(map(int,stdin.readline().split())))

loca[r][c] = 2
count = 1
while True:
    flag = 1
    for i in range(4):
        d = (d-1)%4
        if 0<=r+direction[d][0]<n and 0<= c+direction[d][1]<m and loca[r+direction[d][0]][c+direction[d][1]] == 0:  #조건1
            r = r+direction[d][0]
            c = c+direction[d][1]
            loca[r][c] = 2
            count += 1
            flag = 0
            break
    
    if flag:
        if 0<=r-direction[d][0]<n and 0<= c-direction[d][1]<m and loca[r-direction[d][0]][c-direction[d][1]] != 1:
            r = r-direction[d][0]
            c = c-direction[d][1]
        else:
            break
    
print(count)