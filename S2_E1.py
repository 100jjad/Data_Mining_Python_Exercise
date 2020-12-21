# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 11:47:36 2020

@author: 100jjad


1: Get sparse matrix from user with input() function

2: Save the given matrix in sparse form to a list while save only non zero elements.
(without any packages such as scipy)



..........Sajjad Soheyli.........Series.....02.............Exercise....01...........

"""



R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:"))
N=0


matrix = [] 

#Get Matrix from the user

for i in range(R):  
    print("Enter row" ,i," inputs:")      
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix.append(a) 
    
print("\n\nThe main matrix :\n")
    

#Show The Main Martis
    
for i in range(R):    
    print("[ ", end = " ")     
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print(" ]") 

    print() 
    
    

#Create Sparse Matrix
Sparse_Matrix = []
Sparse_Matrix.append([R,C,0])

for i in range(0 , R):
    for j in range(0 , C):
        if matrix[i][j]!=0:
            N+=1
            Sparse_Matrix.append([i+1 , j+1 , matrix[i][j]])
    
Sparse_Matrix[0][2]=N    
print("\n\n\n",Sparse_Matrix , "\n\n\n")
    

#Show Sparse Matrix

print("      Row    Col    Value\n")
    
for i in range(N+1):    
    print("[ ", end = " ")     
    for j in range(3): 
        print("   ",Sparse_Matrix[i][j], end = "   ") 
    print(" ]") 
    print() 
    
    