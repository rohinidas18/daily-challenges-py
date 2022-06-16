# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:55:12 2020

@author: Rohini
"""
# Complete n-Digit Factor
# A number is said to be a complete ‘n’ digit factor, if it is a factor of all ‘n’ digit numbers 
# when concatenated (joined to right) to itself.
# For example, 7 is a complete 3-digit factor as it divides all three digit numbers from 100 to 
# 999 when concatenated to itself (i.e. 100100, 101101,102102, ... ..., 998998, 999999).
# Given the value of n and m, write a code to generate all numbers from 2 to m (both inclusive) 
# that are complete n-digit factor and print ‘No complete factors’ otherwise.
# For example, if n is 3 and m is 15 then print 7, 11, 13 and if n is 3 and m is then print 
# ‘No complete factors’

# Boundary Conditions: 2<n<9

# Input Format
# First line contain the number of digits, n
# Next line contains the maximum value of m that has to be checked for Complete n-Digit Factor

# Output Format
# Print each Complete n-Digit Factor in one line and print No complete factors otherwise



# n = int(input())
# m = int(input())
# num = str(n)

# l = 10**(n-1)
# # print(l)
# u = 10**(n) - 1
# # print(u)
# fac = []

# 
# for x in range(2, m+1):
#     invalid = True
#     # print("x", x)
#     for i in range(l, u + 1):
#         # print("i", i)
#         h = str(i) + str(i)
#         f = int(h)
#         if f%x == 0:
#             # print(h)
#             continue
#         elif f%x != 0:
#             # print(0)
#             # print(f, x)
#             invalid = False
#     print(x, invalid)
            
#     if invalid == True:
#         print(x)
#         fac.append(x)

# print(fac)

# for y in fac:
#     print(y)


n = int(input())
m = int(input())
num = str(n)

l = 10**(n-1)
u = 10**(n) - 1
fac = []

if n>2 and n<9:
    for x in range(2, m+1):
        invalid = True
        for i in range(l, u + 1):
            h = str(i) + str(i)
            f = int(h)
            if f%x != 0:
                invalid = False
            
        if invalid == True:
            fac.append(x)
            print(x)
if len(fac) == 0:
    print("No complete factors")