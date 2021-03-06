# Breast-First Search (BFS, 너비 우선 탐색)

## BFS의 개념
- 시작 정점을 방문한 후 시작 정점에 인접한 모든 정점들을 우선 방문하는 방법
- 그래프의 **맹목적 탐색** 기법 중 하나이다.

![](https://blog.kakaocdn.net/dn/bLMK90/btqKrJ9aUXI/hvWf1krFJb6R0WlIKx1Vk0/img.gif)
## BFS의 특징
- **Queue**를 이용하여 구현한다.
- 특정 노드에 대한 **방문 여부**를 저장해야한다.
- 주로 두 노드 사이의 최단 경로를 찾고 싶을 때(단순검색) 사용
### 장점
- 단순 검색속도가 DFS보다 빠르다.
- 너비를 우선 탐색하기에 답이 되는 경로가 여러개인 경우에도 최단 길이 경로를 보장한다.
### 단점
- 재귀호출의 DFS와는 달리 큐에 탐색할 정점들을 저장해야 하므로 **많은 저장 공간**을 필요로 하게 된다.
- 노드의 수가 늘어나면 탐색해야하는 노드 또한 많아지기에 비현실적이다.
### 사용 예시
- 그래프의 **모든 정점을 방문**하는 것이 주요한 문제
- **최단거리** 구해야 하는 문제
    - 깊이 우선 탐색으로 경로를 검색할 경우 처음으로 발견되는 해답이 최단거리가 아닐 수 있지만, 너비 우선 탐색으로 현재 노드에서 가까운 곳부터 찾기 때문에 경로를 탐색 시 먼저 찾아지는 해답이 곧 최단거리기 때문입니다.
- 검색대상의 규모가 크지 않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않은 문제
### 시간 복잡도
- 정점의 수: N, 간선의 수: E
    - 인접 리스트 : O(N+E)
    - 인접 행렬 : O(N^2)
## BFS의 구현
``` Python
def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
```