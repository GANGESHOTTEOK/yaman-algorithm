locas = []

def check(y,x,board,friend):
    temp = []
    for i in range(y,y+2):
        for j in range(x,x+2):
            if board[i][j] != friend:
                
                return False
            temp.append((i,j))
    locas.append(temp)
    return True

def solution(m, n, board):
    board = [list(x) for x in board]
    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0':
                    check(i,j,board,board[i][j])
        
        if locas == []:
            break
        
        while locas:
            loca = locas.pop()
            for y,x in loca:
                board[y][x] = '0'
        
        for j in range(n):
            blank = 0
            for i in range(m-1,-1,-1):
                if board[i][j] == '0':
                    blank += 1
                else:
                    board[i+blank][j] = board[i][j]
                    if blank != 0:
                        board[i][j] = '0'
                        
    return sum(map(lambda x : x.count('0') ,board))
