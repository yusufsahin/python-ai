import numpy as np

A=np.array([[2,3],[1,1]])
B=np.array([[1,2],[3,4]])
print("Toplam\n", A + B)
print("Fark:\n", A - B)
print("Çarpım:\n", A@B)
print("Transpoz:\n", A.T)
print("Sabit çarpım:\n", 2 * A)
print("İz:\n", np.trace(A))
print("Birim matris:\n", np.eye(2))
print("A nın 2. kuvveti:\n", np.linalg.matrix_power(A, 2))
print("Determinant:\n", round(np.linalg.det(A),4))
print("Ters matris:\n", np.linalg.inv(A))

# Not: NumPy kullanımı, matris işlemlerini daha verimli ve okunabilir hale getirir.
# NumPy, matris işlemleri için optimize edilmiş fonksiyonlar sunar.
# Bu nedenle, NumPy ile yapılan işlemler genellikle daha hızlıdır.

# ----------------------------------------
# DENKLEM ÇÖZÜMÜ
# ----------------------------------------

# Denklem sistemi:
# 2x + 3y = 20
# 1x + 1y = 9

# Matris formu:
# Z = [[2, 3], [1, 1]]
# T = [[20], [9]]
Z = np.array([[2, 3], [1, 1]])
T = np.array([[20], [9]])
x= np.linalg.solve(Z, T)
print("Denklem çözümü:\n x:", x[0], "ve y:", x[1])
