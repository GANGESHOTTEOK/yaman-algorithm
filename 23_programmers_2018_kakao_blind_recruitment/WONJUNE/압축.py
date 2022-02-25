def solution(msg):
    answer = []
    idx = 1
    d = dict()
    for c in range(ord('A'),ord('Z')+1):
        d[chr(c)] = idx
        idx+=1
    i = 0
    
    while i < len(msg):
        s = ""
        for j in range(i,len(msg)):
            s += msg[j]
            if not s in d:
                answer.append(d[s[:-1]])
                d[s] = idx
                idx+=1
                i = j-1
                break
            elif j == len(msg)-1:
                answer.append(d[s])
                i = len(msg)
        i+=1
    return answer
