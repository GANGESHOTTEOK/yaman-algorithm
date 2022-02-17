from sys import stdin
from itertools import permutations

def game(member):
    idx = 0
    score = 0
    for inning in innings:
        out = 0
        base = [0,0,0]
        while out <3:
            if inning[member[idx]] == 0:
                out += 1
            elif inning[member[idx]] == 1:
                score += base[2]
                base = [1,base[0],base[1]]
            elif inning[member[idx]] == 2:
                score += base[1] + base[2]
                base = [0,1,base[0]]
            elif inning[member[idx]] == 3:
                score += base[0] + base[1] + base[2]
                base = [0,0,1]
            else:
                score += 1 + base[0] + base[1] + base[2]
                base = [0,0,0]
            idx = (idx+1)%9
    return score

n = int(stdin.readline())
innings = [list(map(int,stdin.readline().split())) for _ in range(n)]
m = [1,2,3,4,5,6,7,8]
member_list = permutations(m,8)
ans = 0
for member in member_list:
    member = list(member)
    member.insert(3,0)
    ans = max(ans,game(member))
print(ans)