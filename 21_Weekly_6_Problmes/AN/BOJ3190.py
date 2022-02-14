from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# input
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
    
dr = [0,1,0,-1] # 우 하 좌 상
dc = [1,0,-1,0]
snake = deque([(1,1)])  # snake body
time = d = 0    # time, direction
r = c = 1

# game start
while True:
    if changeD[time] != '':         # direction change
        if changeD[time] == 'D':
            d = (d+1)%4
        else:
            d = (d+3)%4
            
    time += 1
    r,c = r+dr[d], c+dc[d]
    
    if not (0<r<=N and 0<c<=N) or (r,c) in snake: # game over : out of range or crash itself
        break
    
    snake.append((r,c)) # head+1
    
    if board[r][c]==0:  # if not apple
        snake.popleft() # tail-1
    else:               # if apple
        board[r][c] = 0 # eat apple
        
print(time)