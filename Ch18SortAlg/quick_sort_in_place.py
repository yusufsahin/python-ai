import matplotlib.pyplot as plt
import time


# === In-place Quick Sort ===

def partition(arr, low, high):
    pivot = arr[high]
    print(f"Pivot = {pivot} (arr[{high}])")
    i = low - 1

    for j in range(low, high):
        print(f"  Karşılaştır: arr[{j}]={arr[j]} <= {pivot}?")
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"    → Swap: arr[{i}] ↔ arr[{j}] → {arr}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"Son Swap: arr[{i + 1}] ↔ arr[{high}] → {arr}")
    return i + 1


def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(f"Partition index: {pi}")
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)


# === Matplotlib Görselleştirme ===

def draw_array(arr, highlight=None, title=""):
    plt.clf()
    colors = ['red' if highlight and i in highlight else 'skyblue' for i in range(len(arr))]
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.5)


# In-place versiyon için animasyon
def quick_sort_in_place_visual(arr, low, high):
    def partition_visual(a, lo, hi):
        pivot = a[hi]
        i = lo - 1
        for j in range(lo, hi):
            draw_array(a, highlight=[j, hi], title=f"Karşılaştır: {a[j]} <= {pivot}")
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                draw_array(a, highlight=[i, j], title=f"Swap: {a[i]}, {a[j]}")
        a[i + 1], a[hi] = a[hi], a[i + 1]
        draw_array(a, highlight=[i + 1, hi], title="Pivot Swap")
        return i + 1

    if low < high:
        pi = partition_visual(arr, low, high)
        quick_sort_in_place_visual(arr, low, pi - 1)
        quick_sort_in_place_visual(arr, pi + 1, high)


# === Test ===



arr2 = [10, 7, 8, 9, 1, 5]
print("\n🔹 In-place Quick Sort:")
quick_sort_in_place(arr2, 0, len(arr2) - 1)
print("Sıralı (in-place):", arr2)



print("\n📊 In-place Quick Sort Animasyonu:")
arr3 = [10, 7, 8, 9, 1, 5]
plt.ion()
quick_sort_in_place_visual(arr3, 0, len(arr3) - 1)
plt.ioff()
draw_array(arr3, title="In-place Quick Sort Sonuç")
plt.show()
