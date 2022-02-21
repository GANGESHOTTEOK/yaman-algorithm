import sys
input = sys.stdin.readline

def attack(arch,enem):
    count = 0
    row = N
    while enem:                                 # 적이 없어질 때 까지
        attacked = set()
        for col in arch:                        # 궁수별 공격
            isAttack = 0
            for dist in range(1,D+1):           # 거리별 공격
                for dc in range(-dist+1,dist):
                    dr = dist-abs(dc)
                    r,c = row-dr,col+dc
                    if not(0<=r<N and 0<=c<M):
                        continue
                    if (r,c) in enem:
                        isAttack=1
                        attacked.add((r,c))
                        break
                if isAttack==1:
                    break
        count += len(attacked)
        enem = [(i+1,j) for i,j in enem if i+1<N and (i,j) not in attacked]
    return count

def locateArcher(depth):
    global max_result
    if depth==3:
        max_result = max(max_result,attack(archers,enemies))
        return
    k = archers[-1]+1 if archers else 0
    for i in range(k,M):
        archers.append(i)
        locateArcher(depth+1)
        archers.pop()
    return
    
# input
N,M,D = map(int,input().split())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
enemies = [(i,j) for j in range(M) for i in range(N) if board[i][j]]

archers=[]
max_result = 0

locateArcher(0)
print(max_result)