import re
from collections import defaultdict

def token(string):
    d = defaultdict(int)
    for s in range(len(string)-1):
        if(string[s:s+2].isalpha()):
            d[string[s:s+2].upper()] += 1
    return d

def jarcard(d1, d2):
    intersection = d1.keys() & d2.keys()
    intersection_num = 0
    for i in intersection:
        intersection_num += min(d1[i], d2[i])
        
    union = d1.keys() | d2.keys()
    union_num = 0
    for u in union:
        union_num += max(d1[u], d2[u])
    if(union_num == 0): return 65536
    return (int)(intersection_num / union_num * 65536)

def solution(str1, str2):
    dict1, dict2 = token(str1), token(str2)

    return jarcard(dict1, dict2)
