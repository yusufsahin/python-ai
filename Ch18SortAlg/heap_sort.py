import matplotlib.pyplot as plt
import time
def heapify_trace(arr, n, i, depth=0):
    indent = "  " * depth
    print(f"{indent}heapify(arr={arr}, n={n}, i={i})")
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        print(f"{indent}  Sol çocuk arr[{left}]={arr[left]} > arr[{largest}]={arr[largest]}")
        largest = left
    if right < n and arr[right] > arr[largest]:
        print(f"{indent}  Sağ çocuk arr[{right}]={arr[right]} > arr[{largest}]={arr[largest]}")
        largest = right

    if largest != i:
        print(f"{indent}  Swap: arr[{i}]={arr[i]} ↔ arr[{largest}]={arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"{indent}  Sonra: {arr}")
        heapify_trace(arr, n, largest, depth + 1)
    else:
        print(f"{indent}  Değişim yok. Düğüm dengede.")

def heap_sort_trace(arr):
    n = len(arr)
    print("🧱 Max-Heap Oluşturuluyor...")
    for i in range(n // 2 - 1, -1, -1):
        heapify_trace(arr, n, i)
        print(f"→ {arr}\n")

    print("🔁 Elemanlar Sona Alınıyor...")
    for i in range(n - 1, 0, -1):
        print(f"Swap root ↔ arr[{i}]: {arr[0]} ↔ {arr[i]}")
        arr[0], arr[i] = arr[i], arr[0]
        print(f"  Sonra: {arr}")
        heapify_trace(arr, i, 0)
        print(f"→ {arr}\n")

    print("✅ Sıralama Tamamlandı:", arr)

# === Çizim Fonksiyonu ===
def draw_array(arr, highlight=None, title=""):
    plt.clf()
    colors = ['red' if highlight and i in highlight else 'skyblue' for i in range(len(arr))]
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.8)

# === Heapify (Görselli) ===
def heapify_visual(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        draw_array(arr, highlight=[i, largest], title=f"Swap: {arr[i]} ↔ {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        draw_array(arr, highlight=[i, largest], title="Swap sonrası")
        heapify_visual(arr, n, largest)

# === Heap Sort (Görselli) ===
def heap_sort_visual(arr):
    n = len(arr)
    plt.ion()

    # 1. Max Heap oluştur
    for i in range(n // 2 - 1, -1, -1):
        heapify_visual(arr, n, i)

    # 2. Elemanları sırayla sona al
    for i in range(n - 1, 0, -1):
        draw_array(arr, highlight=[0, i], title=f"Swap root ↔ end: {arr[0]} ↔ {arr[i]}")
        arr[0], arr[i] = arr[i], arr[0]
        draw_array(arr, highlight=[0, i], title="Swap sonrası")
        heapify_visual(arr, i, 0)

    plt.ioff()
    draw_array(arr, title="✅ Heap Sort Tamamlandı")
    plt.show()

# === Heapify (Normal) ===
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# === Heap Sort (Normal) ===
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("🧪 Orijinal Dizi:", arr)

    # Trace versiyonu
    print("\n🪵 Trace (Adım Adım) Heap Sort:")
    arr_trace = arr.copy()
    heap_sort_trace(arr_trace)

    # Normal Heap Sort
    arr_copy = arr.copy()
    heap_sort(arr_copy)
    print("✅ Sıralanmış Dizi (Heap Sort):", arr_copy)

    # Görsel Heap Sort
    print("\n📊 Heap Sort Görselleştirme Başlatılıyor...")
    heap_sort_visual(arr.copy())