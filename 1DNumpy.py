import numpy as np

a = np.array([0, 1, 2, 3, 4])

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(a.dtype)

c = np.array([20, 1, 2, 3, 4])
d = c[1:4]
c[3:5] = 300, 400
print(c)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8  :2])

maths = np.array([1, -1, 1, -1])
mean = maths.mean()
print(mean)
deviation = maths.std()
print(deviation)

b = np.array([-1, 2, 3, 4, 5])
max_b = b.max()
print(max_b)
min_b = b.min()
print(min_b)

u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
print(z)

# Plotting functions

import numpy as np 

import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    plt.show()

# Plotvec1(u, z, v)

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.add(arr1, arr2)
print(arr3)

arr4 = np.array([10, 20, 30, 40, 50, 60])
arr5 = np.array([20, 21, 22, 23, 24, 25])
arr6 = np.subtract(arr4, arr5)
print(arr6)

arr7 = np.array([10, 20, 30, 40, 50, 60])
arr8 = np.array([2, 1, 2, 3, 4, 5])
arr9 = np.multiply(arr7, arr8)
print(arr9)

arr10 = np.array([10, 20, 30, 40, 50, 60])
arr11 = np.array([3, 5, 10, 8, 2, 33])
arr12 = np.divide(arr10, arr11)
print(arr12)

X = np.array([1, 2])
Y = np.array([3, 2])
Z = np.dot(X, Y)
print(Z)

print(np.linspace(-2, 2, num=5))