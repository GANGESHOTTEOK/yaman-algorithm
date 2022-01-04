import sys

dir = [[0,1],[1,0],[-1,0],[0,-1]]
T = int(sys.stdin.readline())

for t in range(T):
    N,M,K = map(int, sys.stdin.readline().split())
    field = [[0 for i in range(M)] for j in range(N)]
    cnt = 0
    
    for k in range(K):
        r,c = map(int, sys.stdin.readline().split())
        field[r][c] = 1
        
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                stack = list()
                stack.append((r,c))
                field[r][c] == 0
                cnt += 1
                while stack:
                    node = stack.pop()
                    for d in dir:
                        x = node[0]+d[0]
                        y = node[1]+d[1]
                        if 0<=x<N and 0<=y<M and field[x][y]==1:
                            field[x][y] = 0
                            stack.append((x,y))
    print(cnt)