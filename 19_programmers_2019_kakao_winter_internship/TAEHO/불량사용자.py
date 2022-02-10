from itertools import permutations
answer = []
back_list = []
def check(u_id,b_id):
    for i in range(len(u_id)):
        if len(u_id[i]) == len(b_id[i]):
            for j in range(len(u_id[i])):
                if u_id[i][j] != b_id[i][j] and b_id[i][j] !="*":
                    return False
        else:
            return False
    return True

def backtracking(user_id,banned_id,depth):
    global back_list,answer
    if depth == len(banned_id):
        if check(back_list,banned_id) and set(back_list) not in answer:
            answer.append(set(back_list))
            
        return 
    
    for user in user_id:
        if user not in back_list:
            back_list.append(user)
            backtracking(user_id,banned_id,depth+1)
            back_list.pop()
            
def solution(user_id, banned_id):
    
    # perm_id = list(permutations(user_id,len(banned_id)))
    # for perm in perm_id:
    #     if check(perm,banned_id):
    #         perm = set(perm)
    #         if perm not in answer:
    #             print(perm)
    #             answer.append(perm)
    
    backtracking(user_id,banned_id,0)
    
    return len(answer)