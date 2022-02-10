import sys
input = sys.stdin.readline
a = ord('a')
mask = 0

def words(depth, k):
    global mask
    count = 0
    if depth == K-5:
        for word in strings:
            if word & mask == word:
                count += 1
        return count
    for i in range(k,26):
        if mask & (1<<i):
            continue
        mask |= 1 << i
        count = max(count, words(depth+1,i+1))
        mask &= ~(1<<i)
    return count
        
N,K = map(int, input().split())
strings = [0]*N
for i in range(N):
    string = input().rstrip()
    for alpha in string:
        strings[i] |= 1 << (ord(alpha)-a)

if K<5:
    print(0)
    exit(0)
    
mask |= 1 << (ord('a')-a)
mask |= 1 << (ord('n')-a)
mask |= 1 << (ord('t')-a)
mask |= 1 << (ord('c')-a)
mask |= 1 << (ord('i')-a)

print(words(0,0))