import numpy as np

signal = np.array([0, 1, 0, -1])

result = np.fft.fft(signal)

print(result)


## Numpy Array from list
arrayFromList = np.array([1, 2, 3, 4, 5])

print(arrayFromList)
print(type(arrayFromList))


## Numpy Array From Tuple

arrayFromTuple = np.array((1, 2, 3, 4, 5))

print(arrayFromTuple)


## Single Dimension array


zeroDimensionArray = np.array(42)

print(zeroDimensionArray)

## One Dimension Array

oneDimen = np.array([1, 2, 3, 4, 5])

print(oneDimen)


## Two Dimension Array
twoDim = np.array([[1, 2, 3],
                [4, 5, 6]])

print(twoDim)


## Three Dimaneions array
threeDim = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print(threeDim)



## Check the number of dimensions in the array

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[1, 2], [3, 4]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


