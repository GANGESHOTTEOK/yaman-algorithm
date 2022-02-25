def convert(num,n):
    temp = "0123456789ABCDEF"
    q,r = divmod(num,n)
    return convert(q,n)+temp[r] if q else temp[r]

def solution(n, t, m, p):
    numbers = ''
    for i in range(t*m):
        numbers += convert(i,n)
    
    
    return numbers[p-1:t*m:m]