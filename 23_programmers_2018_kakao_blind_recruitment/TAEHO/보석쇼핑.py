def solution(gems):
    end = 0
    n = len(gems)
    kind_gem = len(set(gems))
    dict_gem = {}
    min_length = [0,n-1]
    for start in range(n):
        while len(dict_gem) != kind_gem and end < n :
            if dict_gem.get(gems[end]):
                dict_gem[gems[end]] += 1
            else:
                dict_gem[gems[end]] = 1
            end += 1
        
        if len(dict_gem) == kind_gem:
            if (end-1) - start < min_length[1] - min_length[0]:
                min_length[0],min_length[1] = start, end-1
                
            if dict_gem[gems[start]] == 1:
                del dict_gem[gems[start]]
            else:
                dict_gem[gems[start]] -= 1
        
    return [min_length[0]+1,min_length[1]+1]