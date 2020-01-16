# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:48:06 2020

@author: Adesiji
"""

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
