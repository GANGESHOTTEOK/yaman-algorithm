## [단지번호붙이기](https://www.acmicpc.net/problem/2667)
---

### 문제 설명
- 
---

### 문제 접근
---

### 문제 풀이
``` Python
import sys
 
dir =[[0, 1],[1, 0],[-1, 0],[0, -1]]
N = int (sys.stdin.readline ())
houses =[list(sys.stdin.readline ()) for i in range (N)]
cnt = 0
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
```
---

### 결과 및 한줄평

[![image](https://user-images.githubusercontent.com/54929223/148060348-ec10409a-7cb7-4599-a761-1ec58019f557.png)](https://www.acmicpc.net/source/37062675)
---