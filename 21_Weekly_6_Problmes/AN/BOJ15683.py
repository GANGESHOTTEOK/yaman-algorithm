import sys
input = sys.stdin.readline

def makeRoom(i,j,direct,toggle):
    for dr,dc in direct:
        row,col = i+dr,j+dc
        while 0<=row<N and 0<=col<M:
            if room[row][col] == 6:
                break
            if not(1<=room[row][col]<=5):
                room[row][col] += toggle
            row,col = row+dr,col+dc

def dfs(depth):
    global answer
    if depth == len(cctvs):
        cnt=0
        for row in room:
            cnt += row.count(0)
        if cnt<answer:
            print(cnt)
            for row in room:
                print(*row)
        answer = min(answer, cnt)
        return
    
    r,c,TVnum = cctvs[depth]
    for direction in cctv[TVnum]:
        makeRoom(r,c,direction,-1)
        dfs(depth+1)
        makeRoom(r,c,direction,1)

N,M = map(int,input().split())
room = []
for _ in range(N):
    room.append(list(map(int,input().split())))
    
cctvs = []
for i in range(N):
    for j in range(M):
        if 1<=room[i][j]<=5:
            cctvs.append((i,j,room[i][j]))
cctv = {
    1: [[(-1,0)],[(0,1)],[(1,0)],[(0,-1)]],
    2: [[(-1,0),(1,0)],[(0,-1),(0,1)]],
    3: [[(-1,0),(0,1)],[(0,1),(1,0)],[(1,0),(0,-1)],[(-1,0),(0,-1)]],
    4: [[(0,-1),(-1,0),(0,1)],[(0,-1),(1,0),(0,1)],
        [(1,0),(0,-1),(-1,0)],[(1,0),(0,1),(-1,0)],],
    5: [[(-1,0),(0,1),(1,0),(0,-1)]]
}
answer = sys.maxsize

dfs(0)
print(answer)

