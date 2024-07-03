import numpy as np

#importing custom function to universal function module

def mypow(x,y):
    return x**y , y**x

mypow = np.frompyfunc(mypow, 2, 2)

print(mypow([1,2,3,4,5], [2,3,4,5,6]))

#Summation on axis
arr = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,0])
x = np.sum([arr,arr2] , axis = 1)
print(x)

#product on axis
y = np.prod([arr,arr2], axis = 1)
print(y)

#GCD and LCM
z=np.lcm.reduce(arr)
print(z)

z=np.gcd.reduce(arr2)
print(z)

#degree and radian conversion
degree = np.array([100, 120, 80, 30, 60])
radians = np.deg2rad(degree)
print(radians)

new_degree = np.rad2deg(radians)
print(new_degree)

#Trignomentric values to angles
#Example sin function

sinvalues = np.array([-1, 1, 0, -1])
sin_radians = np.arcsin(sinvalues)
print(sin_radians)

#set operations (union, intesection, set difference, symmetric difference)

unionarr = np.union1d(arr, arr2)
print(unionarr)
interarr = np.intersect1d(arr, arr2)
print(interarr)

diffarr = np.setdiff1d(arr, arr2)
print(diffarr)

symmdif = np.setxor1d(arr,arr2)
print(symmdif)
