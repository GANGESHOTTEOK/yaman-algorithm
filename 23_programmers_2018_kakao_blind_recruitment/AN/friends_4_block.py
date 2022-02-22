sr = [0,1,1]
sc = [-1,0,-1]

def elimTile(board, blocks):
    for row, col in blocks:
        board[row][col] = '1'
    for row in board:
        while row.count('1'):
            row.pop(row.index('1'))
            row.append('0')
    return 

def isBlock(r,c,board,blocks):
    tile = board[r][c]
    for i in range(3):
        row,col = r+sr[i],c+sc[i]
        if board[row][col] != tile or board[row][col] == '0':
            return False
    blocks.add((r,c))
    for i in range(3):
        blocks.add((r+sr[i],c+sc[i]))
    return True
    
def solution(m, n, board):
    answer = 0
    board = [[board[i][j] for i in range(m-1,-1,-1)] for j in range(n)]
    isFound = 1
    while isFound:
        isFound = 0
        blocks = set()
        for j in range(m-1,0,-1):
            for i in range(n-1): 
                if isBlock(i,j,board,blocks):
                    isFound = 1
        answer += len(blocks)
        elimTile(board,blocks)
    return answer