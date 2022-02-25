import re

def solution(files):
    answer = []
    element = []
    for file in files:
        HEAD = re.match('[A-Za-z\-\s\.]+', file).span()
        NUMBER = re.match('[0-9]+', file[HEAD[1]:]).span()
        TAIL = file[HEAD[1]+NUMBER[1]:]
        NUMBER = (int)(file[HEAD[1]:HEAD[1]+NUMBER[1]])
        HEAD = file[:HEAD[1]].upper()
        element.append((HEAD, NUMBER, TAIL))
    answer = [i for _, i in sorted(zip(element, files), key = lambda x : x[0][:2])]
    return answer
