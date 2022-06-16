# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:08:39 2020

@author: Rohini
"""
# Letter Partners Game
# In a fun game, every letter in English alphabet has a partner. The first thirteen letters of the 
# English alphabet are called pre-partners and the next thirteen letters are called post-partners. 
# That is ‘a’ is the pre-partner and the corressponding post-partner is ‘n’, ‘b’ is the pre-partner 
# and the corressponding post partner is ‘o’ ....‘m’ is the pre-partner and ‘z’ is the post-partner.
# In this game, players will be asked to take a lot with a string ‘w’ and they are said to won the 
# game if the following conditions are satisfied by the letters in ‘w’:
# (i) The string may be mixed with pre-partners and post-partners but all pre-partners should have 
# a post-partner
# (ii) A pre-partner should come before it’s corressponding post-partner
# (iii) For a pre-partner that is in position ‘i’ it’s post-partner
# (a) Shall come immediately at posititon ‘i+1’ or (b) Should come before all corressponding 
# post-partners of pre-partners that is in positions < i and after all corressponding post-partners 
# of pre-partners that is in position > i.
# And the player has lost the game otherwise.

# For example, if the word in the lot taken is ‘abon’ then the player has won the game. 
# All pre-partners come before the post-partner and condition (iii) is also satisfied as follows:
# 1) ‘o’ comes immediately after its pre-partner ‘b’, and as per condition (a) of (iii) it is 
# acceptable
# 2) ‘n’ comes after its prepartner ‘a’ and it comes after the post-partners of pre-partners that 
# has come after ‘a’ and as per condition (b) of (iii) it is acceptable
# Whereas if the word in the lot taken is ‘abno’ then the player has lost the game as the 
# post-partener ‘n’ for pre-partner ‘a’ has come before the post-partner of the pre-partner ‘b’, 
# violates condition (iii).

# ***********************************************************************************************

w = str(input())
D = {k: v for (k, v) in zip(['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m'], ['n', 'o','p', 'q','r', 's','t', 'u','v', 'w','x', 'y','z'])}
# print(D)
W = list(w)
invalid = True

d1 = {}
for i in W:
    if i in D.keys():
        d1[i] = W.index(i)
        
# print(d1)

for i in W:
    if i in D.keys():
        if D[i] not in W:
            # print("butter")
            invalid = False
            break

if invalid == True:
    for r in W:
        if r in D.keys():
            # print(r)
            pos1 = W.index(r)
            # print(pos1)
            pos2 = W.index(D.get(r))
            # print(pos2)
            if pos2 == (pos1 + 1):
                invalid = True
            else:
                for y in d1.keys():
                    if d1[y] > d1[r]:
                        if W.index(D[y]) < W.index(D[r]):
                            invalid = True
                        else:
                            invalid = False
                            break

if invalid == True:
    print("Won")
else:
    print("Lost")