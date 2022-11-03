"""Alta3 Research | treich@alta3.com
  Numpy arrays and operations"""

import numpy as np
np.random.seed(0)
# Use the randint function to generate 1-, 2-, and 3-dimensional arrays
arr1d = np.random.randint(11, size=5) # 1-D array of 5 random integers between 0-10
arr2d = np.random.randint(11, size=(2, 3)) # 2-D array  spanning 2 rows, 3 cols
arr3d = np.random.randint(11, size=(2, 3, 4)) # 3-D array containing two 2-D arrays of 3 rows, 4 cols each 

print("One-dimensional array:", arr1d, sep="\n")
print("Two-dimensional array:", arr2d, sep="\n")
print("Three-dimensional array:", arr3d, sep="\n")

print("First element of arr1d is:", arr1d[0])
print("Element in position (0,0) of arr2d is:", arr2d[0,0])
print("Element in position (0,0,0) of arr3d is:", arr3d[0,0,0])

print(arr1d)
print(arr1d*2) # multiply each element of arr1d by 2
print(list(arr1d)*2) # convert arr1d into a list, then multiply that list by 2

