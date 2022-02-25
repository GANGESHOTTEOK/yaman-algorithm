import re
import sys
input = sys.stdin.readline

def calculate(ops):
    rand = [i for i in operands]
    rator = [(val,1) if i in ops else (val,0) for i,val in enumerate(operators)] # (operator,priority) 1 if priority else 0
    
    # operate priority
    prio = idx = 0
    while idx<len(rator) and prio<len(ops):
        if rator[idx][1] == 1:
            rand[idx] = str(eval(rand[idx]+rator[idx][0]+rand[idx+1]))
            rand.pop(idx+1)
            rator.pop(idx)
            prio += 1
            continue
        idx += 1
        
    # operate not priority
    while rator:
        rand[0] = str(eval(rand[0]+rator[0][0]+rand[1]))
        rand.pop(1)
        rator.pop(0)
        
    return int(rand[0])

def comb(k, depth, ops):
    global max_result
    if k == depth:
        max_result = max(max_result, calculate(ops))
        return
    
    i = ops[-1]+2 if ops else 0
    while i < len(operators):
        if visited[i]==1:
            continue
        visited[i]=1
        ops.append(i)
        comb(k,depth+1,ops)
        ops.pop()
        visited[i]=0
        i += 1

# input    
N = int(input())
exp = input().rstrip()

operands = list(map(str,re.split('[*+-]',exp)))
operators = re.split('[0-9]+',exp)[1:-1]
visited = [0]*len(operators)
max_result = calculate([])

for cnt in range(1,len(operands)//2+1):
    comb(cnt,0,[])
    
# output
print(max_result)