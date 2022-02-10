import sys
input = sys.stdin.readline

def isRoad(i,c):
    global ans
    cnt = 1
    for j in range(0,N-1):
        if c==1:
            d = board[i][j+1]-board[i][j]
        else:
            d = board[j+1][i]-board[j][i]
        if d==0:
            cnt += 1
        elif d==1 and cnt>=L:
            cnt=1
        elif d==-1 and cnt>=0:
            cnt = -L+1
        else:
            return
    if cnt>=0:
        ans += 1
        
N,L = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
ans=0
for k in range(0,N):
    isRoad(k,1)
    isRoad(k,0)
print(ans)