def solution(s):
    answer = []

    array = s.split(' ')
    
    for x in array:
        temp = list(x)

        for y in range(len(temp)):

            if y % 2 == 0:
                temp[y] = temp[y].upper()
            else:
                temp[y] = temp[y].lower()
                
        
        answer.append("".join(temp))
        
    return " ".join(answer)