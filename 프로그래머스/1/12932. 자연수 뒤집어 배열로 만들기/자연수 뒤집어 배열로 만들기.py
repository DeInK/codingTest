def solution(n):

    if n == 0:
        return [0]
    
    answer = []
    
    while n>0 :
        answer.append(n%10)
        n//=10
        
    return answer