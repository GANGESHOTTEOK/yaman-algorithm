def solution(str1, str2):
    answer = 0
    complement = 0
    union = 0
    str1 = str1.upper()
    str2 = str2.upper()
    list1,list2 = [], []
    
    list1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]            
            
    if list1 == [] and list2 == []:
        return 65536
    
    union = len(list1)+len(list2)
    
    if len(list1) >= len(list2):
        for element in list2:
            if element in list1:
                complement += 1
                list1.remove(element)
    else:
        for element in list1:
            if element in list2:
                complement += 1
                list2.remove(element)
                
    union -= complement
    
    if union == 0:
        return 65536
    
    answer = complement / union
    
    return int(answer*65536)