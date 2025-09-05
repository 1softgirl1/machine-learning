import numpy as np

#1 задание
print('1 задание')
arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([10, 20, 40])
common = np.intersect1d(arr1, arr2)
print(common)

#2 задание
print('2 задание')
arr_ = np.array([10, 10, 20, 20, 30, 30])
unique= np.unique(arr_)
print(unique)

#3 задание
print('3 задание')
arr_ = np.array([10, 10, 20, 20, 30, 30])
unique, counts = np.unique(arr_, return_counts=True)
print(unique)
print(counts)

#4 задание
print('4 задание')
new_arr = np.tile(arr_, 3)
print(new_arr)

#5 задание
print('5 задание')
arr5 = np.array([200, 300, np.nan, 4, np.nan, 6, 7, np.nan])
arr5_ = arr5[~np.isnan(arr5)]
print(arr5_)

#6 задание
print('6 задание')
arr6 = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
k = 4
result = np.sort(arr6)[:k]
print(result)

#7 задание
print('7 задание')
arr7 = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
target = 3.09066280756759
result = arr7[np.argmin(np.abs(arr7 - target))]
print(result)

print('8 задание')
arr1 = np.array(['Python', 'PHP'])
arr2 = np.array(['Java', 'C ++'])
result = np.char.add(np.char.add(arr1, ' '), arr2)
print(result)

print('9 задание')
arr9 = np.array(['Python', 'PHP', 'JS', ' examples', 'html'])
result = np.array([np.char.count(s, 'P') for s in arr9])
print(result)

print('10 задание')
roots_a = np.roots([1, -4, 7])
print("Корни x^2 - 4x + 7:", roots_a)
roots_b = np.roots([1, -11, 9, 11, -10])
print("Корни x^4 - 11x^3 + 9x^2 + 11x - 10:", roots_b)