# Greedy (탐욕 알고리즘)

## Greedy의 개념
- 현재 상황에서 가장 좋은 것을 선택하는 알고리즘이다.
- 모든 문제나 상황에서 이를 이용하여 최적해를 도출할 수 있는 것은 아니다.
- 경우의 수를 모두 검토하기 위해 점화식을 통해 구성되는 동적 프로그래밍(Dynamic Programming) 사용 시 지나치게 많은 일을 한다는 것에서 착안하여 고안된 알고리즘이다.

## Greedy 알고리즘의 조건
1. 탐욕스런 선택 조건(greedy choice property)
    - 탐욕적 선택은 항상 **안전하다**는 것을 보여야 한다. 즉, 탐욕적 선택으로 전체 문제의 **최적해를 반드시 구할 수 있다는 것**을 보여야 한다.
1. 최적 부분 구조 조건(optimal substructure)
    - 문제에 대한 최종 해결 방법이 **부분 문제**에 대해서도 또한 최적의 해결 방법이다는 조건.
- 위의 두 조건을 만족하지 않더라도 Greedy는 **근사 알고리즘**(Approximation Algorithm)으로 사용이 가능하다. 최적해를 보장하진 않지만 계속 속도가 빠르기 때문에 실용적으로 사용이 가능하다. 

## DP(동적 프로그래밍)과의 비교
- Local Optimal이 Global Optimal이 되란 법은 없다. 따라서 DP는 모든 경우의 수를 계산하여 최적해를 도출한다.
- Greedy는 항상 최적해를 보장하지는 않지만 모든 경우의 수를 따지지 않고 Local Optimal을 찾아 계산 속도가 빠르고 근사 알고리즘으로 사용가능하다.
- 즉, Greedy는 DP와 최적 부분 구조 조건을 충족한다는 공통점이 있고,
- DP는 시간 복잡도가 높고, Greedy는 결과에 대한 신뢰도가 비교적 낮다.
## Greedy를 활용하는 대표적인 문제
- 활동 선택 문제
- 분할 가능한 배낭 문제

## 참고
- https://ko.wikipedia.org/wiki/%ED%83%90%EC%9A%95_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
- https://rain-bow.tistory.com/entry/DP%EC%99%80-Greedy-Algorithm
- https://velog.io/@contea95/%ED%83%90%EC%9A%95%EB%B2%95%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98