import sys
from itertools import permutations
input = sys.stdin.readline

def play(line_up):
    score = turn = 0
    line_up.insert(3,0)
    for inning in innings:
        out = 0
        runners = []
        while out<3:
            hitter = line_up[turn]
            if not inning[hitter]:
                out += 1
            else:
                runners.append(inning[hitter])
            turn = (turn+1)%9
        base = 0
        for i in range(len(runners)-1,len(runners)-4,-1):
            if i < 0:
                break
            base += runners[i]
            if base >= 4:
                break
            runners.pop()
        score += len(runners)
    return score

N = int(input())
innings=[]
for _ in range(N):
    innings.append(list(map(int,input().split())))
    
max_result = 0
players = [1,2,3,4,5,6,7,8]

for line_up in permutations(players):
    max_result = max(max_result, play(list(line_up)))

print(max_result)