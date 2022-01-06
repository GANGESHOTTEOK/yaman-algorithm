
## [로프](https://www.acmicpc.net/problem/2217)
---

### 문제 설명
- 각각의 로프를 이용하여 서로 다른 무개의 물체를 들어올릴 수 있다.
- k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

#### 입력
- 정수 N(1<=N<=100,000) : 로프의 수
- N개의 W(1<=W<=10,000) : 각 로프가 버틸 수 있는 최대 중량

#### 출력
- 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 출력
---

### 문제 접근
- `weights`를 내림차순으로 정렬한다.
- 한 로프가 감당해야할 무게는 무게들의 평균과 같다. 
- 내림차순으로 정렬된 배열에서 0번째부터 i번째까지의 평균을 구하면 그 평균은 i번째 원소보다 무조건 크다.
- 따라서 정렬된 `weights`에서 `weight[0]`부터 `weight[i]`까지 사용할 때 들어올릴 수 있는 물체의 최대 중량은 `weight[i]*(i+1)`과 같다.
---

### 문제 풀이
``` Python
import sys

N = int(sys.stdin.readline())
weights = []
for i in range(N):
    weights.append(int(sys.stdin.readline()))

weights.sort(reverse=True)

for i in range(N):
    weights[i] = weights[i]*(i+1)
    
print(max(weights))
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148313155-e549b277-c3fa-44a2-af5a-bbae8a489a4b.png)](https://www.acmicpc.net/source/37136827)

---