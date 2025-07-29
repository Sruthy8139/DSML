import numpy as np
n = int(input("Enter size of square matrix (n x n): "))
print(f"Enter {n*n} elements (row-wise, space separated):")
elements = list(map(float, input().split()))
print("elements:",elements)
matrix = np.array(elements).reshape(n, n)
print("\nOriginal Matrix:")
print(matrix)
det = np.linalg.det(matrix)
print(det)
if det == 0:
    print("\nMatrix is singular (det = 0), inverse does not exist.")
else:
    inverse = np.linalg.inv(matrix)
    print("\nInverse Matrix:")
    print(inverse)
