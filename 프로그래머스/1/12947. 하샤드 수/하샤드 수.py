def solution(x):
    answer = False
     
    original_x = x
    y = 0
    

    while x > 0:
        y += x % 10
        x //= 10
        
    if original_x % y == 0:
        answer = True
        
    return answer