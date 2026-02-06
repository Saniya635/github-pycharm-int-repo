import numpy as np
print("Enter elements of 5x3 matrix:")
a = []
for i in range(5):
    row = []
    for j in range(3):
        row.append(int(input()))
    a.append(row)
print("Enter elements of 3x2 matrix:")
b = []
for i in range(3):
    row = []
    for j in range(2):
        row.append(int(input()))
    b.append(row)
a = np.array(a)
b = np.array(b)
result = np.dot(a, b)
print("Product Matrix:")
print(result)
