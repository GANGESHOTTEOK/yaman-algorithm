from sys import stdin
from collections import defaultdict

n,d,k,c = map(int,stdin.readline().split())
foods = []
dict_food = defaultdict(int)
left,right = 0,0
result = 0
for _ in range(n):
    food = int(stdin.readline())
    foods.append(food)

dict_food[c] += 1
while right < k:
    dict_food[foods[right]] += 1
    right +=1

while left < n:
    result = max(result,len(dict_food))
    dict_food[foods[left]] -= 1
    dict_food[foods[right]] += 1
    if dict_food[foods[left]] == 0:
        del dict_food[foods[left]]
    left += 1
    right = (right+1) % n
print(result)