import numpy as np

a = np.array([10, 20, 30, 40])

b = a.copy()
c = a.view()

a[1] = 999

print("Original array:", a)
print("Copy array:", b)#stores the values of variable "a" in a new memory location
print("View array:", c)