# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:14:17 2020

@author: 100jjad

Multiply two Sparse Matrix



..........Sajjad Soheyli.........Series.....02.............Exercise....04...........

"""

#Get Martix 1 from the user

N1=0
N2=0

R1 = int(input("Enter the number of The First matrix Rows : ")) 
C1 = int(input("Enter the number of The First matrix columns:"))


matrix1 = [] 



for i in range(R1):  
    print("Enter row" ,i," inputs of First Matrix : ")      
    a =[] 
    for j in range(C1):      
         a.append(int(input())) 
    matrix1.append(a) 
    
print("\n")    


#Get Martix 2 from the user


R2 = int(input("Enter the number of The First matrix Rows : ")) 
C2 = int(input("Enter the number of The First matrix columns:"))


matrix2 = [] 



for i in range(R2):  
    print("Enter row" ,i," inputs of First Matrix : ")      
    a =[] 
    for j in range(C2):      
         a.append(int(input())) 
    matrix2.append(a) 
    
print("\n")   


#Create Sparse Matrix   
    
    
Sparse_Matrix1 = []
Sparse_Matrix1.append([R1,C1,0])


Sparse_Matrix2 = []
Sparse_Matrix2.append([R2,C2,0])




for i in range(0 , R1):
    for j in range(0 , C1):
        if matrix1[i][j]!=0:
            N1+=1
            Sparse_Matrix1.append([i+1 , j+1 , matrix1[i][j]])
    
Sparse_Matrix1[0][2]=N1   
print("\n\n Sparse_Matrix1 : \n",Sparse_Matrix1 , "\n\n\n")



for i in range(0 , R2):
    for j in range(0 , C2):
        if matrix2[i][j]!=0:
            N2+=1
            Sparse_Matrix2.append([i+1 , j+1 , matrix2[i][j]])
    
Sparse_Matrix2[0][2]=N2   
print("\n\n Sparse_Matrix2 : \n",Sparse_Matrix2 , "\n\n\n")
    
    




#Multiply of two matrices


if C1 != R2:
    print("Multiplication Operation is Not Possible")
else:
    Unusual_Matrix_Multiply = [[0 for x in range(C2)] for y in range(R1)] 
    for i in range(1,N1+1):
        for j in range(1,N2+1):  
                    if Sparse_Matrix1[i][1] == Sparse_Matrix2[j][0] :
                            temp = Sparse_Matrix1[i][2] * Sparse_Matrix2[j][2]
                            row = Sparse_Matrix1[i][0] -1
                            col = Sparse_Matrix2[j][1] -1
                            Unusual_Matrix_Multiply[row][col] +=temp 
                        
                                                
                    
                
print("\n\n Multiply two Sparse Matrix : \n",Unusual_Matrix_Multiply , "\n\n\n")