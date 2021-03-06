# Divide & Conquer 분할 정복

### 분할 정복이란?
---
- 분할정복법이란 주어진 문제를 작은 사례로 나누고 각각의 작은 문제들을 해결하여 정복하는 방법
- 문제의 사례를 여러개의 더 작은 사례로 나누어 생각하고, 해결가능 할 만큼 작은 경우 해결한다
- 큰 문제로 부터 작은 문제로 내려가는 Top-down 방식의 접근 방법

### 분할 정복 설계 전략
---
1. 문제 사례를 하나 이상의 작은 사례로 분할한다.
2. 나눈 문제가 해결될 수 있을 때 까지 더 작은 사례로 나눈다.
3. 작은 사례를 정복하고 탈출한다.
4. 필요하다면 작은 사례의 해답을 통해 큰 사례의 해답을 구한다.

### 활용 예
--- 
- 이분 탐색
- 상한 하한 찾기
- 병합 정렬
- 퀵 정렬
- 최대 값 찾기
- 쉬트라센 행렬 곱셈 등


### 장점과 단점
---
- 장점
  - 문제를 분할 함으로써 어려운 문제를 해결할 수 있다.
- 단점
  - 함수를 재귀적으로 호출함으로 오버헤드가 발생하고, 스택오버플로우의 위험 존재
