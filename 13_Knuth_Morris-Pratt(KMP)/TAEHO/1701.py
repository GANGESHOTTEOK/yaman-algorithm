from sys import stdin

answer = 0
text= stdin.readline().rstrip()
for i in range(len(text)):

    sub_text = text[i:]
    table = [0]*len(sub_text)
    j = 0
    for k in range(1,len(sub_text)):
        while j>0 and sub_text[j] != sub_text[k]:
            j = table[j-1]
        
        if sub_text[k] == sub_text[j]:
            table[k] = j+1
            j += 1

    answer = max(answer, max(table))

print(answer)