
## [바이러스](https://www.acmicpc.net/problem/2606)
---

### 문제 설명
-  컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 감염.
- 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력
#### 입력
- 정수 N(1<=N<=100) : 컴퓨터의 수
- 정수 K : 결되어 있는 컴퓨터 쌍의 수
- K개의 서로 다른 X(0<=X<=M-1)와 Y(0<=Y<=N-1) : 연결되어 있는 컴퓨터의 번호 쌍(X,Y)

#### 출력
- **1번** 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의를 출력
---

### 문제 접근
- 각 컴퓨터를 노드, 네트워크상에서 연결된 컴퓨터들을 간선으로 연결한 그래프를 생각
- 1번 노드에서 너비 우선 탐색(BFS)를 시작하여 1번 노드와 연결된 컴퓨터의 수를 출력
- 컴퓨터의 수를 저장하는 변수 `count`는 1번 컴퓨터는 셈에 포함되지 않기때문에 `0`으로 초기화한다.
---

### 문제 풀이
``` Python
import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
net = [[0 for i in range(N+1)] for j in range(N+1)]         # 연결되어 있는 컴퓨터의 번호 쌍의 정보를 저장하는 이중배열
visited = [0 for i in range(N+1)]                           # 탐색 여부를 저장하는 배열
queue = deque([1])
visited[1] = 1
count = 0

for i in range(K):
    X, Y = map(int, sys.stdin.readline().split())
    net[X][Y] = net[Y][X] = 1
    
while queue:        # BFS
    x = queue.popleft()
    for k in range(N+1):
        if visited[k]==0 and net[x][k] == 1:
            queue.append(k)
            visited[k] = 1
            count += 1
            
print(count)
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148222767-2d1c6381-a217-4bb7-a480-806cfd5a10fb.png)](https://www.acmicpc.net/source/37084531)

---