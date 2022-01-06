
## [신입 사원](https://www.acmicpc.net/problem/1946)
---

### 문제 설명
- 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다.
- 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
- 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

#### 입력
- 정수 N(1<=T<=20) : 테스트 케이스의 수
- 정수 N(1<=N<=100,000) : 지원자 숫자
- N개의 서로 다른 `first`와 `second` : 지원자의 서류심사 성적, 면접 성적의 순위
#### 출력
- 각 테스트 케이스에 대해서 선발할 수 있는 신입사원의 최대 인원수
---

### 문제 접근
- 서류 성적을 기준으로 `info`를 오름차순으로 정렬한다. 
- 정렬된 `info`의 뒤의 원소는 앞의 원소보다 무조건 서류 성적 등수가 낮다. 
- 따라서 선발이 되기 위해서는 면접 등수가 앞에 있는 모든 원소들의 등수보다 높아야 한다.
---

### 문제 풀이
``` Python
import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    info = []
    for j in range(N):
        first, second = map(int, sys.stdin.readline().split())
        info.append((first,second))
    
    info.sort()
    
    count = 0
    highest = info[0][1]                # 가장 높은 등수 저장
    
    for grades in info:
        if grades[1] <= highest:        # 가장 높은 등수와 비교 더 높으면
            count += 1
            highest = grades[1]
    
    print(count)
```
---

### 결과 및 한줄평
[![image](https://user-images.githubusercontent.com/54929223/148310535-3f4bcb40-df2c-4db6-a799-cd2558fdcfcd.png)](https://www.acmicpc.net/source/37135730)
- 메모리와 소요 시간이 좀 큰듯하나 같은 문제의 다른 사람들 결과랑 비교하면 괜찮은 것 같기도...  
![image](https://user-images.githubusercontent.com/54929223/148310481-aef1af14-db28-47d6-b0b4-d1d464a3d269.png)


---