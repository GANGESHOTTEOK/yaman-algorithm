
## [Z](https://www.acmicpc.net/problem/1074)
---

### 문제 설명
- $2^N X 2^N$인 2차원 배열을 Z모양으로 탐색
![문제예시](https://upload.acmicpc.net/adc7cfae-e84d-4d5c-af8e-ee011f8fff8f/-/preview/)

#### 입력
- 정수 N(1<=N<=15) : 숫자 카드의 개수
- 정수 r, c(0<=r,c<= $2^N$) : 구해야할 순서의 정보(r행 c열)
#### 출력
- r행 c열을 몇 번째로 방문했는지 출력
---

### 문제 접근
- $2^nX2^n$인 2차원 배열을 4분할 할 때, 분할된 각 행렬의 가장 첫번째 칸의 인덱스와 방문 순서는 n,분할면의 위치, 첫번째 분할면의 첫칸의 방문 순서로 나타낼 수 있다.

---

### 문제 풀이
``` Python
import sys

def Zsearch(n,i,j,start,seq):
    if n==0:
        return seq
    m = 2**(n-1)
    start = (i//m)*2+j//m
    seq = 4*seq+start
    return Zsearch(n-1, i%m, j%m, start, seq)
    
N, r, c = map(int, sys.stdin.readline().split())
print(Zsearch(N,r,c,0,0))
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148625808-7c8a06ae-2622-4cea-9df7-77387f66f2e7.png)](https://www.acmicpc.net/source/37235634)

---