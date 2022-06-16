# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:08:16 2020

@author: Rohini
"""

# Unique Multiplication
# A multiplication is said to be unique when the digits of the multiplicand, multiplier and 
# product are different and digits from 1 to 9 are present in it.

# For example, 4*1963 = 7852 is unique multiplication as all the nine digits from 1 to 9 
# are present in it and the digits in the multiplicand, multiplier and product are different.

# Given the multiplicand and the multiplier, write a code to check if it is a unique 
# multiplication. Print Yes for unique multiplication and No otherwise



n = int(input())
m = int(input())

h = n*m

t = list(str(n))
s = list(str(m))
q = list(str(h))

for i in q:
    if i in t or i in s:
        invalid = True
    else:
        invalid = False

if invalid == False:
    print("Yes")
else:
    print("No")
