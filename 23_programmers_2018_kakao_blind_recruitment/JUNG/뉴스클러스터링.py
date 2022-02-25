def solution(str1, str2):
    # 다중 집합 구하기
    set1, set2 = [], []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i].lower() + str1[i+1].lower())

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set2.append(str2[i].lower() + str2[i+1].lower())

    # 다중 집합의 교집합과 합집합
    union = set1.copy()
    union_temp = set1.copy()
    for e in set2:
        if e not in union_temp:
            union.append(e)
        else:
            union_temp.remove(e)

    inter = []
    for e in set2:
        if e in set1:
            set1.remove(e)
            inter.append(e)


    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
