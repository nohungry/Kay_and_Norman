import numpy as np

a = np.random.randint(5, high=8, size=(2, 3))
b = np.random.randint(5, high=8, size=(3, 1))
print(a)
print(b)
print('-----')
print(a.dot(b))