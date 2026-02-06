#a
import numpy as np
mat = np.eye(4)
print("4x4 Identity Matrix:")
print(mat)

#b
import numpy as np
mat1 = np.random.randint(1, 10, (3, 3))
mat2 = np.random.randint(1, 10, (3, 3))
print("Matrix 1:")
print(mat1)
print("\nMatrix 2:")
print(mat2)
add = mat1 + mat2
print("\nMatrix Addition:")
print(add)
mul = np.dot(mat1, mat2)
print("\nMatrix Multiplication:")
print(mul)
