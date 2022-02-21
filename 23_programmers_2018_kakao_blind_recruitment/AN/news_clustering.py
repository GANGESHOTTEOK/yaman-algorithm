from collections import defaultdict
import math

def jacard(A,B):
    if not (A or B):
        return 1
    intersection = sum([min(Acnt,Bcnt) for b,Bcnt in B.items() for a,Acnt in A.items() if a==b])
    union = sum(A.values())+sum(B.values())-intersection
    return intersection/union

def getSubSet(string):
    subSet = defaultdict(int)
    for i in range(len(string)-1):
        if string[i:i+2].isalpha():
            subSet[string[i:i+2]] += 1
    return subSet

def solution(str1, str2):
    str1,str2 = str1.upper(),str2.upper()
    A = getSubSet(str1)
    B = getSubSet(str2)
    answer = math.trunc(jacard(A,B)*65536)
    return answer