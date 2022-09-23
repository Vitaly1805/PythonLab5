import numpy as np

arr = np.random.randint(10, 31, size = 10, dtype=np.int32)
print('Сгенерированный список:')
print(arr)
print(arr.dtype)
print('----------------------------------------------------')

arr = np.array(arr).astype(np.float32)
print('Изменение типа списка:')
print(arr)
print(arr.dtype)
print('----------------------------------------------------')

arr[3:6] *= -1
print('Отрицательные значения по интервалу 3..5:')
print(arr)
print('----------------------------------------------------')

arr[np.argmax(arr)] = 0
print('Приравнивание к 0 максимального элемента списка:')
print(arr)
print('----------------------------------------------------')

np.savetxt('test.txt', arr,  fmt='%1.1f', newline=' ')