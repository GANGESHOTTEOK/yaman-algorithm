# Two-Pointers

## Two-Pointers 알고리즘이란
- 1차원 배열에서 다른 원소를 가리키는 2개의 포인터를 조작하며 원하는 것을 얻는 알고리즘
- 1차원 배열의 부분배열에 관한 알고리즘

## Two-Pointers의 구현
- 서로 다른 원소를 가리키는 두 포인터로 선택된 부분배열의 시작과 끝의 인덱스를 `start`, `end`
    - `start=end=0` 시작하며 항상 `start<=end`임을 만족
    - 정확히는 부분배열은 배열의 `[start,end)`이다. `start`의 원소는 포함하고 `end`는 포함하지 않는다.
- 주어진 조건, 구해야하는 것에 따라 `start`와 `end`를 적절히 증가시켜가며 해를 구한다.
## 시간 복잡도
- N개의 원소를 가지는 배열일 때 : `O(N)`
## 관련 예제
### [수들의 합 2](https://www.acmicpc.net/problem/2003)

``` Python
import sys

input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))

start = end = part_sum = count = 0

while True:
    if part_sum >= M:
        part_sum -= A[start]
        start += 1
    elif end==N:
        break
    else:
        part_sum += A[end]
        end += 1
    if part_sum == M:
        count += 1
    
print(count)
```
### [부분합](https://www.acmicpc.net/problem/1806)
``` Python
import sys

input = sys.stdin.readline

N,S = map(int, input().split())
seq = list(map(int,input().split()))

start=end=part_sum=0
min_len = sys.maxsize

while True:
    if part_sum >= S:
        part_sum -= seq[start]
        start += 1
    elif end == N:
        break
    else:
        part_sum += seq[end]
        end += 1
    if part_sum >= S:
        min_len = min(min_len, end-start)
        
print(min_len if min_len != sys.maxsize else 0)
```
