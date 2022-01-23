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
    return max(pi)

S = sys.stdin.readline().rstrip()

sub_len = 0
for i in range(len(S)):
    sub_len = max(sub_len, getPi(S[i:]))
    
print(sub_len)