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
