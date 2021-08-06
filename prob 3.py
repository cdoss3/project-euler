# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:52:47 2021

@author: Christopher

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

factors = []

"""def largestprime(n):
    # Get the largest prime factor of a number
    b = 1
    while b <= n // 2:
        # add factors of n to the list
        if n % b == 0:
            factors.append(b)
            b += 1
        else:
            b += 1
    for num in factors:
        # remove non-prime factors
        bigprime = 0
        for i in range(2, num // 2):
            if (num % i) == 0:
                break
            else:
                bigprime = num
    print(factors)
    print(bigprime)
    
    """
    
def getfactors(n):
    """Find all factors of n"""
    for k in range(n // 30, n // 2 + 1):
        k = 2 * k + 1
        if n % k == 0:
            factors.append(k)
        else:
            pass
    print(factors)
    
    
def isprime(n):
    """Check whether number is prime. Return true/false."""
    primelist = []
    for k in range(1, n // 2):
        if n % k == 0:
            pass
        else:
            primelist.append(k)
    if primelist == []:
        return True
    else:
        return False