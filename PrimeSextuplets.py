#!/usr/bin/env 
#coding=utf-8

#We are interested in collecting the sets of six prime numbers, that having a starting prime p, the following values are also primes forming the sextuplet[p, p + 4, p + 6, p + 10, p + 12, p + 16]

#质数数列
def prime_seive(n):
    start = range(n)
    for i1 in start:
        if i1 > 1:
            for i2 in range(i1*2,n,i1):
                start[i2] = 0
    return [i for i in start if i > 0]

#缓存
prime = prime_seive(7000000)

#找到满足[p, p + 4, p + 6, p + 10, p + 12, p + 16]且和大于sum_limit的数列
def find_primes_sextuplet(sum_limit):
    for i in range(len(prime)):
        l = prime[i:i+6]
        p = l[0]
        if l == [p, p + 4, p + 6, p + 10, p + 12, p + 16] and sum(l)>sum_limit:
            return l
    return None
# print find_primes_sextuplet(28713551)
# print find_primes_sextuplet(18785302)
# print find_primes_sextuplet(23702719)