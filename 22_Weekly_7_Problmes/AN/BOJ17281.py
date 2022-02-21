import sys
from itertools import permutations
input = sys.stdin.readline

# get score with line_up
def play(line_up):
    score = turn = 0
    line_up.insert(3,0)         # fourth hitter is fixed

    for inning in innings:
        out = 0   # out count
        runners = []   # runners' result in this inning

        while out<3:
            hitter = line_up[turn]
            if not inning[hitter]:  # if result is 0
                out += 1            # out count increase
            else:                   # if result is not 0
                runners.append(inning[hitter])  # add runners
            turn = (turn+1)%9       # next hitter
        
        # find rest of runners on base, cannot get score
        base = 0
        for i in range(len(runners)-1,len(runners)-4,-1):
            if i < 0:    # out of range
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

for line_up in permutations(players):    # make line-up
    max_result = max(max_result, play(list(line_up)))

print(max_result)