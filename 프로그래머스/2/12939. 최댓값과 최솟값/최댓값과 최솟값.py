def solution(s):
    array = list(map(int, s.split()))
    
    max = None
    min = None
    
    for x in array:

        if max is None or max < x:
            max = x

        if min is None or min > x:
            min = x
    answer = f"{min} {max}"
    
    return answer