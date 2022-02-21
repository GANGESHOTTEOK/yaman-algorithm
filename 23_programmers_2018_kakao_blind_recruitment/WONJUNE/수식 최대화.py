def solution(expression):
    answer = 0
    prior = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    operators = ['*', '+', '-']
    num_split = expression
    num_split = num_split.replace('+', ' ').replace('-', ' ').replace('*', ' ').split(' ')
    
    operator = [op for op in expression if not op.isdecimal()]
    
    for p in prior:
        nums = num_split
        op = operator
        
        for i in range(3):
            stack_num = []
            stack_op = []
            
            stack_num.append(nums[0])
            
            for j, o in enumerate(op):
                stack_num.append(nums[j+1])
                stack_op.append(o)
                
                if stack_op[-1] == operators[p[i]]:
                    num1 = stack_num.pop(-1)
                    num2 = stack_num.pop(-1)
                    o = stack_op.pop(-1)
                    
                    stack_num.append((str)(eval(num2+o+num1)))
            nums = stack_num
            op = stack_op
            
        answer = max(answer, abs((int)(nums[0])))
    
    return answer
