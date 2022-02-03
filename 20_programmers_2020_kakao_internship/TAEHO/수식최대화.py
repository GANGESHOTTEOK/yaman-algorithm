import re
def solution(expression):
    combinations = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    max_num = 0
    for combination in combinations:
        operand = re.split('[*+-]',expression)
        operator = re.split('[0-9]',expression)
        operator = [op for op in operator if op in ["+","-","*"]]
        for comb in combination:
            idx = operator.index(comb) if comb in operator else -1
            while idx != -1:
                operand[idx] = str(eval(operand[idx] + operator[idx] + operand[idx+1]))
                operand.pop(idx+1)
                operator.pop(idx)
                idx = operator.index(comb) if comb in operator else -1
        max_num = max(max_num,abs(int(operand[0])))
    return max_num