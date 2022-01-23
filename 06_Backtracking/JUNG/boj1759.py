L, C = map(int, input().split())
pwd = list(input().split())
pwd.sort()

check_list = []
temp = []
visited = []
def get_check_list(pwd, size, call):
    if len(temp) == size:
        check_list.append(''.join(temp))
        return

    for ch in pwd:
        if ch not in visited and ch >= call:
            visited.append(ch)
            temp.append(ch)
            get_check_list(pwd, size, ch)
            temp.pop()
            visited.remove(ch)

get_check_list(pwd, L, pwd[0])
check_list.sort()

vo_cnt = 0
con_cnt = 0
for word in check_list:
    for ch in word:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            vo_cnt += 1
        else:
            con_cnt += 1

    if vo_cnt >= 1 and con_cnt >= 2:
        print(word)

    vo_cnt = 0
    con_cnt = 0