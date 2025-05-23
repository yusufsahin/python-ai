import matplotlib.pyplot as plt
import time

# === Basamak bazlı Counting Sort (Pozitif) ===
def counting_sort_by_digit_trace_visual(arr, exp, step, enable_plot=True):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    print(f"\n📊 [Adım {step}] → Basamak: {exp}'ler")
    print(f"Girdi: {arr}")

    # 1. Sayma
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    print(f"  Sayım (count): {count}")

    # 2. Kümülatif toplama
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(f"  Kümülatif (count): {count}")

    # 3. Çıkış dizisi (kararlılık için tersten)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    print(f"  Çıkış: {output}")

    # 4. Görsel çizim
    if enable_plot:
        plt.clf()
        plt.bar(range(len(output)), output, color='skyblue')
        plt.title(f"Radix Sort - Basamak {exp} (Adım {step})")
        plt.xlabel("Index")
        plt.ylabel("Değer")
        plt.pause(1)

    # 5. Geri kopyala
    for i in range(n):
        arr[i] = output[i]

# === Pozitif Sayılar için Radix Sort ===
def radix_sort_positive(arr, enable_plot=True):
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
        plt.title("✅ Pozitifler Sıralandı")
        plt.show()

# === Negatif Sayılar için Radix Sort ===
def radix_sort_negative(arr, enable_plot=True):
    arr = [-x for x in arr]  # Pozitife çevir
    radix_sort_positive(arr, enable_plot=False)  # TRACE sadece pozitif için
    arr = [-x for x in reversed(arr)]  # Sıralı negatif geri çevir
    return arr

# === Tam Radix Sort (Negatif + Pozitif) ===
def radix_sort_with_negatives_trace_visual(arr, enable_plot=True):
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    print("🔹 Negatifler:", negatives)
    sorted_neg = radix_sort_negative(negatives, enable_plot)

    print("\n🔹 Pozitifler:", positives)
    radix_sort_positive(positives, enable_plot)

    return sorted_neg + positives

# === Test ===
if __name__ == "__main__":
    arr = [170, -45, 75, -90, 802, 24, 2, -66]
    print("📥 Orijinal Dizi:", arr)

    sorted_arr = radix_sort_with_negatives_trace_visual(arr.copy(), enable_plot=True)

    print("\n✅ Sıralanmış Dizi:", sorted_arr)
