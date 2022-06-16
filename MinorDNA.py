# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 08:43:43 2020

@author: Rohini
"""

# Minor DNAs
# Deoxyribonucleic acid (DNA) is a molecule composed of two chains that coil around each other and carry genetic instructions 
# used in the growth, development, functioning and reproduction of all living organisms. The DNA is composed of simpler units 
# called nucleotides. Each nucleotide is composed of one of four nitrogen-containing nucleobases cytosine [C], guanine [G], 
# adenine [A] or thymine [T]. There are specific rules by which a DNA is formed with these four nucleobases. 
# Example DNAs are: ccag, actaatagtacccataaacctgcta

# Many research is being carried out based on the occurrences of the nucleotides in a DNA.

# Here a minor DNA ‘d1’ of length ‘k’ can be obtained from a given DNA ‘d’ of length ‘n’ by deleting ‘n-k’ nucleotides in ‘d’. 
# For example, if the given DNA ‘d’ of length four is ‘ccag’ then all the possible minor DNAs of length three are four minor DNAs:

# Remove last letter - cca
# Remove third letter - ccg
# Remove second letter - cag
# Remove first letter – cag

# Minor DNAs of length 4 of a DNA ctctac which is of length 6 are:
# ctct, ctca, ctta, ccta, ctcc, cttc, cctc, ctac, ccac, ctac, tcta, tctc, tcac, ttac and ctac.

# Given a DNA of length ‘n’ and a length ‘k’ of minor DNAs required, write a code to generate all possible minor DNAs of length ‘k’ and print them in ascending order.

# Input Format

# First line contains the DNA, d
# Next line contains the length of the minor DNAs required, k

# Output Format

# Print all minor DNAs of length ‘k’ in ascending order
# Print one minor DNA in one line


d = str(input())
k = int(input())

n = len(d)
md = []
ir = 0

if n-k == 1:
    for i in range(0, n):    
        f = d[i]
        t = d.replace(f, "", 1)
        md.append(t)
elif n-k > 1:
    for s in range(1, n+1):
        for j in range(0, n-s):
            W = ""
            L = list(d)
            # print(L)
            Z = []
            for i in range(0, len(d)):
                Z.append(i)
            # print(Z)
            D = {}
            for key in Z:
                D[key] = L[key]
            # print(D)
            del D[ir]
            for zu in range((j+ir+1),(j+ir+n-k)):
                print(zu)
                del D[zu]
            KEy = list(D.keys())
            KEy.sort()
            for y in KEy:
                W = W + D[y]
            md.append(W)
        ir = ir + 1
md.sort()
for q in md:
    print(q)

