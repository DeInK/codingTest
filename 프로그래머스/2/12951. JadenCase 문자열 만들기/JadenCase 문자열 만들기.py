def solution(s):
    answer = ''
    result = []
    
    array = s.split(' ')
    
    for x in array :
        if not x:
            result.append("")
            result.append(" ")
            continue
            
        temp = list(x)
        temp[0] = temp[0].upper()
        result.append(temp[0])
        
        for y in range(1, len(temp)):
            temp[y] = temp[y].lower()
            result.append(temp[y])  
        result.append(" ")
        
    if result:
        result.pop()
    
    answer = ''.join(result)
    return answer