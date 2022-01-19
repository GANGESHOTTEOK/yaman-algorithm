import sys

input = sys.stdin.readline

R, C = map(int, input().split())
dr = [1,-1,0,0]
dc = [0,0,1,-1]
board = []
for i in range(R):
    board.append(input().rstrip())
duplicate = set(board[0][0])
max_len = 0
# visited = [[False]*C]*R
visited = [[False for i in range(C)] for j in range(R)]
visited[0][0] = True
# for i in range(R):
#     for j in range(C):
#         print(visited[i][j], end=' ')
#     print()
    
def dfs(r,c,depth):
    global max_len
    # print("=== dfs ", r, c, depth, " ===")
    for i in range(4):
        row = r + dr[i]
        col = c + dc[i]
        if 0<=row<R and 0<=col<C:
            # print(row,col)
            # print(visited[row][col])
            if visited[row][col]:
                continue
            alphabet = board[row][col]
            # print(row, col, alphabet)
            if alphabet in duplicate:
                max_len = max(max_len, depth)
                # print("it's duple", depth, max_len)
                continue
            duplicate.add(alphabet)
            visited[r][c] = True
            dfs(row,col,depth+1)
            duplicate.discard(alphabet)
            visited[row][col] = False

dfs(0,0,1)
# print(visited)
print(max_len)