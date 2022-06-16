# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 00:34:29 2021

@author: Rohini
"""
# Secret Agent and Code Word
# A secret agent is a government employee whose job involves gathering secret information about 
# the governments of unfriendly foreign countries. A secret agent ‘X’ emailed a sentence ‘S’ with 
# a code word ‘W’ to his head office. Only one word of the sentence 'S' is real and others are fake. 
# The agent ‘X’ also mailed a sentence as a clue - if I tell you any one character ‘C’ of the code 
# word 'W', then you would find exactly two words with ‘C’ in it, those words will have same number 
# of vowels and one of them is ‘W’.

# For example, if the senetence ‘S’ mailed by agent ‘X’ is "AIM DUE OAT TIE MOD", then TIE is the 
# code word. Due to the following reasons:

# Word ‘W’  Letter in word    Words with ‘C’ in it    No. Vowels    Consider/Reject Pair  C/R Word                                                   
#                 (C)

# AIM             A               AIM, OAT               AIM – 2          Consider      
#                                                        OAT – 2

# AIM             I               AIM, TIE               AIM – 2          Consider
#                                                        OAT – 2

# AIM             M               AIM, MOD               AIM – 2           Reject        Reject
#                                                        MOD – 1

# DUE             D               MOD, DUE               DUE – 2           Reject        Reject
#                                                        MOD – 1                         

# OAT             O              OAT, MOD                OAT – 2
#                                                        MOD – 1            Reject      Reject
                                                       
# MOD             M              MOD, AIM               MOD – 1            Reject       Reject
#                                                       AIM – 2             

# TIE            T               OAT, TIE               OAT - 2
#                                                       TIE – 2             Consider

# TIE            I               TIE, AIM               TIE – 2
#                                                       AIM – 2             Consider

# TIE            E               TIE, DUE               TIE – 2
#                                                       DUE – 2              Consider    Consider

# Input Format: First line contains the sentence with codeword

# Output Format: First line should contain the code word

# Boundary Conditions:
# Length of the sentence < 200
# Length of each word in the sentence<10
# Number of words in each sentence <20

#-------------------------------------------------------------------------------------------------

sen = str(input())
sl = sen.split(" ")
vow = ['A', 'E', 'I', 'O', 'U']

vc = {}
wl = {}

for i in sl:
    count = 0
    for j in i:
        if j in vow:
            count += 1
    vc[i] = count
    wl[i] = list(i)

cl = []
firstL = []

for m in sl:
    for n in m:
        for h in sl:
            if m != h and n in list(h):
                firstL.append((m,h))
                if vc[m] == vc[h]:
                    cl.append((m,h))
                    
dl = []

for y in firstL:
    if y not in cl:
        for yy in cl:
            if y[0] == yy[0]:
                dl.append(yy)


for w in dl:
    if w in cl:
        cl.remove(w)

fD = {}
for kk,vv in cl: 
    fD.setdefault(kk, []).append(vv) 


for ii in fD:
    if len(ii) == len(fD[ii]):
        print(ii)