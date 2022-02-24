from collections import deque

def d2n(digit,n):
    if not digit:
        return ['0']
    ret = []
    while digit:
        mod = digit%n
        ret = [str(mod) if mod<10 else chr(ord('A')+mod-10)]+ret
        digit = digit//n
    return ret
    
def solution(n, t, m, p):
    answer = []
    turn = digit = 0
    que = deque()
    while len(answer) < t:
        if not que:
            temp = d2n(digit,n)
            for k in temp:
                que.append(k)
            digit += 1
        if (turn%m)==p-1:
            answer.append(que.popleft())
        else:
            que.popleft()
        turn = (turn+1)%m
    
    return ''.join(k for k in answer)