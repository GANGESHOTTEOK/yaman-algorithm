
## [숨바꼭질](https://www.acmicpc.net/problem/1697)
---

### 문제 설명
- 점 X에서 1초 동안 이동할 수 있는 거리는 X+1, X-1, 2*X
- 빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 최소 시간을 구하라

#### 입력
- 정수 N(1<=N<=100,000) : 수빈이의 현재 위치
- 정수 K(1<=K<=100,000) : 동생의 위치

#### 출력
- 수빈이가 동생을 찾는 가장 빠른 시간을 출력
---

### 문제 접근
- 각 점을 노드, 1초 동안 이동할 수 있는 노드들을 간선으로 연결한 그래프를 생각
- BFS(너비 우선 탐색)을 사용하여 동생의 위치에 해당하는 점을 찾았을 때의 깊이(Depth)를 출력
- (점의 위치, 깊이)인 순서쌍을 원소로하는 `queue`를사용한다.
---

### 문제 풀이
``` Python
import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
queue = deque([(N,0)])
visited = set([N])
        
while queue:
    x,depth = queue.popleft()
    if x==K:
        print(depth)
        break
    for n in [x-1, x+1, 2*x]:
        if n not in visited and 0<=n<=100000:
            visited.add(n)
            queue.append((n,depth+1))
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148221599-f2dc37dd-d4a5-49c4-95ee-ae5e14b54cf4.png)](https://www.acmicpc.net/source/37082236)

---