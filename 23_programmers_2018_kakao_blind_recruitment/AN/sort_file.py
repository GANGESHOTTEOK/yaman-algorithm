def solution(files):
    
    separated = []
    
    for index,file in enumerate(files):
        
        for i in range(len(file)):
            if file[i].isdigit():
                HEAD = file[:i].upper()
                break
            
        for j in range(i,len(file)):
            if j==len(file)-1 and file[j].isdigit():
                NUMBER = int(file[i:])
                break
    
            if not file[j].isdigit():
                NUMBER = int(file[i:j])
                break
        
        separated.append((index,HEAD,NUMBER))
    
    separated.sort(key=lambda x:(x[1],x[2],x[0]))
    
    answer = [files[file[0]] for file in separated]
    
    return answer