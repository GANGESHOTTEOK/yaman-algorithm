def solution(msg):
    answer = []
    word_dict = dict()
    for i in range(26):
        word_dict[chr(ord('A') + i)] = i+1
    
    word,idx = 0,1
    
    while idx<=len(msg):
        try:
            test = word_dict[msg[word:idx]]
            text = msg[word:idx]
            
        except:
            word_dict[msg[word:idx]] = len(word_dict) + 1
            answer.append(word_dict[text])
            idx-=1
            word = idx
        idx += 1
    answer.append(word_dict[msg[word:idx]])
    return answer