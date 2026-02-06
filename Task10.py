#1
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Number of dimensions:", arr.ndim)
print("Shape of array:", arr.shape)
print("Size of array:", arr.size)
print("Data type:", arr.dtype)

#2
import numpy as np
count = np.zeros(5, dtype=int)
spoilt = 0
n = int(input("Enter number of voters: "))
for i in range(n):
    vote = int(input("Enter vote: "))
    if vote >= 1 and vote <= 5:
        count[vote - 1] = count[vote - 1] + 1
    else:
        spoilt = spoilt + 1
for i in range(5):
    print("Votes for candidate", i + 1, ":", count[i])
print("Spoilt ballots:", spoilt)


#3
import numpy as np
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input()))
arr = np.array(arr)
max_diff = max(arr) - min(arr)
print("Maximum difference:", max_diff)


#4
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])
result = np.setdiff1d(array1, array2)
print("Set difference between two arrays:")
print(result)


#5
import numpy as np
arr = []
print("Enter 10 elements:")
for i in range(10):
    arr.append(int(input()))
arr = np.array(arr)
rev = arr[::-1]
print("Original array:", arr)
print("Reversed array:", rev)