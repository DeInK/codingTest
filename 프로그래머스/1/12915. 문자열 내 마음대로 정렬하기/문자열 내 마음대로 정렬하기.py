def solution(strings, n):
    taged_array = []
    
    for word in strings:
        tag = word[n]
        taged_char = tag + word
        taged_array.append(taged_char)
        
    taged_array.sort()
    
    answer = []

    for x in taged_array:

        fixed_char= x[1:]
        answer.append(fixed_char)
        
    return answer