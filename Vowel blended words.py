# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:07:47 2020

@author: Rohini
"""

# Vowel Based Blended Words
# In English, blend words are words which are formed by combining two English words. 
# Vowel based blended words are one which are formed by joining the part of the first word 
# before a vowel in it and part of the second word starting from the same vowel as in first 
# word.
# For example, spork is a vowel based blending word formed from spoon and fork as shown 
# below: spoon + fork – spork
# When more than one vowel is present in the words, consider the first occurrence of the 
# vowels. Given two words, write a code to form the vowel based blended word from them 
# Input Format
# First line contains the first word, w1
# Next line contains the second word, w2

# Output Format
# Print the vowel based blended words formed


# w1 = str(input())
# w2 = str(input())

# vow = ["a", "e", "i", "o", "u"]
# invalid = False
# W1 = w1.lower()
# W2 = w2.lower()
# word = ""

# for i in w1:
#     if i not in vow and invalid == False:
#         word = word + i
#     if i in vow:
#         invalid = True


# for x in w2:
#     if x in vow:
#         y = w2.index(x)
#         word = word + w2[int(y):]
#         break

# print(word)


import re
a = input()
b = input()

n1 = re.split('a|e|i|o|u', a)
# print(n1)
n11 = n1.pop(0)
# print(n11)

n111 = str(n11)
n2 =[]

for i in b:
    n2.append(i)

# print(n2)
l = ["a", "e", "i", "o", "u"]

for x in n2:
    if x in l:
        u = n2.index(x)
        t  = "".join(n2[u:])
        break

# print(t)
newword = str(n11) + str(t)
print(newword)









