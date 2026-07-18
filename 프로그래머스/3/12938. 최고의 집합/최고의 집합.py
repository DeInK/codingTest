def solution(n, s):

    if n > s:
        return [-1]
    
    avg = s // n
    mok = s % n
    
    answer = [avg] * n
    

    for i in range(1, mok + 1):
        answer[-i] += 1
        
    return answer