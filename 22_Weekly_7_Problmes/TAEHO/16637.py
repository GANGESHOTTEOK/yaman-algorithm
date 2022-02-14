from sys import stdin,maxsize
import re


def cal():
    operand = re.findall("[0-9]",expr)
    operator = re.findall("[*+-]",expr)
    count = 0
    for idx in bracket:
        idx -= count
        operand[idx] = str(eval(operand[idx] + operator[idx] + operand[idx+1]))
        operand.pop(idx+1)
        operator.pop(idx)
        count += 1

    for i in range(len(operator)):
        operand[i+1] = str(eval(operand[i] + operator[i] + operand[i+1]))
    return int(operand[-1])

def BT(idx, length):
    global max_num
    if idx > length-1:
        return
    
    max_num = max(max_num, cal())
    for i in range(idx,length):
        bracket.append(i+2)
        BT(i+2,length)
        bracket.pop()

n = int(stdin.readline())
expr = stdin.readline().rstrip()
length = len(expr)//2
bracket = []
max_num = cal()

for i in range(length):
    bracket.append(i)
    BT(i,length)
    bracket.pop()

print(max_num if length != 0 else int(expr[0]))
