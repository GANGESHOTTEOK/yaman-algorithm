from collections import defaultdict

def solution(msg):
    answer = []
    
    # init dictionary : include word with length 1.
    dic = defaultdict(int)
    for i in range(26):
        dic[chr(ord('A')+i)] = i+1
        
    index = 27      # indexing
    while msg:
        
        if dic[msg] != 0:               # if rest of msg exist in dictionary
            answer.append(dic[msg])   
            break
        
        for c in range(1,len(msg)):     # find the most lenght word in dictionary
            if dic[msg[:c+1]] == 0:     # if check 0~c word is not in dictionary
                break                   # break: index 'c' is next input
        
        dic[msg[:c+1]] = index          # msg 0~c update dictionary
        answer.append(dic[msg[:c]])     # add the most length word to output
        msg = msg[c:]                   # msg cut
        index += 1
        
    return answer