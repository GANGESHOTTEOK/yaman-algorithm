def solution(s):
    answer = []
    s = s.replace("{","[")
    s = s.replace("}","]")
    s = eval(s)
    
    s = sorted(s, key= lambda x:len(x))
    
    for i in range(len(s)):
        if len(s[i]) == 1:
            answer.append(s[i][0])
        else:
            for element in s[i]:
                if element not in answer:
                    answer.append(element)
            
    return answer