# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n = 0
numlist = []
total = 0

while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        numlist.append(n)
        n = n + 1
    else:
        n = n + 1

for num in numlist:
    total = total + num
    
print(total)