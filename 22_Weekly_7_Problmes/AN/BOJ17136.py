import sys
input = sys.stdin.readline

# size : paper's size (size x size)
# r,c : start index (r,c)
# curMap : current Map
# is curMap's (r,c) covered with size paper
def isCovered(curMap,r,c,size):
    for row in range(r,r+size):
        for col in range(c,c+size):
            if not(0<=row<10 and 0<=col<10):
                return False
            if not curMap[row][col]:
                return False
    return True

# depth : dfs's depth (in this program, mean count of paper)
# curMap : current Map
# find min count of paper with dfs
def dfs(curMap, depth):
    global min_result
    
    isFind=0
    for i in range(10):          # find 1 in curMap
        for j in range(10):
            if curMap[i][j]:     # if it's 1
                r,c = i,j        # store index
                isFind=1         # change flag
                break
        if isFind:
            break
    
    if not isFind:                            # if there's not any 1
        min_result = min(min_result,depth)    # get min value
        return                                # end of dfs
    
    # search proper size from big one to small one
    for k in range(5,0,-1):     # k is size
        if paperCnt[k]==5:      # if k paper is all used
            continue            # skip
        if not isCovered(curMap,r,c,k): # if it is not covered with k paper
            continue                    # skip
        # if k paper can cover, create new map(temp) whose covered range is 0
        temp = [[0 if r<=i<r+k and c<=j<c+k else curMap[i][j] for j in range(10)] for i in range(10)]
        paperCnt[k] += 1
        dfs(temp,depth+1)
        paperCnt[k] -= 1
    return

# input
board = []
for _ in range(10):
    board.append(list(map(int,input().split())))

paperCnt = [0]*6
min_result = 26
dfs(board,0)

# output
print(min_result if min_result<26 else -1)