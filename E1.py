# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:17:55 2020

@author: 100jjad
"""
#1. Write a Python program to count the number of characters (character frequency) in a string
#	Sample String : google.com'
#	Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 


#..........Sajjad Soheyli.........Exercise....01...........


"""
lst = [] 
n = int(input("Enter number of elements : ")) 


for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 
"""

n = input("Enter a String : ") 

for i in range(0 , len(n)):
    num = 0
    for j in range(0 , len(n)):
        if n[i]==n[j]:
            num+=1
#    print(n[:i])
#    print(n[i] in n[:i])        
    if (n[i] in n[:i]) != True:
        print(str(n[i])+" : "+str(num))
