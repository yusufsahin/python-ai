import matplotlib.pyplot as plt
import time

# === TRACE + VISUAL destekli Counting Sort ===
def counting_sort_by_digit_trace_visual(arr, exp, step, enable_plot=True):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    print(f"\n📊 [Adım {step}] → Basamak: {exp}'ler")
    print(f"Girdi: {arr}")

    # 1. Sayım
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    print(f"  Sayım (count): {count}")

    # 2. Kümülatif toplama
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(f"  Kümülatif (count): {count}")

    # 3. Output dizisi
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    print(f"  Output (kararlı sıralama): {output}")

    # 4. Görsel çizim
    if enable_plot:
        plt.clf()
        plt.bar(range(len(output)), output, color='skyblue')
        plt.title(f"Radix Sort - Basamak {exp} (Adım {step})")
        plt.xlabel("Index")
        plt.ylabel("Değer")
        plt.pause(1)

    # 5. Geri kopyalama
    for i in range(n):
        arr[i] = output[i]

# === Ana Radix Sort Fonksiyonu ===
def radix_sort_trace_visual(arr, enable_plot=True):
    if not arr:
        return

    max_val = max(arr)
    exp = 1
    step = 1

    if enable_plot:
        plt.ion()

    while max_val // exp > 0:
        counting_sort_by_digit_trace_visual(arr, exp, step, enable_plot)
        exp *= 10
        step += 1

    if enable_plot:
        plt.ioff()
        plt.title("✅ Radix Sort Tamamlandı")
        plt.show()

# === Test ===
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("📥 Orijinal Dizi:", arr)
    radix_sort_trace_visual(arr, enable_plot=True)
    print("\n✅ Sıralı Dizi:", arr)
