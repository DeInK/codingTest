def solution(n):
    answer = 0
    for x in range(n+1):
        if x%2==0:
            answer+= x
    return answer