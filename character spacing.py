# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:45:30 2020

@author: Rohini
"""
# Same Letter Distances
# Same letter distance is the number of characters between two consecutive occurrances of the same 
# character. Given a string, write a code to find the letter that has most frequently occurred in it. 
# And also find same letter distance between the occurrances of the most frequently occurred character. 
# If distance is zero then print ‘No characters’, if distance is 1 then print ‘1 character’ and if 
# distance is ‘d’, greater than 1 then print ‘d characters’.
# For example, if the string is ‘accomodation’, the most frequently occurred character is ‘o’ and the 
# same letter distances are
# 1 character
# 4 characters

# If the string is ‘bookkeeper’, the most frequently occurred character is ‘e’ and the same letter 
# distances are
# No characters
# 1 character
# If more than one character occurs maximum number of times then consider the first character in the 
# string.
# Input Format
# First line contains the string, w
# Output Format
# Print the letter that has occurred most frequently, ch
# Print the same letter distance for consecutive occurrences of ch in next few lines


w = str(input())
l = list(w)
counts = dict()

print(l)

for x in l:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

# print(counts)

u = list(counts)
print(u)

k = []

for key in counts.values():
    # print(key)
    k.append(key)
    
# print(k)

g = max(k)
i = k.index(g)
p = u[i] 
print(p)

a = []   
s = 0
for j in l:
    if j not in 
    if  in l:
    counter = 0
    elem_pos = []
    for n in l:
        if n == h:
            elem_pos.append(counter)
        counter = counter + 1
    print(elem_pos)
    
#         chrc = u[e]
#         for y in w:
#             if y == chrc:
#                 upp = w.index(y)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            