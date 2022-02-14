from collections import defaultdict, deque
import sys
input = sys.stdin.readline
dr = [0,1,0,-1] # 우 하 좌 상
dc = [1,0,-1,0]
N = int(input())
K = int(input())
board = [[0]*(N+1) for i in range(N+1)]
for _ in range(K):
    r,c = map(int,input().split())
    board[r][c] = 1
L = int(input())
changeD = defaultdict(str)
for _ in range(L):
    X,C = map(str,input().split())
    changeD[int(X)] = C
snake = deque([(1,1)])
time = d = 0
r = c= 1
while True:
    if changeD[time] != '':
        if changeD[time] == 'D':
            d = (d+1)%4
        else:
            d = (d+3)%4
    time += 1
    r = r+dr[d]
    c = c+dc[d]
    if not (0<r<=N and 0<c<=N) or (r,c) in snake:
        break
    snake.append((r,c))
    if board[r][c]==0:
        snake.popleft()
    else:
        board[r][c] = 0
        
print(time)