import re
def solution(files):
    first_sort = sorted(files,key=lambda x: int(re.findall(r"\d+",x)[0]))
    answer = sorted(first_sort,key=lambda x: re.findall(r"[a-zA-Z- .]+",x)[0].lower())
    return answer