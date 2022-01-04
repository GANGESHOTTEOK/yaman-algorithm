
## [유기농 배추](https://www.acmicpc.net/problem/1012)
---

### 문제 설명
- 배추흰지렁이를 사용하여 유기농 배추농사를 짓는데, 이 벌레는 배추 근처에 서식하며 상하좌우로 인근해 있는 배추들을 이동하며 해충을 먹는다. 
- 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
- 주어진 배추 밭에서 최소로 필요한 배추흰지렁이의 최소 마리 수를 구하라.
#### 입력
- 정수 T : 테스트 케이스 수
- 정수 M(1<=M<=50) : 가로의 길이
- 정수 N(1<=N<=50) : 세로의 길이
- 정수 K(1<=K<=2500) : 배추가 심겨져있는 위치의 개수
- K개의 서로 다른 X(0<=X<=M-1)와 Y(0<=Y<=N-1) : 배추가 심겨져 있는 위치 정보(X,Y)

#### 출력
- 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.
---

### 문제 접근
- 입력받은 행렬을 순회하며 `1`을 만날 경우 탐색을 시작하여 인근 노드들에 배추가 심겨있는지 확인한다.
- 탐색한 노드는 `0`으로 만들어줌으로써 탐색을 완료한 후 순회를 재개했을 때 같은 무리를 중복으로 세는 일이 없게한다.
- 배추 무리의 개수를 세는 변수 `cnt`는 `1`을 만나 탐색을 시작할 때 증가시켜준다.
---

### 문제 풀이
``` Python
import sys

dir = [[0,1],[1,0],[-1,0],[0,-1]]
T = int(sys.stdin.readline())

for t in range(T):
    N,M,K = map(int, sys.stdin.readline().split())      # 행,열,배추 개수
    field = [[0 for i in range(M)] for j in range(N)]   # N*M배열
    cnt = 0                                             # 배추 군락 개수
    
    for k in range(K):
        r,c = map(int, sys.stdin.readline().split())
        field[r][c] = 1
        
    for r in range(N):
        for c in range(M):                              # (0,0)부터 밭 순회
            if field[r][c] == 1:                        # 배추 심겨있으면 탐색 시작

                # dfs(stack 사용)
                stack = list()
                stack.append((r,c))
                field[r][c] == 0                        # 중복 탐색 방지, 방문 여부 기록
                cnt += 1
                
                while stack:
                    node = stack.pop()
                    for d in dir:                       # 이웃하는 노드 탐색
                        x = node[0]+d[0]
                        y = node[1]+d[1]

                        # (x,y)가 밭 내부이고 배추가 심겨져있으면
                        if 0<=x<N and 0<=y<M and field[x][y]==1:    
                            field[x][y] = 0
                            stack.append((x,y))
    print(cnt)
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148062161-731f6dd8-248e-42df-ae71-2657fe0925ac.png)](https://www.acmicpc.net/source/37062675)

---