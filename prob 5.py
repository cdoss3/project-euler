# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:51:08 2021

@author: Christopher

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def smallestmult(numgrp):
    n = 2520
    matchall = False
    for num in numgrp:
        if n % num != 0:
            

smallestmult(divisors)