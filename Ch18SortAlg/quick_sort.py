import matplotlib.pyplot as plt
import time


# === Fonksiyonel (non-inplace) Quick Sort ===

def quick_sort(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}Girdi: {arr}")

    if len(arr) <= 1:
        print(f"{indent}Tek elemanlı veya boş → {arr}")
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"{indent}Pivot: {pivot} → Left: {left}, Middle: {middle}, Right: {right}")
    return quick_sort(left, depth + 1) + middle + quick_sort(right, depth + 1)


# === Matplotlib Görselleştirme ===

def draw_array(arr, highlight=None, title=""):
    plt.clf()
    colors = ['red' if highlight and i in highlight else 'skyblue' for i in range(len(arr))]
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.5)


# Fonksiyonel versiyon için animasyon
def quick_sort_visual(arr):
    def sort(data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        merged = sort(left) + middle + sort(right)
        draw_array(merged, title=f"Pivot: {pivot}")
        return merged

    plt.ion()
    sorted_data = sort(arr.copy())
    plt.ioff()
    draw_array(sorted_data, title="Fonksiyonel Quick Sort Sonuç")
    plt.show()
    return sorted_data



# === Test ===

arr1 = [10, 7, 8, 9, 1, 5]
print("🔹 Fonksiyonel Quick Sort:")
sorted_arr = quick_sort(arr1.copy())
print("Sıralı:", sorted_arr)


# === Görsel animasyonlar ===
print("\n📊 Fonksiyonel Quick Sort Animasyonu:")
quick_sort_visual([10, 7, 8, 9, 1, 5])
