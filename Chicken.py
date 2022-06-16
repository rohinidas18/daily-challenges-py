# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:45:41 2020

@author: Rohini
"""

n = int(input())
m = int(input())

nomore = 1

if n < m:
    print("No way")
else:
    for x in range(1, n):
        h = n - m
        for i in range(1, h + 1):
            g = h - i
            if i%2 != 0 and i > m and i < g:
                print(m, i, g)
                nomore = 0
            else:
                yes = 0
        m = m + 2

if yes == 0:
    if nomore == 0:
        pass
    else:
        print("No way")
    
    