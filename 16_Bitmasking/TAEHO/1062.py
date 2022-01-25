from sys import stdin
from itertools import combinations
max_count = 0
alpha = {'b': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'j': 6,
         'k': 7, 'l': 8, 'm': 9, 'o': 10, 'p': 11, 'q': 12, 'r': 13,
         's': 14, 'u': 15, 'v': 16, 'w': 17, 'x': 18, 'y': 19, 'z': 20}

n,k = map(int,stdin.readline().split())
words = []
student = 0

for _ in range(n):
    word = set(stdin.readline().rstrip()[4:-4]).difference('a','c','i','n','t')
    words.append(word)

if k<5:
    print(0)
elif k==26:
    print(n)
else:
    bitmap = [2**i for i in range(21)]
    for comb in combinations(bitmap,k-5):
        comb_sum = sum(comb)
        count = 0
        for word in words:
            for w in word:
                if comb_sum & 1<<alpha[w] == 0:
                    break
            else:
                count+=1
        max_count = max(max_count,count)
    print(max_count)