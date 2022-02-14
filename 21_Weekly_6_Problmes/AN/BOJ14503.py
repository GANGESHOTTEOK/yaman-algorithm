import sys
input = sys.stdin.readline

# input
N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = []   # N X M
for _ in range(N):
    board.append(list(map(int,input().split())))
    
dr = [-1,0,1,0]   # 북 서 남 동
dc = [0,-1,0,1]
cnt = 0
if d==1:
    d=3
elif d==3:
    d=1

# run robot
while True:
    if board[r][c] == 0:    # clean up
        board[r][c] = -1
        cnt += 1
        
    for i in range(1,5):    # check four directions
        d = (d+1)%4         # turn left
        row,col = r+dr[d],c+dc[d]   # get index of next
        if board[row][col] == 0:    # robot can clean up
            break
        if i==4:    # all directions are checked
            i=5
            
    if i == 5:          # all derections cannot be cleaned up
        row, col = r+dr[(d+2)%4], c+dc[(d+2)%4] # back
        if board[row][col] == 1:    # cannot back
            break                   # robot done
    r,c = row,col

print(cnt)