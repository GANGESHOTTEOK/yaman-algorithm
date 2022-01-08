# Binary Search(이분 탐색법)

## Binary Search
- 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법이다.
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
- `O(log N)`의 시간복잡도를 가진다.

## Binary Search의 과정
- 정렬되어있는 `list`, 찾고자하는 값 `target`, 탐색 범위의 시작 값`left`, 끝 값 `right`
1. 중간 값을 `left`와 `right`를 이용하여 구해준다. : `mid = (left+right)//2`
1. `mid`와 `target`을 비교한다.
    - `mid`가 `target`보다 클 경우 `left`를 `mid+1`로 만들어준다.
    - `mid`가 `target`보다 작을 경우 `right`를 `mid-1`로 만들어준다.
- 위 과정을 `left <= right` 를 만족하는 동안 반복한다.

![Binary Search의 과정](https://t1.daumcdn.net/cfile/tistory/221D4A3F5705041A1F "Binary Search의 과정")

## 구현 코드
- 반복문
``` Python
def BinarySearch(list, target):
    list.sort()
    left, right, isExist = 0, len(list)-1, 0
    while left <= right:
        mid = (left+right)//2
        if mid == target:
            isExist = 1
        elif mid <= target:
            left = mid+1
        else:
            right = mid-1
    return isExist
``` 

- 재귀
```Python
def BinarySearch(list, left, right, target):
    if left > right:
        return 0
    mid = (left+right)//2
    if mid == target:
        return 1
    elif mid <= target:
        BinarySearch(list, mid+1, right, target)
    else:
        BinarySearch(list, left, mid-1, target)
```