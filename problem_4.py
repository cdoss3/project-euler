# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:27:46 2021

@author: Christopher

A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def mult(a, b):
    product = a * b
    return product

for x, y in range(900, 1000):
    