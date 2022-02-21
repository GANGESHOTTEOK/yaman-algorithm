from collections import deque
from sys import maxsize

def solution(board):
    def bfs(start):
        visit = [[maxsize]*len(board) for _ in range(len(board))]
        dx = [-1,1,0,0] #왼 오
        dy = [0,0,-1,1] #상 하
        q = deque([start])
        visit[0][0] = 0
        while q:
            y,x,value,direction = q.popleft()
            for i in range(4):
                new_y, new_x = y+dy[i],x+dx[i]
                if 0<=new_y<len(board) and 0<=new_x<len(board) and board[new_y][new_x] == 0:
                    new_value = value+100 if direction == i else value+600
                    if visit[new_y][new_x] > new_value:
                        visit[new_y][new_x] = new_value
                        q.append([new_y,new_x,new_value,i])
                    
        return visit[len(board)-1][len(board)-1]
    
    return min(bfs([0,0,0,1]),bfs([0,0,0,3]))