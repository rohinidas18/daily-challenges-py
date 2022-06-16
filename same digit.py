# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:15:06 2020

@author: Rohini
"""

# Digit Same Positions
# Given two numbers n1 and n2, write a code to print the positions in which the digits are same. If none of the digits of the numbers are same then print ‘No digits are same’. Position of the number 128654 is as follows:

# Positions: For example, if n1 is 14287 and n2 is 24787 the digits are same at, 1’s, 
# 10th and 1000th positions. So print
# Same at 1's position
# Same at 10th position
# Same at 1000th position
    

n1 = int(input())
n2 = int(input())

no = str(n1)
nt = str(n2)
h = len(no)
x = h
invalid = True

for i in range(1, (len(no) + 1)):
    if no[(x - 1):x] == nt[(x - 1):x]:
        pos = 10**(h - x)
        if pos == 1:
            print("Same at {}'s position".format(pos))
        else:
            print("Same at {}th position".format(pos))
        invalid = False
    x = x - 1
 
if invalid == True:
       print("No digits are same")