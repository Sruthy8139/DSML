import numpy as np
row=int(input("Enter the rows:"))
col=int(int(input("Enter the colum:")))
matrix=[]
for i in range(row):
	row=[]
	for j in range(col):
		row.append(int(input("Enter the elements:")))
	matrix.append(row)
print("Matrix")
print(matrix)
mat=np.array(matrix)
determinant=np.linalg.det(mat)
print(determinant)
