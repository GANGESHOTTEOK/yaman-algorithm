from queue import Queue

def fillQueue(M, N, idx):
    q = Queue()
    for m in range(M):
        if(b[M-1-m][idx] == 'X'): continue
        q.put((M-1-m, idx))
    return q
    
def check(q1, q2):
	s = set()
	if q1.qsize() == 0 or q2.qsize() == 0:
		return s
	block = [[q1.get(),q2.get()],['','']]
    
	while q1.qsize() and q2.qsize():
		block[1][0], block[1][1] = block[0][0], block[0][1]
		block[0][0], block[0][1] = q1.get(), q2.get()
		if b[block[0][0][0]][block[0][0][1]] == b[block[0][1][0]][block[0][1][1]] == b[block[1][0][0]][block[1][0][1]] == b[block[1][1][0]][block[1][1][1]]:
			s.add(block[0][0])
			s.add(block[0][1])
			s.add(block[1][0])
			s.add(block[1][1])
	return s
    
def solution(m, n, board):
	answer = 0
	global b
	b = board
	while True:
		s = set()
		for j in range(n-1):
			s = s | check(fillQueue(m,n,j), fillQueue(m,n,j+1))
		if not bool(s):
			break
		answer += len(s)
		for y,x in s:
			b[y] = b[y][:x]+'X'+b[y][x+1:]
    
	return answer
