import numpy as np
import matplotlib . pyplot as plt
# Question 3: Array adressing and slicing. As the dimensions of the array increase it becomes very important how one indexes
# those arrays, slicing becomes important when one wants to get some desired subpart of a whole array. This Question has two parts.

# 3.1. Print the sum of left diagonal and right diagonal of a square matrix.

mat = np . array ([[1 ,3 ,4 ,5 ,2] ,[1 ,5 ,2 ,4 ,3] ,[5 ,2 ,3 ,4 ,1 ,] ,[1 ,4 ,2 ,6 ,9] ,[4 ,5 ,2 ,1 ,7]])
def left_diagonal_sum ( mat : np . ndarray ) ->float :
    sum=0
    for i in range(mat.shape[0]):
        sum+=mat[i][i]
    # sum=np.trace(mat)   #alternate approach
    return sum

def right_diagonal_sum ( mat : np . ndarray ) ->float :
    sum=0
    r,c=mat.shape
    for i in range(r):
        sum+=mat[i][r-i-1]
    # flip_mat = np.fliplr(mat)    #alternate approach
    # sum = np.trace(flip_mat)
    return sum
    
print (f'Left Diagonal Sum of { mat =} is { left_diagonal_sum (mat)}')
print (f'Right Diagonal Sum of { mat =} is { right_diagonal_sum ( mat )}')

print() #blank line

# 3.2. From the matrix of previous part, print the 3x4 sub-matrix from 1st row 2nd column to 3rd row 5th column. Make use of
# the array slicing operations preferably , use of for loops is discouraged.

def submatrix_3x4 ( mat : np . ndarray ) -> np . ndarray :
    sub_matrix=mat[0:3,1:5]
    return sub_matrix

print (f'The desired submatrix of \n { mat } is \n { submatrix_3x4 ( mat )}')