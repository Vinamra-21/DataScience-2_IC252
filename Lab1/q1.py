import numpy as np
import matplotlib . pyplot as plt
# Question 1: Find out the size of array ’a’, ’b’, and ’c’. In the following code block.

a = np . array (42)
b = np . array ([1 , 2, 3 , 4 , 5])
c = np . array ([[1 , 2, 3] , [4 , 5, 6]])


#solution
def arr_sze(arr):
    return arr.nbytes/4
# Print size of all arrays
print("size of array a = ",arr_sze(a))
print("size of array b = ",arr_sze(b))
print("size of array c = ",arr_sze(c))

#alternate approach#

# Print size of all arrays
print("size of array a = ",np.size(a))
print("size of array b = ",np.size(b))
print("size of array c = ",np.size(c))

#to find shape of array 'c' as it is a 2D array
print("shape (rows,columns) of array c = ",np.shape(c))