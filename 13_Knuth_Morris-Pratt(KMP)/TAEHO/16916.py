from sys import stdin

def make_table(p):
    j = 0
    for i in range(1,len(p)):
        while j>0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            table[i] = j+1
            j += 1

def kmp(s,p):
    j= 0 
    for i in range(len(s)):
        while j>0 and s[i] != p[j]:
            j = table[j-1]

        if s[i] == p[j]:
            if j == len(p)-1:
                print(1)
                return
            else:
                j += 1
    print(0)

s = stdin.readline().rstrip()
p = stdin.readline().rstrip()
table = [0]*len(p)
make_table(p)
kmp(s,p)