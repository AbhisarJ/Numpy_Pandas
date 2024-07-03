import numpy as np

#Creating Arrays
A= np.array([1,2,3,4,5])
print(A)
print(type(A))

#Indexing and Slicing
print(A[0] + A[3])

arr = np.array([[1,2,3,4,5] , [6,7,8,9,4]])
print(arr[1,2])
print(arr[0,-3])

print(arr)

print(arr[1, 1:4])
print(arr[0, 1:4])
print(A[1:4:2])

#Data Types

arr2 = np.array(['hello' , 'bye' , 'goodbye'], dtype='S')
print(arr2.dtype)
print(arr2)
""" newarr = arr2.astype(bool) """

B = np.array([1,2,3,4,5], dtype='U32')
print(B)

float_arr = np.array([1.3, 2.6, 7.2, 5.1])
new_arr = float_arr.astype(int)

print(new_arr)

bool_arr = float_arr.astype(bool)
print(bool_arr)

#Copy & View

X = B.copy()
B[0]= 42
print(B,X)

Z = B.view()
B[0] = 45
print(B)
Z[0] = 43
print(Z)

#Array Shape and Reshape

print(arr.shape)

h_arr = np.array([3,4,3,9,2], ndmin=5)
print(h_arr.shape)
print(h_arr.ndim)

C = np.array([1,2,3,4,5,6,7,8,9,10])
new_C = C.reshape(5,2)
print(new_C)
neww_C = new_C.reshape(-1)
print(neww_C)


#Iterating
for x in arr:
    print(x)   

