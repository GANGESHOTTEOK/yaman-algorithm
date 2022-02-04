def solution(s):
    arr = []
    answer = [] # 정답 리스트

    # 주어진 문자열의 앞뒤 중괄호 2개 제거
    # 문자열 "},{" 기준으로 나누어서 리스트 생성
    s = s[2 : -2].split("},{")
    # 각 원소를 "," 기준으로 나누어서 리스트 생성한 후 집합으로 만들어서 arr 리스트에 추가
    for ele in s:
        arr.append(set(ele.split(",")))
    # 원소 개수를 기준으로 오름차순 정렬
    arr.sort(key= lambda x : len(x))

    result = set()
    for ele_set in arr: # arr 리스트 원소 ele_set은 set
        temp_set = ele_set - result
        answer.append(tuple(temp_set)[0]) # temp_set을 튜플로 만들어서 인덱싱으로 값을 지정한 다음 answer에 추가
        result = result | temp_set # result와 temp_set을 합집합

    # 원소들 모두 정수로 변환
    answer = [int(i) for i in answer]
    return answer