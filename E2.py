# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:11:45 2020

@author: 100jjad
"""
#2. Write a Python program to remove the characters which have odd index values of a given string
#..........Sajjad Soheyli.........Exercise....02...........


s = input("Enter a String:")
temp=""
for i in range(0 , len(s)):
    if i%2==0:
        temp=temp+s[i]
s=temp
print(s)