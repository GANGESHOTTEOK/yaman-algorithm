import sys

def Zsearch(n,i,j,start,seq):
    if n==0:
        return seq
    m = 2**(n-1)
    start = (i//m)*2+j//m
    return Zsearch(n-1, i%m, j%m, start, 4*seq+start)
    
N, r, c = map(int, sys.stdin.readline().split())
print(Zsearch(N,r,c,0,0))