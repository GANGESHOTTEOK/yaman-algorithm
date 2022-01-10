from sys import stdin
vowel = ['a','e','i','o','u']

def backtracking(cnt,idx,vowel_count,consonant_count):
    if cnt == l:
        if vowel_count >= 1 and consonant_count >= 2:
            print("".join(back_list))
        return 

    for i in range(cnt, cnt+c-l+1):
        if i>idx:
            back_list[cnt] = alpha[i]
            idx = i
            if alpha[i] in vowel:
                backtracking(cnt+1,idx,vowel_count+1,consonant_count)
            else:
                backtracking(cnt+1,idx,vowel_count,consonant_count+1)



l,c = map(int,stdin.readline().split())
back_list = [' ']*l
alpha = stdin.readline().split()
alpha.sort()

backtracking(0,-1,0,0)