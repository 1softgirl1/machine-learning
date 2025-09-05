import numpy as np

a11 = float(input('Введите коэффициент a11: '))
a12 = float(input('Введите коэффициент a12: '))
a21 = float(input('Введите коэффициент a21: '))
a22 = float(input('Введите коэффициент a22: '))
b1 = float(input('Введите коэффициент b1: '))
b2 = float(input('Введите коэффициент b2: '))

A = np.array([[a11, a12], [a21, a22]])
B = np.array([b1, b2])
det = np.linalg.det(A)

if det == 0:
    print('Система не имеет решений или имеет бесконечно много решений')
else:
    x = np.linalg.solve(A, B)
    print("Решение системы (x, y):")
    print(x)