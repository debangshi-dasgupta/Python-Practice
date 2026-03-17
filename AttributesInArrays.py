import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.shape(arr)) #array dimensions
print(np.size(arr)) #length of array
print(np.ndim(arr)) #number of array dimensions
print(arr.dtype) #datatype of array elements
print(arr.astype(str)) #convert an array to a string
print(arr.astype(float)) #convert an array to a float