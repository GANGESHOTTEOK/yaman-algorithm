from sys import stdin

back_list = [0]*6

def backtracking(cnt,idx):
    global length
    if cnt == 6:
        print(' '.join(map(str,back_list)))
        return

    for i in range(cnt,cnt+length-5):
        if i > idx:
            back_list[cnt] = lotto[i]
            idx = i
            backtracking(cnt+1,idx)


while True:
    lotto = list(map(int, stdin.readline().split()))
    if lotto[0] == 0:
        break
    length = lotto[0]
    lotto = lotto[1:]
    backtracking(0,-1)
    print()
