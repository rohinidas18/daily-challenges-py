# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:20:46 2021

@author: Rohini
"""

# Nullify Bits
# For a given integer, odd_bit_value is defined as the number of bits which are '1' in odd position and 
# even_bit_value is defined as the number of bits which are '1' in even position. Nullification is a 
# process in which the 1's in odd position are made as zero if odd_bit_value is lesser than 
# even_bit_value and it makes 1's in even position as zeros otherwise.

# In this process, number of bits to be considered for this process is equal to the minimum number of 
# bits required to represent the number. The right most bit of the number is considered to at poistion 1. 
# For example, if n is 12 - 1100, it becomes 4 and 15 becomes 5.

# Given an integer, write a C++ program to print the number after nullification.

# Input Format
# First line contains number, n

# Output Format
# Print the number after nullification

# ___________________________________________________________________________________________________


def decimalToBinary(n):
    return bin(n).replace("0b", "")
    
def binaryToDecimal(n):
    return int(n,2)

n = int(input())
bn = decimalToBinary(n)

f = str(bn)
k = len(f)

odd_bit_value=0
for i in range(k):
    if i%2!=0 and f[i]=='1':
            odd_bit_value +=1

even_bit_value=0            
for j in range(k):
    if j%2==0 and f[j]=='1':
            even_bit_value +=1
    
g = list(f)

if odd_bit_value < even_bit_value:
    for ii in range(k):
        if ii%2!=0 and f[ii]=='1':
            g[ii]="0"
else:
    for jj in range(k):
        if jj%2==0 and f[jj]=='1':
            g[jj] = "0"

t="".join(g)
t = binaryToDecimal(t)
print(t)
