def solution(n, works):
    if sum(works) <= n:
        return 0
        
    works.sort(reverse=True)
    
    x = 0
    while n > 0:
        
        if x < len(works) - 1 and works[x] == works[x + 1]:
            x += 1
        else:
            group_size = x + 1
            
            if n >= group_size:
                for i in range(group_size):
                    works[i] -= 1
                n -= group_size
            else:

                for i in range(n):
                    works[i] -= 1
                break
                
    return sum(t**2 for t in works)