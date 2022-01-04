## [단지번호붙이기](https://www.acmicpc.net/problem/2667)
---

### 문제 설명
- 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타내는 지도
- **상하좌우**로 연결된 집의 모임을 단지라고 한다.
- 주어진 지도의 **단지의 개수**와 각 단지가 갖고있는 **집의 개수**를 구하라.
#### 입력
- 정수 N(5<=N<=25) : 정방행렬의 크기
- N개의 자료(0혹은 1) : 지도 정보, 집의 유무
#### 출력
- 첫 번째 줄에는 총 단지수를 
- 그리고 각 단지내 집의 수를 __오름차순__ 한 줄씩 출력
---

### 문제 접근
- 입력받은 행렬을 순회하며 `1`을 만날 경우 탐색을 시작하여 인근 노드들에 집이 확인한다.
- 탐색한 노드는 `0`으로 만들어줌으로써 탐색을 완료한 후 순회를 재개했을 때 같은 단지를 중복으로 세는 일이 없게한다.
- 단지의 집의 개수를 세는 변수 `sc`는 탐색을 시작하여 `stack`에 노드를 삽입할 때마다 `1`씩 증가시켜준다.
- 한 단지의 탐색이 끝나면 `sc`를 `list`형 변수인 `scale`에 삽입하여 `scale`의 길이를 단지의 개수로, 정렬하여 각 단지의 집의 개수를 오름차순으로 출력할 수 있게한다.
---

### 문제 풀이
``` Python
import sys
 
dir =[[0, 1],[1, 0],[-1, 0],[0, -1]]
N = int (sys.stdin.readline())
houses =[list(sys.stdin.readline()) for i in range (N)]    
scale =[]
 
for r in range (N):                     # (0,0)부터 순회
    for c in range (N):
        if houses[r][c] == '1':         # 집이 있으면 탐색 시작\
            # dfs(stack)
            stack = list()
            stack.append((r,c))
            houses[r][c] == '0'         # 중복 탐색 방지, 방문 여부 기록
            sc = 1
            while stack:
                node = stack.pop()
                houses[node[0]][node[1]] = '0'
                for d in dir:           # 이웃하는 노드 탐색
                    x = node[0] + d[0] 
                    y = node[1] + d[1] 
                    # (x,y)가 지도 내부이고 집이 있으면
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
- `list(sys.stdin.readline())`는 입력받은 줄을 `string`으로 받아오기 때문에 `'0'` 또는 `'1'`로 검사한다.
---

### 결과 및 한줄평

[![image](https://user-images.githubusercontent.com/54929223/148060348-ec10409a-7cb7-4599-a761-1ec58019f557.png)](https://www.acmicpc.net/source/37062675)
---