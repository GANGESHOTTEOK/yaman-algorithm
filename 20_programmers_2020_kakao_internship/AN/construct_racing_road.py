from collections import deque
import sys
# 직선 100원, 코너 500원

def solution(board):
    N = len(board)    
    dx = [-1,1,0,0] # 상 하 좌 우
    dy = [0,0,1,-1]
    cost = [[sys.maxsize for _ in range(N)] for i in range(N)]
    cost[0][0] = 0
    que = deque([(0,0,0,0)]) # i,j,direction,cost
    while que:
        r,c,before,cur_cost = que.popleft()
        for after in range(4):
            row = r+dx[after]
            col = c+dy[after]
            if 0<=row<N and 0<=col<N:
                if board[row][col]==1:
                    continue
                new_cost = cur_cost
                if r==0 and c==0:
                    new_cost += 100
                else:
                    if before==after:
                        new_cost += 100
                    else:
                        new_cost += 600
                if cost[row][col] >= new_cost:
                    cost[row][col] = new_cost
                    que.append((row,col,after,new_cost))
            
    return cost[-1][-1]