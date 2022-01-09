## DFS and BFS

---

그래프 순회란 그래프 탐색(search)이라고도 불리며, 그래프의 각 정점을 방문하는 과정을 말한다.
그래프의 각 정점을 방문하는 그래프 순회에는 크게 깊이 우선 탐색(Deapth First Search, 이하 DFS)와 너비 우선 탐색(Breath First Search, 이하 BFS)가 있다.
DFS는 주로 스택으로 구현하거나 재귀로 구현하며, BFS는 주로 큐로 구현한다.

---

#### 재귀 구조로 구현한 DFS

```
  DFS(G, v)
    label v as discovered
    for all directed deges from v to w that are in G.adjacentEdges(v) do
      if vertex w is not labeled as discovered then
        recursively call DFS(G, w)
```

#### 스택으로 구현한 DFS
```
  DFS-stack(G, v)
  let S be a stack
  S.push(v)
  while S is not empty do
    v = S.pop()
    if v is not labeled as discovered then
      label v as discovered
      for all edges from v to w in G.adjacentEdges(v) do
        S.push(w)
```        

#### 큐로 구현한 BFS
```
  BFS(G, start_v)
    let Q be queue
    label start_v as discovered
    Q.enqueue(start_v)
    while Q is not empty do
      v := Q.dequeue()
      for all edges from v to w in G.adjacentEdges(v) do
        if w is not labeled as discovered then
          label w as discovered
          w.parent := w
          Q.enqueue(w)
```


## [단지번호붙이기](https://www.acmicpc.net/problem/2667)
---

### 문제 설명
---
정사각형 모양의 지도가 주어지고 1은 집이 있는 곳, 0은 집이 없는 곳이다. 지도 상에서 1이 연결되어 있으면 단지이다. 주어진 정사각형 모양의 지도에서 단지의 수를 계산하고
각 단지의 집의 수를 오름차순으로 정렬하여 출력해야한다.

### 문제 접근
---
전형적인 그래프 탐색 문제이다. DFS와 BFS로 모두 풀 수 있다. 제시된 코드는 재귀적인 DFS로 풀이하였다.

### 문제 풀이
---
데이터 입력 부분이다.
```
# input data
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
```
---

해당 좌표가 0인지 1인지 확인하고, 0이면 False를 return, 1이면 DFS를 이용하여 해당 단지 내 모든 집을 0으로 만들어버린다.
그리고 True를 return한다.
해당 단지 내 집의 수를 counting한다.

```
def house_counting(graph, x, y) -> bool:
    # 범위를 벗어나면
    if x <= -1 or y <= -1 or x >= N or y >= N:
        return False
    
    # 집이 아니면
    if graph[x][y] == 0:
        return False
    
    # 집이면
    global house_cnt
    house_cnt += 1
    
    graph[x][y] = 0
    house_counting(graph, x-1, y)
    house_counting(graph, x+1, y)
    house_counting(graph, x, y-1)
    house_counting(graph, x, y+1)
    return True
```
---

2중 반복문으로 지도의 모든 점을 확인한다. 
```
# 단지의 수
complex_cnt = 0
# 단지 내 집의 수
house_cnt = 0
house = []

for i in range(N):
    for j in range(N):
        if house_counting(graph, i, j):
            house.append(house_cnt)
            house_cnt = 0
            complex_cnt += 1
            
print(complex_cnt)
house.sort()
for num in house:
    print(num)
```
---

### 결과 및 한줄평
---
