import re

def solution(files):
    
    separated = []
    for index,file in enumerate(files):
        HEAD = re.search('[^0-9]+',file).group().upper()
        NUMBER = int(re.search('[0-9]+',file).group())
        separated.append((index,HEAD,NUMBER))
        
    separated.sort(key=lambda x:(x[1],x[2],x[0]))
    
    answer = [files[file[0]] for file in separated]
    
    return answer