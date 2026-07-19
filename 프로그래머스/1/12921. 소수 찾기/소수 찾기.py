def solution(n):

    is_prime = [True] * (n + 1)
    

    is_prime[0] = False
    is_prime[1] = False
    

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:

            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    prime_count = 0
    for is_p in is_prime:
        if is_p:
            prime_count += 1
            
    return prime_count