def insertion_sort(bucket):
    for i in range(1,len(bucket)):
        up=bucket[i]
        j=i-1
        while j>=0 and bucket[j]>up:
            bucket[j+1]=bucket[j]
            j-=1
        bucket[j+1]=up

def bucket_sort(arr):
    if not arr:
        return []
    n = len(arr)
    buckets=[[] for _ in range(n)]

    #1. Elemanları uygun bucket'lara yerleştir
    for val in arr:
        index=int(n*val) # 0 ≤ val < 1 varsayımı
        if index==n:
            index=n-1
        buckets[index].append(val)
    #2. Her bucket'ı sıralayın
    for bucket in buckets:
        insertion_sort(bucket)
    #3. Tüm bucket'ları birleştir
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

def bucket_sort_trace(arr):
    if not arr:
        return []

    print(f"\n📥 Girdi: {arr}")
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for val in arr:
        index = int(n * val)
        if index == n:
            index = n - 1
        print(f"  {val} → kova[{index}]")
        buckets[index].append(val)

    for i, bucket in enumerate(buckets):
        print(f"\n🪣 Kova[{i}] sıralanmadan: {bucket}")
        insertion_sort(bucket)
        print(f"🪣 Kova[{i}] sıralandı: {bucket}")

    result = []
    for bucket in buckets:
        result.extend(bucket)

    print(f"\n✅ Sıralı: {result}")
    return result

if __name__ == "__main__":
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.55]
    print("Orijinal Dizi:", arr)
    sorted_arr = bucket_sort(arr)
    print("Sıralı Dizi:", sorted_arr)
    arr2 = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.55]
    sorted_arr2 = bucket_sort_trace(arr2)
