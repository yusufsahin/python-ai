import matplotlib.pyplot as plt
import time

def draw_array(arr, highlight=None, title=""):
    plt.clf()
    colors = ['red' if i in highlight else 'skyblue' for i in range(len(arr))]
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Değer")
    plt.pause(0.5)

def insertion_sort_visual(arr):
    plt.ion()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        draw_array(arr, highlight=[i], title=f"Anahtar: {key}")
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            draw_array(arr, highlight=[j+1], title=f"Kaydırılıyor: {arr}")
        arr[j + 1] = key
        draw_array(arr, highlight=[j+1], title=f"Yerleştirildi: {key}")
    plt.ioff()
    draw_array(arr, title="Sıralı Dizi")
    plt.show()


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]# sıradaki eleman(anahtar)
        j = i-1
        #Anahtarı yerleştirmek için sola kaydırma
        while j >= 0 and arr[j] > key: #key deki eleman ile karşılaştır ve buradaki karşılaştırma sıralama tipini belirliyor
            arr[j+1] = arr[j] #büyük olanları sağa kaydır
            j -= 1
        arr[j+1] = key #anahtarı doğru yere yerleştir
def insertion_sort_trace(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nAdım {i}: Anahtar = {key}")
        while j >= 0 and arr[j] > key:
            print(f"  {arr[j]} > {key}, {arr[j]} sağa kaydırılıyor")
            arr[j + 1] = arr[j]
            j -= 1
            print(f"  Durum: {arr}")
        arr[j + 1] = key
        print(f"  Anahtar {key} pozisyonuna yerleştirildi")
        print(f"  Sonuç: {arr}")


arr=[12, 11, 13, 5, 6]
print(arr)
insertion_sort(arr)
print("Sorted array is:",arr)
arr2=[12, 11, 13, 5, 6]
insertion_sort_trace(arr2)
arr3=[12, 11, 13, 5, 6]
insertion_sort_visual(arr3)