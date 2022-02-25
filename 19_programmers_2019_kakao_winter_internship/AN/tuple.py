from collections import defaultdict
def solution(s):
    count = defaultdict(int)
    digit = 0
    for i in range(1,len(s)-1):
        if s[i] == ',':
            count[digit] += 1
            digit = 0
        elif s[i].isdigit():
            digit = digit*10+int(s[i])
    count[digit] += 1
            
    leng = len(count.keys())
    answer = [0]*leng
    for key, value in count.items():
        answer[leng-value] = key
    return answer