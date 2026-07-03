import numpy as np
## One Dimension Array

oneDimen = np.array([1, 2, 3, 4, 5])

print(oneDimen)


## Two Dimension Array
twoDim = np.array([[1, 2, 3],
                [4, 5, 6]])

print(twoDim)



################Arithematic Operations

# * Sum
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newArray = np.add(arr1, arr2)

print(newArray)

# * Subtract

arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])

newArray2 = np.add(arr3, arr4)

print(newArray2)

# * Multiplication

arr5 = np.array([10, 20, 30, 40, 50, 60])
arr6 = np.array([20, 21, 22, 23, 24, 25])

newArray3 = np.multiply(arr5, arr6)

print(newArray3)


# same for others, methods are Power,mod() or remainder(),divmod()

arr7 = np.array([-1, -2, 1, 2, 3, -4])
newArray7 = np.absolute(arr7)
print(newArray7)


# Numpy Builtin Functions
array8 = np.array([10, 20, 30, 40, 50])
print("Maximum:", np.max(array8))
print("Minimum:", np.min(array8))
print("Mean:", np.mean(array8))
print("Sum:", np.sum(array8))

# Resha[ing]
array9 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Length of array:", len(array9))
arr2d = array9.reshape(4, 3)
print("\nReshaped to 2-D:")
print(arr2d)
arr3d = array9.reshape(2, 3, 2)
print("\nReshaped to 3-D:")
print(arr3d)


##  Indexing and slicing
## Acccess first Element of narray
accessFirst = np.array([1, 2, 3, 4])

print(accessFirst[0])
# Add Third and Fourth
arrayToadd = np.array([1, 2, 3, 4])

print(arrayToadd[2] + arrayToadd[3])

## Access 5th element of 2nd row
twoD = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(twoD[1, 4])


## Access in three D array: access 3rd element of 2nd row in first array

arr3 = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10,11,12]]
])
print(arr3[0, 1, 2])


## Access in 2d array using negative indexing: access last element of 2nd row
arrNeg = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(arrNeg[1, -1])


## Slicing in 1D array is same as slicing in list 

arrSlcinf = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

# Second row, columns 1 to 2
print("Slicing in 2d")
print(arrSlcinf[1, 1:3]) # First parameter is row index and 2nd one is column  1 to 2 

print(arrSlcinf[:, 1:4]) # al rows and columns 1 to 3 

