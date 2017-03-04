def prime_seive(n):
    start = range(n)
    for i1 in start:
        if i1 > 1:
            for i2 in range(i1*2,n,i1):
                start[i2] = 0
    return [i for i in start if i > 1]
