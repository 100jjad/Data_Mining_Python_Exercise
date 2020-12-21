# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:27:58 2020

@author: 100jjad

Calculate matrix transpose



..........Sajjad Soheyli.........Series.....02.............Exercise....02...........

"""


R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:"))


matrix = [] 

#Get Matrix from the user

for i in range(R):  
    print("Enter row" ,i," inputs:")      
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix.append(a) 
    
    
    
    
T_Matrix = [[0 for x in range(R)] for y in range(C)] 

for i in range(C):
    for j in range(R):
        T_Matrix[i][j] = matrix[j][i]



print("Origin Matrix : \n" , matrix , "\n\n\n Transpose Matrix : \n" , T_Matrix)