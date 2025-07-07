import numpy as np
arr = np.array([[4, 5, 6],
                [7, 8, 9]])
total_sum = np.sum(arr)
column_sum = np.sum(arr, axis=0)
row_sum = np.sum(arr, axis=1)
print("Array:\n", arr)
print("Sum of all elements:", total_sum)
print("Sum of each column:", column_sum)
print("Sum of each row:", row_sum)

