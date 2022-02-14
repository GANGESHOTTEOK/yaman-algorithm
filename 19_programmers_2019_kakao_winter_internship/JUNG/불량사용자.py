import itertools

def is_matched(name, ban_name):
    for i in range(len(name)):
        if ban_name[i] == "*":
            continue
        if ban_name[i] != name[i]:
            return False
    return True

def check(names, banned_id):
    for i in range(len(names)):
        if len(names[i]) != len(banned_id[i]):
            return False
        if is_matched(names[i], banned_id[i]) == False:
            return False
    return True

def solution(user_id, banned_id):
    answer = []

    # names = ('frodo', 'fradi')
    for names in list(itertools.permutations(user_id, len(banned_id))):
        if check(names, banned_id) == True:
            names = set(names)
            if names not in answer:
                answer.append(names)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))