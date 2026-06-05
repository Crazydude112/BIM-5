import numpy as np
a = np.array(5)                  # 0D
b = np.array([1,2,3])           # 1D
c = np.array([[1,2],[3,4]])     # 2D
print(a.ndim)                      # dimension
print(b.ndim)                      # dimension
print(c.ndim)                      # dimension
ab= np.array([1, 2, 3], dtype="float")
print(ab.dtype)

# sliceing
bc= np.array([[1,2,3],[4,5,6]])
print(bc[1,1])   # row 1, col 1 → 5
#indexing
