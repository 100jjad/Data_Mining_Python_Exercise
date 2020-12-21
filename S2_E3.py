# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:59:19 2020

@author: 100jjad


Add two sparse matrix with same dimensions




..........Sajjad Soheyli.........Series.....02.............Exercise....03...........


"""
#Get two Matrix From User

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:"))
N1=0
N2=0
N3=0


matrix1 = [] 
matrix2 = [] 


for i in range(R):  
    print("Enter row" ,i," inputs of First Matrix : ")      
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix1.append(a) 
    
print("\n")    

for i in range(R):  
    print("Enter row" ,i," inputs of Second Matrix : ")      
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix2.append(a) 
    
    
#sum of two Matrix  By Usual Method

Matrix_Sum = [[0 for x in range(R)] for y in range(C)] 

 

for i in range(R):
    for j in range(C):
        Matrix_Sum[i][j] = matrix1[i][j] + matrix2[i][j] 

print("Sum of two Sparse Matrix By Usual Method : \n" , Matrix_Sum)




#Create Sparse Matrix   
    
    
Sparse_Matrix1 = []
Sparse_Matrix1.append([R,C,0])


Sparse_Matrix2 = []
Sparse_Matrix2.append([R,C,0])


Sparse_Matrix_Sum = []
Sparse_Matrix_Sum.append([R,C,0])




for i in range(0 , R):
    for j in range(0 , C):
        if matrix1[i][j]!=0:
            N1+=1
            Sparse_Matrix1.append([i+1 , j+1 , matrix1[i][j]])
    
Sparse_Matrix1[0][2]=N1   
print("\n\n Sparse_Matrix1 : \n",Sparse_Matrix1 , "\n\n\n")



for i in range(0 , R):
    for j in range(0 , C):
        if matrix2[i][j]!=0:
            N2+=1
            Sparse_Matrix2.append([i+1 , j+1 , matrix2[i][j]])
    
Sparse_Matrix2[0][2]=N2   
print("\n\n Sparse_Matrix2 : \n",Sparse_Matrix2 , "\n\n\n")
    
    

for i in range(0 , R):
    for j in range(0 , C):
        if Matrix_Sum[i][j]!=0:
            N3+=1
            Sparse_Matrix_Sum.append([i+1 , j+1 , Matrix_Sum[i][j]])
    
Sparse_Matrix_Sum[0][2]=N3   
print("\n\n Sparse_Matrix_Sum : \n",Sparse_Matrix_Sum , "\n\n\n")




#sum of two Matrix  By Unusual Method

Unusual_Matrix_Sum = [[0 for x in range(R)] for y in range(C)] 
"""
for i in range(1 , N1):
    for j in range(1 , N2):
        if Sparse_Matrix1[i][0] == Sparse_Matrix2[j][0]  & Sparse_Matrix1[i][1] == Sparse_Matrix2[j][1]:
            row = Sparse_Matrix1[i][0] -1
            col = Sparse_Matrix1[i][1] -1
            temp = Sparse_Matrix1[i][2] + Sparse_Matrix2[j][2]
            Unusual_Matrix_Sum[row][col] += temp
            temp = 0
            break
"""

for i in range(1 , N1+1):
    row = Sparse_Matrix1[i][0] -1
    col = Sparse_Matrix1[i][1] -1
    Unusual_Matrix_Sum[row][col] += Sparse_Matrix1[i][2]

for i in range(1 , N2+1):
    row = Sparse_Matrix2[i][0] -1
    col = Sparse_Matrix2[i][1] -1
    Unusual_Matrix_Sum[row][col] += Sparse_Matrix2[i][2]
    
print("\n\nSum of two Sparse Matrix By Unusual Method : \n" , Unusual_Matrix_Sum)
                


    

