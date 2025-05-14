#Liste/List
#Sıralı bir kolleksiyon ve Elemanları değişebilir

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1]="orange"
print(fruits)
print(fruits[1])

#Demet/Tuple
#Sıralı bir kolleksiyon ve Elemanları değiştirilemez
coordinates = (10.0, 20.0)
print(coordinates)
print(coordinates[0])

#Küme/Set
#Sırasız ve tekrarsız bir kolleksiyon
unique_numbers = {1, 2, 3, 4, 5,45,5,3,4}
print(unique_numbers)

#Sözlük/Dictionary
#Anahtar-değer çiftleri içeren bir veri yapısı

person = {"first_name": "John", "last_name": "Doe", "age": 30}
print(person)
print(person["first_name"])

#Matris

#Matris, birden fazla boyutta veri saklamak için kullanılan bir veri yapısıdır.
#Matris, genellikle sayılarla temsil edilen bir tablo gibi düşünülebilir.

#Matris oluşturma
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

#Boş matris oluşturma 3X3

rows = 3
cols = 3
empty_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(empty_matrix)

print(matrix[0])
print(matrix[0][1]) #1. satır 2. sütün

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Satır toplamları
cols = len(matrix2[0])  # Sütun sayısını al
rows = len(matrix2)     # Satır sayısını al

for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix2[i][j]
    print(f"{j}. sütun toplamı: {col_sum}")
max_value = matrix[0][0]
for row in matrix:
    for elem in row:
        if elem > max_value:
            max_value = elem
print("En büyük değer:", max_value)


rows = int(input("Kaç satır? "))
cols = int(input("Kaç sütun? "))
matrix3 = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Matris[{i}][{j}] giriniz: "))
        row.append(value)
    matrix3.append(row)

print("Girilen Matris:")
for row in matrix3:
    print(row)
