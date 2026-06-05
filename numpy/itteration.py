import numpy as np
#1d array
a = np.array([1, 2, 3])

for i in a:
    print(i)    
#2d array
b = np.array([[1, 2, 3], [4, 5, 6]])
for row in b:
    for element in row:
        print(element)