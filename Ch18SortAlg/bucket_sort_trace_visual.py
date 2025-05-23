import matplotlib.pyplot as plt
import time

# === Yardımcı: Kova çizimi ===
def draw_bucket_state(buckets, title=""):
    plt.clf()
    offset = 0
    for i, bucket in enumerate(buckets):
        x_vals = [offset + j * 0.2 for j in range(len(bucket))]
        plt.bar(x_vals, bucket, width=0.15, label=f"Kova {i}")
        offset += len(bucket) + 1
    plt.title(title)
    plt.xlabel("Kova Pozisyonu")
    plt.ylabel("Değer")
    plt.pause(0.8)

# === Insertion Sort + TRACE + VISUAL ===
def insertion_sort_trace_visual(bucket, index):
    print(f"\n🪣 Kova[{index}] sıralanmadan: {bucket}")
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
        draw_bucket_state([bucket], title=f"Kova[{index}] sıralanıyor")
    print(f"🪣 Kova[{index}] sıralandı: {bucket}")

# === Ana Bucket Sort Fonksiyonu ===
def bucket_sort_trace_visual(arr):
    if not arr:
        return []

    print("📥 Orijinal Dizi:", arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]

    plt.ion()
    plt.clf()
    plt.bar(range(len(arr)), arr, color='orange')
    plt.title("Başlangıç Dizisi")
    plt.pause(1)

    # Kovaya yerleştir
    for val in arr:
        index = int(n * val)
        if index == n:
            index = n - 1
        print(f"  {val} → kova[{index}]")
        buckets[index].append(val)
        draw_bucket_state(buckets, title=f"{val} → kova[{index}]")

    # Kovaları sırala
    result = []
    for i, bucket in enumerate(buckets):
        if bucket:
            insertion_sort_trace_visual(bucket, i)
        result.extend(bucket)

    # Sonuç göster
    plt.ioff()
    plt.clf()
    plt.bar(range(len(result)), result, color='green')
    plt.title("✅ Sıralı Dizi (Bucket Sort)")
    plt.show()

    print("\n✅ Sıralı Dizi:", result)
    return result

# === Test ===
if __name__ == "__main__":
    test_data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    sorted_result = bucket_sort_trace_visual(test_data.copy())
