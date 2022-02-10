from sys import stdin

n = int(stdin.readline())

for i in range(n):
    if i==0:
        DP1 = list(map(int,stdin.readline().split()))   #최대
        DP2 = [dp for dp in DP1] #최소
    else:
        new_DP = list(map(int,stdin.readline().split()))
        temp = [dp for dp in DP1]
        DP1[0] = max(temp[0]+new_DP[0],temp[1]+new_DP[0])
        DP1[1] = max(temp[0]+new_DP[1],temp[1]+new_DP[1],temp[2]+new_DP[1])
        DP1[2] = max(temp[1]+new_DP[2],temp[2]+new_DP[2])
        temp = [dp for dp in DP2]
        DP2[0] = min(temp[0]+new_DP[0],temp[1]+new_DP[0])
        DP2[1] = min(temp[0]+new_DP[1],temp[1]+new_DP[1],temp[2]+new_DP[1])
        DP2[2] = min(temp[1]+new_DP[2],temp[2]+new_DP[2])
        
print(max(DP1),min(DP2))