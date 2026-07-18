
def solution(s, n):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = []
    
    for char in s:
        
        if char == " ":
            answer.append(" ")
            continue
            
        idx = alphabet.index(char)
        
        if idx < 26:
            new_idx = (idx + n) % 26
            
        else:
            new_idx = (idx - 26 + n) % 26 + 26
            
        answer.append(alphabet[new_idx])
        
    return "".join(answer)