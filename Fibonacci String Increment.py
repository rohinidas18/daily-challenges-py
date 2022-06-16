# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:56:19 2020

@author: Rohini
"""

# Fibanocci Increment Mixed String
# Increment mixed string is an operation which operates on two strings S1 and S2 of same length to 
# generate a new string S3. The letters in odd position of S3 is one more than the corressponding 
# letter in S1 and the letters in even position of S3 is one more than the corressponding letter in 
# S2. For example, if S1 = ‘amey’ and S2 = ‘dhft’ then S3 = ‘bifu’. For letter ‘z’, letter ‘a’ is 
# one more than it.

# Fibanocci increment mixed string is operation which operates on the last two strings in the series. 
# Given two strings, S1 and S2 write a code to generate the nth element using Fibanocci increment 
# mixed string operation. The given strings S1 and S2 are the first two elements in the Fibanocci 
# increment mixed string series. Third element in the series is found by applying increment mixed 
# string operation for first two elements.
 

# If S1 = ‘amey’ and S2 = ‘dhft’ then the first five elements in the series are as follows:
# amey
# dhft
# bifu
# ejgv
# ckgw

# Input Format
# First line contains the string S1
# Next line contains the string S2
# Next line contains the value of n

# Output Format
# Print the nth element in the Fibanocci increment mixed string series


S1 = str(input())
s1 = list(S1)

S2 = str(input())
s2 = list(S2)

L = []
L.append(S1)
L.append(S2)

n = int(input())
alpha1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha = alpha1 + alpha1

for s in range(1, n-1):
    S = ""
    for i in range(0, len(S1)):
        if i%2 != 0:
            g = alpha.index(s2[i]) + 1
            S = S + alpha[g]
        elif i%2 == 0:
            h = alpha.index(s1[i]) + 1
            S = S + alpha[h]
    L.append(S)
    s1 = list(L[s])
    s2 = list(L[s+1])

print(S)