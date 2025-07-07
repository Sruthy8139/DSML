import numpy as np
a = np.array([[1, 2, 3],[2,3,4]])
print("first array:",a)
b = np.array([[4, 5, 6],[5,6,7]])
print("second array:",b)
if np.array_equal(a,b):
	print("equal")
else:
	print("not	equal")
