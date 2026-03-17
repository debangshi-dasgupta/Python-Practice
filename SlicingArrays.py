import numpy as np

#Slicing arrays with one row
arr1 = np.array([10,20,30,40,50])
print(arr1[0:2])
#Slicing arrays with two rows
arr2 = np.array([[10,20,30,40],[50,60,70,80]])
print(arr2[0:2,0:2])
#Slicing arrays with three rows
arr3 = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(arr3[2,1])

