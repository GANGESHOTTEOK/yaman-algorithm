import sys

def getPi(string):
    pi = [0]*len(string)
    l = 0
    for i in range(1,len(string)):
        while l>0 and string[l] != string[i]:
            l = pi[l-1]
        if string[l] == string[i]:
            l+=1
            pi[i] = l
    return pi
    
def kmp(s,p):
    pi = getPi(p)
    k=0
    for i in range(len(s)):
        while k>0 and s[i] != p[k]:
            k = pi[k-1]
        if s[i] == p[k]:
            if k == len(p)-1:
                return 1
            else:
                k += 1
    return 0
                
S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
print(kmp(S,P))