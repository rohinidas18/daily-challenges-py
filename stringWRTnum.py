# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 00:11:43 2020

@author: Rohini
"""

# String generation using W-function
# Using an N-function, every letter of English alphabet (either upper case or lower case) can be 
# represented as a number that corresponds to its position in the English alphabet. For example, 
# ‘A’ is represented by 1, ‘z’ by 26. This is written as N(A)=1, N(a)=1. In the same way, using a 
# W-function, a number k in the range, from 1 to 26 (both included) , is represented by the symbol 
# whose positional index in the English alphabet, is k. This is written as W(25)=y.
# From an integer n, two strings W1 and W2 may be generated in such a way that every character ‘c’ 
# in W1 or W2, taken in order, is equal to W(k)=c where k is a single digit for generating W1 and 
# it is a two digit number for generating W2, that occurs in order in the given integer ‘n’. When 
# the two digit number, k is greater than 26 take the letter corresponding to modulus 26 of k.

# Given an integer ‘n’ which does not have any zero as its digits, write an algorithm and the 
# pseudocode to generate the two strings that can be formed from the number n using W-function.
# Print both the words in lower case letters

# For example, if n = 1234 then words are generated from n as follows.
# 1-2-3- 4 generates abcd
# 12-23-34 generates lwh
# When n= 491
# 4-9-1 generates dia
# 49-91 – generates wm

# Input format :
# First line contains a number, n

# Output format
# Print W1 in first line
# Print W2 in second line


n = int(input())
num = str(n)
nml = list(num)

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

w1 = ""
for i in nml:
    in1 = nums.index(int(i))
    w1 = w1 + alpha[in1]

print(w1)

u = 0
w2 = ""
for x in range(1, len(num)):
    no = ""
    for y in nml[u:u+2]:
        no = no + y
    if int(no) > 26:
        non = (int(no))%26
        in2 = nums.index(int(non))
        w2 = w2 + alpha[in2]
        u = u + 1
    else:
        in2 = nums.index(int(no))
        w2 = w2 + alpha[in2]
        u = u + 1
        
print(w2)
