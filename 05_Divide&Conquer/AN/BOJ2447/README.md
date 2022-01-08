
## [별 찍기 - 10](https://www.acmicpc.net/problem/2447)
---

### 문제 설명
- 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양
- 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴
- N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태

#### 입력
- 정수 N(3<=N<=$3^8$) : 줄 수
#### 출력
- 첫째 줄부터 N번째 줄까지 별을 출력
---

### 문제 접근
- 
---

### 문제 풀이
- 
``` Python
import sys

N = int(sys.stdin.readline())
stars = [[' ' for i in range(N)] for j in range(N)]

def getStar(n,r,c):
    if n==1:
        stars[r][c] = '*'
        return
    m = n//3
    getStar(m,r,c)
    getStar(m,r+m,c)
    getStar(m,r+2*m,c)
    getStar(m,r,c+m)
    getStar(m,r+2*m,c+m)
    getStar(m,r,c+2*m)
    getStar(m,r+m,c+2*m)
    getStar(m,r+2*m,c+2*m)
        
getStar(N,0,0)

for a in stars:
    for b in a:
        print(b,end='')
    print()
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148641595-7ffe4b60-f532-46a2-a7b8-a84291f75f58.png)](https://www.acmicpc.net/source/37257654)

- 시간초 줄이기
``` Python
import sys

def getStar(n):
    if n == 1:
        return ['*']
    
    divN = n//3
    stars = getStar(divN)
    result=[]
    
    for i in stars:
        result.append(i*3)
    for i in stars:
        result.append(i+' '*(divN)+i)
    for i in stars:
        result.append(i*3)
    return result

n=int(sys.stdin.readline().strip())
print('\n'.join(getStar(n)))
```
[![image](https://user-images.githubusercontent.com/54929223/148641595-7ffe4b60-f532-46a2-a7b8-a84291f75f58.png)](https://www.acmicpc.net/source/37258165)


---