import numpy as np

a = np.array([1, 1, 1, 1], dtype='int64')
print(a)
b = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(b)
print(b.ndim)  # Nechta list borligini korsatadi
print(b.shape)  # nechta list borligini va uni ichda nechta obyekt borligini korsatadi
print(a.dtype)  # type ni korsatadi
print(a.itemsize)  # hajmi
print(a.nbytes)  # umumiy hajmi
print(b[0, -1])  # listdan chiqarish
print(b[0, :])  # bitta indexdagi hamma sonni print qilish yani listni ajratib olish
print(b[:, 1])  # bu hamma indexdagi listlardan 1 xil qatorda joylashganlarini print qiladi
print(b[0,
      1:6:2])  # malum bir list indexdan bironbir indexdan ixtiyoriy indexgachon bolgan sonlarni har 2 chisini chiqarish
c = np.array([[[1, 2], [3, 4]], [[6, 7], [8, 9]]])  # 3d
print(c[0, 0, 1])  # 3dlistdan chiqarish
c[:, 0, :] = [[9, 9], [9, 9]]  # almashtirish
print(c)
d = np.zeros((1, 3, 3))  # 0dan list yaratadi one 1 dan yaratish full 99 yozilgan sondan yaratish
print(d)
print(np.random.rand(1, 4))  # rand orqalik yaratish
print(np.random.randint(7, size=(3, 3)))  # kirtilgan shakl orqalik random yaratish
print(np.identity(5))  # 5 ga 5 yaratish
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=1)
print(r1)
# Matematika
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5])
print(a + 2)
print(a * 2)
print(a / 2)
print(a - 2)
print(a + b)
print(np.sin(a))  # or cos
# LInear algebra
print(np.matmul(a, b))
# Statistic
print(np.min(a))  # minum chiqaradi
print(np.max(a))  # maxsimum chiqaradi
print(np.sum(a))  # sonlarni qushib chiqaradi
