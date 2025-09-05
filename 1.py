import numpy as np

def save_and_load_array(arr, arr_txt, arr_np):
    print(arr, arr.nbytes)
    np.savetxt(arr_txt, arr, delimiter=',')
    np.save(arr_np, arr)
    load_arr_np = np.load(arr_np)
    load_arr_txt = np.loadtxt(arr_txt, delimiter=',')
    print(load_arr_np)
    print(load_arr_txt)



#1 задание
print('1 задание')
array = np.array([1, 7, 13, 105])
save_and_load_array(array,'array.txt', 'array.npy' )

#2 задание
print('2 задание')
arr0 = np.array([])
arr1 = np.array([])
arr5 = np.array([])

for i in range(10):
    arr0 = np.append(arr0, 0)
    arr1 = np.append(arr1, 1)
    arr5 = np.append(arr5, 5)

save_and_load_array(arr0, 'arr0.txt', 'arr0.npy')
save_and_load_array(arr1, 'arr1.txt', 'arr1.npy')
save_and_load_array(arr5, 'arr5.txt', 'arr5.npy')

#3 задание
print('3 задание')
arr_even = np.array([i for i in range(30, 71) if i % 2 == 0])
save_and_load_array(arr_even, 'arr_even.txt', 'arr_even.npy')

#4 задание
print('4 задание')
arr4 = np.linspace(5, 50, 10)
save_and_load_array(arr4, 'arr4.txt', 'arr4.npy')

#5 задание
print('5 задание')
arr_rand_3_3_3 = np.random.randint(1, 100, (3, 3, 3))
print(arr_rand_3_3_3, arr_rand_3_3_3.nbytes)

np.savetxt('array_text.txt', arr_rand_3_3_3.reshape(3, -1), delimiter=',', fmt='%d')
np.save('array_binary.npy', arr_rand_3_3_3)

loaded_text = np.loadtxt('array_text.txt', delimiter=',').reshape(3, 3, 3)
print(loaded_text)

loaded_binary = np.load('array_binary.npy')
print(loaded_binary)

#6 задание
print('6 задание')
arr6 = np.arange(30, 42).reshape(3, 4)
save_and_load_array(arr6, 'arr6.txt', 'arr6.npy')

#7 задание
print('7 задание')
arr7 = np.zeros((10, 10))
arr7[0, :] = 1
arr7[-1, :] = 1
arr7[:, 0] = 1
arr7[:, -1] = 1
save_and_load_array(arr7, 'arr7.txt', 'arr7.npy')

#8 задание
print('8 задание')
diagonal = [1, 2, 3, 4, 5]
arr8 = np.diag(diagonal)
save_and_load_array(arr8, 'arr8.txt', 'arr8.npy')


#9 задание
print('9 задание')
arr9 = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        if i != j:
            if (i + j) % 2 == 1:
                arr9[i, j] = 1

save_and_load_array(arr9, 'arr9.txt', 'arr9.npy')

#10 задание
print('10 задание')
march_2017 = np.arange('2017-03-01', '2017-04-01', dtype='datetime64[D]')
print(march_2017.nbytes)
np.savetxt('march_2017.txt', march_2017.astype('datetime64[D]'), fmt='%s', delimiter='\n')
np.save('march_2017.npy', march_2017)
loaded_binary = np.load('march_2017.npy')
loaded_txt = np.genfromtxt('march_2017.txt', dtype='datetime64[D]')
print(loaded_binary)
print(loaded_txt)
