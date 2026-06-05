import numpy as np
a = np.array([[3, 1, 4, 2],
              [2, 3, 4, 5]])

print(np.sort(a))          # sorting
print(np.sort(a)[:,::-1])          # reverse sorting
print(np.argsort(a))       # indices of sorted array (shows how the original array is rearranged to get the sorted array)
print(np.argwhere(a == 2))    # index of 2
a