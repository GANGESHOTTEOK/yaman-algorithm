def solution(user_id, banned_id):
    answer = 1
    ban_list = [[] for _ in range(len(banned_id))]
    checked = [0]*len(user_id)
    for banID, ban in enumerate(banned_id):
        for userID, user in enumerate(user_id):
            if len(user) != len(ban):
                continue
            for i in range(len(ban)):
                if ban[i] == "*":
                    continue
                if ban[i] != user[i]:
                    break
            if i == len(ban)-1:
                ban_list[banID].append(userID)
    print(ban_list)
    
    return answer