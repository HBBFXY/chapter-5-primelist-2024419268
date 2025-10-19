def primelist(N):
    if N <= 2:
        return ""
    
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  
    
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i*i : N : i] = [False] * len(is_prime[i*i : N : i])
    primes = [str(i) for i, prime in enumerate(is_prime) if prime]    
    return ' '.join(primes)



    
