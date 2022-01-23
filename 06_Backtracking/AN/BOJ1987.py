import sys

input = sys.stdin.readline

R, C = map(int, input().split())
dr,dc = [1,-1,0,0], [0,0,1,-1]
board = []
for i in range(R):
    board.append(input().rstrip())
max_len = 1
visited = [False]*(ord('Z')-ord('A')+1)
visited[ord(board[0][0])-65] = True

    
def dfs(r,c,depth):
    global max_len
    for i in range(4):
        row,col = r+dr[i], c+dc[i]
        if 0<=row<R and 0<=col<C:
            if visited[ord(board[row][col])-65]:
                continue
            visited[ord(board[row][col])-65] = True
            dfs(row,col,depth+1)
            visited[ord(board[row][col])-65] = False
            
    max_len = max(max_len, depth)

dfs(0,0,1)
print(max_len)