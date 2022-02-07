from collections import Counter
def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = '[' + s + ']'
    s = eval(s)
    answer = list(map(lambda x : x[0],Counter(s).most_common()))
    return answer
