from itertools import combinations

def get_substring(string : str):
    for i in combinations(string, len(string) - 1):
        yield ''.join(i)

dp = dict()
def func(string: str, substring : set):
    if len(string) == 1:
        substring.add(string)
        return

    substring.add(string)
    for s in get_substring(string):
        substring.add(s)
        func(s, substring)

s1 = input()
s2 = input()
subset_s1, subset_s2 = set(), set()

func(s1, subset_s1)
func(s2, subset_s2)

print(max(list(map(len, subset_s1 & subset_s2))))
