
## [예산](https://www.acmicpc.net/problem/2512)
---

### 문제 설명
- 국가는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는데 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
    1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
    1. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 
- 예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 

#### 입력
- 정수 N(3<=N<=10,000) : 지방의 수
- N개의 정수 k(1<=k<=100,000) : 각 지방의 예산요청
- 정수 M(N<=M<=1,000,000,000) : 총 예산
#### 출력
- 배정된 예산들 중 최댓값인 정수
---

### 문제 접근
- 0부터 `budgets`의 최댓값까지를 범위로하여 상한금액을 이분탐색한다.
- 이때, `target`은 총 예산 `M`이 된다.
---

### 문제 풀이
``` Python
import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

budgets.sort()

def getSum(limit):                      # 상한액이 limit일 때 책정된 총 예산을 반환하는 함수
    sum = 0
    for k in budgets:
        if k <= limit:
            sum += k
        else:
            sum += limit
    return sum

left, right, highest = 0, budgets[N-1], 0

while left <= right:                    # 이분탐색 시작
    mid = (left+right)//2
    total = getSum(mid)
    if total <= M:
        highest = mid
        left = mid+1
    else:
        right = mid-1

print(highest)
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148478652-bd4a93d4-5f09-4d44-bac5-38e59af80ad7.png)
](https://www.acmicpc.net/source/37190847)



---