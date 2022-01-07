# Binary Search 이분 탐색

## 개념 정리

### 이분 탐색이란
---
정렬되어 있는 배열에서 특정 테이터를 찾기 위해 모든 데이터를 순차적으로 확인하는 대신 탐색 범위를 절반으로 줄여가며 찾는 방법

순차적으로 차례대로 탐색하는 선형 탐색 O(N)에 비해 이분 탐색은 O(lg N)의 시간 복잡도를 가지기 때문에, N이 커지면 커질 수록 속도의 차이가 발생한다.

### 구현 방법
---
이분 탐색을 할 때 에는 범위를 나타내기 위한 변수 `start`와 `end` 가 필요하다. 

그리고 두 변수가 잡은 범위를 절반으로 줄이기 위해 변수 `middle`에 (`start` + `end`) / 2 의 인덱스를 할당해준다.

그리고 `middle`가 가르키는 값과 타켓의 값을 비교하여 발견하지 못했다면 절반으로 나눈 **오른쪽의 범위**에서 다시 탐색할 것인지, **왼쪽의 범위**에서 탐색 할 것인지를 결정한다.

- 타겟이 더 크다면 `start` = `middle` + 1
- 타겟이 더 크다면 `end` = `middle` - 1

탐색 대상인 배열 안에 타켓 값이 존재하지 않는다면?  
값을 끝까지 찾지 못해서 범위의 시작을 나타내는 변수 `start`가 범위의 끝인 `end`보다 커질 것이다. 
- `start` > `end`

#### 코드 구현
```cpp
bool binarysearch(int target){
  int start = 0, end = n-1, middle;

  while(start <= end) {
    middle = (start+end)/2;

    if(a[middle] < target) 
        start = middle+1; // 오른쪽 범위
    else if(a[middle] > target) 
        end = middle-1; // 왼쪽 범위
    else return true; // 발견
  }
  return false; // start>end일 경우 while문을 탈출
}
```
#### 재귀적으로 구현

```cpp
bool binarySearch(int start, int end) {
    if (start > end) return false; // start>end일 경우 탈출

    int middle = (start + end) / 2;

    if (a[middle] < target) 
        binarySearch(start, middle - 1); // 오른쪽 범위
    else if(a[middle] > target) 
        binarySearch(middle + 1, end); // 왼쪽 범위
    else return true; // 발견
}
```

간단한 이분 탐색이라면 직접 구현하지 않고 STL 함수를 사용 할 수 있음
```cpp
bool target_exist = binary_search(start, end, target);
```

### 주의 사항
---
1. 이분 탐색을 하고자 한다면 주어진 배열은 정렬되어 있어야 한다.
2. 무한 루프에 빠지지 않게 mid 값을 잘 정해야 한다.
3. `binary_search()` 와 같은 함수들을 활용해도 되지만 도움이 되지 않을 때도 있다.

### 이분 탐색의 활용
- 좌표 압축
- parametric search
- 등등