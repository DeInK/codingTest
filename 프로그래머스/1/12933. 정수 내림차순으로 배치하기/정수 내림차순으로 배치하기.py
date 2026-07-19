def solution(n):
    answer = 0
    array = []
    
    while n > 0:
        tmp = n % 10
        array.append(tmp)
        n = n // 10
        
    array.sort(reverse=True)   
    
    for num in array:
        answer = (answer * 10) + num
        
    return answer