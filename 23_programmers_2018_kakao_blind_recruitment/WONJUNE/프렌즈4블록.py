def solution(m, n, board):
    answer = 0
    b = [[0 for _ in range(m)] for _ in range(n)]
    change = [True for _ in range(n)]
    for i in range(m):
        for j in range(n):
            b[j][i] = board[m-1-i][j]
    while True:
        s = set()
        for i in range(n-1):
            if not change[i] and not change[i+1] or len(b[i]) < 2 or len(b[i+1]) < 2: continue
            row1, row2 = b[i], b[i+1]
            block = [[row1[0],row2[0]],['','']]
            preCheck = False
            if row1[0] == row2[0]:
                preCheck = True
            for j in range(1,min(len(row1),len(row2))):
                block[1] = block[0]
                block[0] = [row1[j], row2[j]]
                if preCheck:
                    if row1[j] == row2[j]:
                        if row1[j] == block[1][0]:
                            s.update([(i+1,j), (i+1,j-1), (i,j), (i,j-1)])
                        else:
                            if row1[j] == row2[j]:
                                preCheck = True
                            else:
                                preCheck = False
                    else:
                        preCheck = False
                else:
                    if row1[j] == row2[j]:
                        preCheck = True
        if not bool(s): return answer
        answer += len(s)
        s = sorted(s, key = lambda x : x[1], reverse=True)
        newChange = [False for _ in range(n)]
        for e in s:
            b[e[0]].pop(e[1])
            newChange[e[0]] = True
        change = newChange
        
    
