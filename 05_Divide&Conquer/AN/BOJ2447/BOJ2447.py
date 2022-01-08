import sys

def getStar(n):
    if n == 1:
        return ['*']
    
    divN = n//3
    stars = getStar(divN)
    result=[]
    
    for i in stars:
        result.append(i*3)
    for i in stars:
        result.append(i+' '*(divN)+i)
    for i in stars:
        result.append(i*3)
    return result

n=int(sys.stdin.readline().strip())
print('\n'.join(getStar(n)))