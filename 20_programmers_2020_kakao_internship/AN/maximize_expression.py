import re
def calculator(a,b,oper):
    if oper == '*':
        return a*b
    if oper == '+':
        return a+b
    return a-b

def solution(expression):
    answer = 0
    priorities = [['*','+','-'],['*','-','+'],['+','*','-'],['+','-','*'],['-','*','+'],['-','+','*']]
    
    for priority in priorities:
        operand = list(map(int,re.split('[*+-]',expression)))
        operator = re.split('[0-9]+',expression)
        operator = operator[1:-1]
        print(priority)
        for oper in priority:
            while oper in operator:
                i = operator.index(oper)
                operand[i] = calculator(operand[i],operand[i+1],oper)
                operand.pop(i+1)
                operator.pop(i)
        answer = max(answer, abs(operand[0]))
    return answer