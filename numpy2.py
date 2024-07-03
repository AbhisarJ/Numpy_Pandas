import numpy as np

A = np.array([1,2,3,4,5])
B = np.array([9,7,8,6,9])

#Join
new_array = np.concatenate((A,B))
print(new_array)

#Split
C = np.array_split(new_array , 5)
print(C)

#Search
x = np.where(A==4)
print(x)
x = np.searchsorted(A, 4)
print(x)

#Sort
arr = np.array([3,2,5,4,1])
print(arr)
sort_arr = np.sort(arr)
print(sort_arr)

#Filter
filter_array = []

for i in arr:
    if i>2:
        filter_array.append(True)

    else:
        filter_array.append(False)

new_arr = arr[filter_array]
print(filter_array, new_arr)