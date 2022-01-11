from sys import stdin
from collections import deque


max_count = -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]


## -----------backtracking 시간초과 엄청걸림--------------##
def backtracking(x,y,count):
    global max_count
    max_count = max(max_count,count)
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0<=new_x<r and 0<=new_y<c and visit_alpha[matrix[new_x][new_y]]==0:
            visit_alpha[matrix[new_x][new_y]] = 1
            backtracking(new_x,new_y,count+1)
            visit_alpha[matrix[new_x][new_y]] = 0

            
r,c = map(int,stdin.readline().split())
matrix = []
visit_alpha = [0]*26
for _ in range(r):
    matrix.append(list(map(lambda x: ord(x)-65,stdin.readline().rstrip())))
    

visit_alpha[matrix[0][0]] = 1
backtracking(0,0,1)
print(max_count)

## -----------------bfs----------------- ##
# def bfs(x,y):
#     global max_count
#     q =  set((x,y,matrix[0][0])) #set 자료구조를 queue처럼 사용

#     while q:
#         x,y,alpha = q.pop() 

#         for i in range(4):
#             new_x = x + dx[i]
#             new_y = y + dy[i]
#             if 0<=new_x<r and 0<=new_y<c and (not matrix[new_x][new_y] in alpha):
#                 max_count = max(max_count, len(alpha)+1)
#                 q.add((new_x,new_y,alpha+matrix[new_x][new_y]))

# r,c = map(int,stdin.readline().split())
# matrix = []
# for _ in range(r):
#     matrix.append(list(stdin.readline().rstrip()))
    
# bfs(0,0)
# print(max_count)