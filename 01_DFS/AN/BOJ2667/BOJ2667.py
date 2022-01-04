import sys
 
dir =[[0, 1],[1, 0],[-1, 0],[0, -1]]
N = int (sys.stdin.readline ())
houses =[list(sys.stdin.readline ()) for i in range (N)]
scale =[]
 
for r in range (N):
    for c in range (N):
        if houses[r][c] == '1':
            stack = list()
            stack.append((r,c))
            houses[r][c] == '0'
            sc = 1
            while stack:
                node = stack.pop()
                houses[node[0]][node[1]] = '0'
                for d in dir:
                    x = node[0] + d[0] 
                    y = node[1] + d[1] 
                    if 0<=x < N and 0 <= y < N and houses[x][y] == '1':
                        houses[x][y] = '0' 
                        stack.append((x, y)) 
                        sc += 1 
            scale.append(sc)
scale.sort() 
print (len(scale)) 
for k in scale:
    print(k) 