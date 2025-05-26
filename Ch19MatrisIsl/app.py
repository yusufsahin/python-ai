def matris_topla(A,B):
    satir= len(A)
    sutun= len(A[0])
    C = [[0 for _ in range(sutun)] for _ in range(satir)]
    for i in range(satir):
        for j in range(sutun):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matris_fark(A,B):
    satir= len(A)
    sutun= len(A[0])
    C = [[0 for _ in range(sutun)] for _ in range(satir)]
    for i in range(satir):
        for j in range(sutun):
            C[i][j] = A[i][j] - B[i][j]
    return C

def matris_carp(A, B):
    sonuc= [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                sonuc[i][j] += A[i][k] * B[k][j]
    return sonuc

def matris_transpoz(A):
    return  [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def sabit_carp(A, k):
    return [[eleman * k for eleman in satir] for satir in A]

def matris_iz(A):
    return sum(A[i][i] for i in range(len(A)))

def birim_matris(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def matris_ussu(A, n):
    sonuc = birim_matris(len(A))
    for _ in range(n):
        sonuc = matris_carp(sonuc, A)
    return sonuc

def determinant_2x2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

def ters_matris_2x2(A):
    det = determinant_2x2(A)
    if det == 0:
        raise ValueError("Determinant sıfır, ters yok.")
    return [
        [ A[1][1]/det, -A[0][1]/det],
        [-A[1][0]/det,  A[0][0]/det]
    ]

# Vektörle değil, genel matris çarpımı kullanılır
# 2x2 ile 2x1 çarpımı zaten genel matris çarpımıdır

# Örnek kullanım
A = [[2, 3], [1, 1]]
B = [[1, 2], [3, 4]]
print("Toplam:", matris_topla(A, B))
print("Çıkarma:", matris_fark(A, B))
print('Çarpım:', matris_carp(A, B))
print("Matris A:", A)
print("Transpoz:", matris_transpoz(A))
print("Sabit çarpım:", sabit_carp(A, 2))
print("İz:", matris_iz(A))
print("Birim matris (2x2):", birim_matris(2))
print("Matris A'nın 2. kuvveti:", matris_ussu(A, 2))
print("Determinant (2x2):", determinant_2x2(A))
print("Ters matris (2x2):", ters_matris_2x2(A))

# ----------------------------------------
# DENKLEM ÇÖZÜMÜ
# ----------------------------------------

# Denklem sistemi:
# 2x + 3y = 20
# 1x + 1y = 9

Z = [[2, 3], [1, 1]]   # Katsayılar matrisi
T = [[20], [9]]        # Sonuçlar matrisi

try:
    Z_ters = ters_matris_2x2(Z)
    sonuc = matris_carp(Z_ters, T)  # vektör özel fonksiyona gerek yok
    print("Elma fiyatı:", sonuc[0][0])
    print("Armut fiyatı:", sonuc[1][0])
except ValueError as e:
    print("Hata:", e)
