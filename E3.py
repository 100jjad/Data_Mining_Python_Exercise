# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:29:47 2020

@author: 100jjad
"""
#3. Write a Python program to count the occurrences of each word in a given sentence
#..........Sajjad Soheyli.........Exercise....03...........
s = input("Ente a Sentence : ")
list_of_word=s.split(" ")
print(list_of_word)

for i in range(0 , len(list_of_word)):
    num = 0
    for j in range(0 , len(list_of_word)):
        if list_of_word[i]==list_of_word[j]:
            num+=1      
    if (list_of_word[i] in list_of_word[:i]) != True:
        print(str(list_of_word[i])+" : "+str(num))