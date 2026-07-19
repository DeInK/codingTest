def solution(n, words):
    
    history = [words[0]]
    
    for i in range(1, len(words)):
        curr = words[i]
        prev = words[i - 1]
        
        if curr[0] != prev[-1] or curr in history:
            return [(i % n) + 1, (i // n) + 1]
        
        history.append(curr)
        
    return [0, 0]