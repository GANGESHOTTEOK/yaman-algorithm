# Divide and Conquer(분할 정복)

## Binary Search
- 그대로 해결할 수 없는 문제를 **작은 문제로 분할(Divide)**하여 **문제를 해결(Conquer)**하는 방법이나 알고리즘
- 해를 구할 수 있을 만큼 충분히 더 작은 사례로 나누어 해결하는 방법
- **재귀호출**을 사용하여 구현된다.
- 처음부터 큰 문제를 방문 후 작은 문제를 호출하는 **top-down** 접근 방법
- 서로 **상관관계가 없는 문제**를 해결하는데 적합(쪼개진 문제들간의 내용이 서로 연관이 없다는 것)
### 장점
- 문제를 나눔으로써 어려운 문제를 해결할 수 있다.
- 분할 정복이 그대로 사용되는 효율적인 알고리즘들이 많다.
- 문제를 나누어 해결한다는 특징상 병렬적으로 문제를 해결
### 단점
- 재귀적 함수 호출로 인한 오버헤드가 발생
- 스택에 다양한 데이터를 보관하고 있어야하므로 스택 오버플로우가 발생하거나 과도한 메모리 사용된다.

## 분할정복법의 설계전략
1. Divide : 문제가 분할이 가능할 경우, 2개 이상의 문제로 나눈다.
1. Conquer : 각각의 문제들을 해결한다.
1. Combine : 해결한 문제들을 병합하여 상위의 문제를 해결한다.

## 응용 문제
- [Binary Search](https://github.com/GANGESHOTTEOK/yaman-algorithm/blob/master/04_BinarySearch/AN/README.md)
- Merge / Quick Sort
- Matrix Multiplication
- Fibonacci Sequence