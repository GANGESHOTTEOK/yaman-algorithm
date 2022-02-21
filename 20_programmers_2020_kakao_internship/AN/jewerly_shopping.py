from collections import defaultdict
def solution(gems):
    answer = []
    min_len = len(gems)+1
    kind = defaultdict(int)
    kindCount = len(set(gems))
    start = end = cur_count = 0
    while end < len(gems):
        if kind[gems[end]] == 0:
            cur_count += 1
        kind[gems[end]] += 1
        end += 1
        if cur_count == kindCount:
            while start < end:
                if kind[gems[start]] > 1:
                    kind[gems[start]] -= 1
                    start += 1
                elif end-start < min_len:
                    min_len = end-start
                    answer = [start+1,end]
                    break
                else:
                    break
        
    return answer