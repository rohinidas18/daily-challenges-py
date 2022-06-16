# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:55:32 2020

@author: Rohini
"""
# Image Transformation
# Digital images are represented as a matrix and each element in the matrix represents the RGB 
# value of a pixel. Given the pixel values of a nXn image. Write a code to transform the image 
# into another image by alternate swap of edge pixels. That is for example, given a 4 X 4 image 
# as follows:

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# The edge elements of the above image are 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9 and 5. 
# The following steps are involved in the transformation:

# 1 and 3 are swapped
# 1 and 8 are swapped
# 1 and 16 are swapped
# 1 and 14 are swapped
# 1 and 9 are swapped

# After doing alternate swap of edge elements the pixel values of the image looks as follows:
# 3 2 8 4
# 5 6 7 16
# 1 10 11 12
# 13 9 15 14

# And given an image of dimension 5 X 5 as follows:

# 2 4 5 6 3
# 3 11 12 7 9
# 7 15 13 8 1
# 2 21 25 13 14
# 17 10 16 19 3

# Should transform as:

# 5 4 3 6 1
# 3 11 12 7 9
# 2 15 13 8 3
# 2 21 25 13 14
# 7 10 17 19 16

# Input Format
# First line contains the dimension of the matrix, n
# Next nxn lines contain the elements of the matrix in row major order. That is the elements 
# in the first row are given followed by second row and so on

# Output Format
# Print the transformed nxn matrix in ‘n’ lines
# Each line contains the elements of a row separated by a tab.

# *******************************************************************************************


n = int(input())
el = []
for i in range(1, n*n + 1):
    e = int(input())
    el.append(e)         ## to create a list of all number in the og matrix
c = n*2 + (n-2)*2
#print(el)

bel = []
for i in el[0:n]:
    bel.append(i)
for f in range(2, n):
    var1 = el[(n*f)-1]
    bel.append(var1)        ## to create a list 'bel' having all the border elements
for x in range(1, n+1):
    var2 = el[(n*n)-x]
    bel.append(var2)
for y in range(2, n):
    var3 = el[n*(n-y)]
    bel.append(var3)
#print(bel)

sbl = []
for h in range(0, c):
    if h == 0:
        sbl.append(bel[h+2])
    elif h%2 == 0 and h < (len(bel)-2):
        sbl.append(bel[h+2])
    elif h%2 != 0:              ## to create a list of the swapped border elements
        sbl.append(bel[h])
    elif h == (len(bel)-2):
        sbl.append(bel[0])
#print("sbl: ", sbl)    

mel = []
for de in sbl[0:n]:
    mel.append(de)
for df in range(1, n-1):
    mel.append(sbl[-df])         ## to create a list of combined elements from sbl and el 
    for dg in range(1, n-1):                ##in order to form the final matrix
        mel.append(el[n*df+dg])
    mel.append(sbl[n-1+df])
v = 0
for dj in range(1, n+1):
    mel.append(sbl[(-(n-1)-v)])
    v = v + 1
#print(mel)

for p in range(0, n):
    for q in range(0, n):                  ##print the matrix
        t = q + n*p
        print(mel[t], end = "\t")
    print()




    