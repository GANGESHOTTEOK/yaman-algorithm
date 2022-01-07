
## [숫자 카드](https://www.acmicpc.net/problem/10815)
---

### 문제 설명
- 숫자 카드는 정수 하나가 적혀져 있는 카드
- 숫자 카드 N개를 가지고 있을 때, 정수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하라.

#### 입력
- 정수 N(1<=N<=500,000) : 숫자 카드의 개수
- N개의 정수 x(-10,000,000<=x<=10,000,000) : 숫자 카드에 적혀있는 정수
- 정수 M(1<=M<=500,000) : 판별해야할 숫자 카드의 개수
- M개의 정수 y(-10,000,000<=x<=10,000,000) : 판별해야할 카드
#### 출력
- 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력
---

### 문제 접근
1. 이분탐색을 이용한다.
1. set함수를 이용한다.
---

### 문제 풀이
- 이분탐색(Binary Search) 이용
``` Python
import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

card.sort()

for k in target:
    left = 0
    right = len(card)-1
    flag = 0
    while left <= right:
        mid = (left+right)//2
        if card[mid] == k:
            flag = 1
            break
        elif card[mid] < k:
            left = mid+1
        else:
            right = mid-1
    print(flag, end=' ')
```
- set함수 이용
``` Python
import sys

N = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for k in target:
    if k in card:
        print('1', end=' ')
    else:
        print('0', end=' ')
```
---

### 결과 및 한줄평
- Binary Search를 이용한 결과
[![image](https://user-images.githubusercontent.com/54929223/148474181-e5213c7e-84fd-4c12-bab4-d1ec6efb9ae0.png)](https://www.acmicpc.net/source/37188970)
- set함수를 이용한 결과
[![image](https://user-images.githubusercontent.com/54929223/148474267-4c2aead4-dad2-48eb-abf6-8d37f117001f.png)](https://www.acmicpc.net/source/37189099)
- set함수를 이용하는게 훨씬 빠르다
- 한 원소를 검색하는데 있어 Binary Search는 `O(log N)`이 걸리지만 set함수의 경우 `O(1)`이 걸리기 때문이다.

---