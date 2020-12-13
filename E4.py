# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:49:00 2020

@author: 100jjad
"""
#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form
#..........Sajjad Soheyli.........Exercise....04...........

s = input("Enter List of Word Separated by Comma : ")
list_of_word=s.split(",")
list_of_word.sort()
Number_of_Word = {}
sorted_list = []
for i in range(0 , len(list_of_word)):
    count = 0
    for j in range(0 , len(list_of_word)):
        if list_of_word[i]==list_of_word[j]:
            count+=1
        Number_of_Word[list_of_word[i]] = count

print("Number of sentence words Sorted : ")
print(Number_of_Word)

val_num = list(Number_of_Word.values())
key_num = list(Number_of_Word.keys())

for i in range(0 , len(Number_of_Word)):
    if val_num[i] == 1:
        sorted_list.append(key_num[i])


print("The Unique and Sorted Words in Sentence : ")
print(sorted_list)

