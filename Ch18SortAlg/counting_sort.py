def counting_sort(arr):
    if not arr:
        return []
    max_val=max(arr)
    count =[0]*(max_val+1)

    #1.Sayıları say
    for num in arr:
        count[num]+=1

    #2.Toplanarak indexlere dönüştür
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    #3.Sıralı diziyi oluştur
    output = [0]*len(arr)
    #4.Ters sırada yerleştir(stabilite için)
    for num in reversed(arr):
        output[count[num]-1]=num
        count[num]-=1
    return output
def counting_sort_trace(arr):
    if not arr:
        print("Dizi boş.")
        return []
    print("Girdi:", arr)
    max_val = max(arr)
    count = [0] * (max_val + 1)
    print("Max değer:", max_val)
    print("\n Sayma aşaması")
    for num in arr:
        count[num] += 1
        print(f"  {num} sayıldı : count = {count}")
    print("\n Kümülatif toplama:")
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        print(f"  count[{i}] -> {count[i]}")
    output = [0] * len(arr)
    print("\n Çıkış dizisi:",output)

    print("\n Ters sırada yerleştirme:")
    for i in reversed(arr):
        output[count[i] - 1] = i
        count[i] -= 1
        print(f"  count[{num}] güncellendi: {count}")
        print(f"  output: {output}")

    print("\n✅ Sonuç:", output)
    return output
def counting_sort_with_negatives(arr, trace=True):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    if trace:
        print("📥 Girdi:", arr)
        print(f"🧮 Min: {min_val}, Max: {max_val}, Range: {range_of_elements}")

    # 1. Frekansları say
    for num in arr:
        count[num - min_val] += 1
        if trace:
            print(f"  Sayı {num} sayıldı → count = {count}")

    # 2. Kümülatif toplama
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    if trace:
        print("\n➕ Kümülatif count dizisi:", count)

    # 3. Ters sırada yerleştir (kararlılık için)
    for num in reversed(arr):
        index = count[num - min_val] - 1
        output[index] = num
        count[num - min_val] -= 1
        if trace:
            print(f"  {num} → output[{index}]")
            print(f"  count güncellendi: {count}")
            print(f"  output: {output}")

    if trace:
        print("\n✅ Sıralı Dizi:", output)

    return output

import matplotlib.pyplot as plt
import time

def draw_count_array(arr, count, output, step=""):
    plt.clf()
    plt.suptitle(step, fontsize=14)

    # Girdi dizisi
    plt.subplot(3, 1, 1)
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title("Girdi Dizisi")

    # Count dizisi
    plt.subplot(3, 1, 2)
    plt.bar(range(len(count)), count, color='orange')
    plt.title("Sayma Dizisi (count)")

    # Çıkış dizisi
    plt.subplot(3, 1, 3)
    plt.bar(range(len(output)), output, color='green')
    plt.title("Sıralı Sonuç (output)")

    plt.pause(1)

def counting_sort_visual(arr):
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    plt.ion()
    draw_count_array(arr, count, output, "Başlangıç")

    for num in arr:
        count[num] += 1
        draw_count_array(arr, count, output, f"Sayıldı: {num}")

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        draw_count_array(arr, count, output, f"Kümülatif: i={i}")

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
        draw_count_array(arr, count, output, f"Yerleştiriliyor: {num}")

    plt.ioff()
    draw_count_array(arr, count, output, "✅ Tamamlandı")
    plt.show()
    return output


arr=[4,2,2,8,8,3,3,1]
print("Orijinal dizi:", arr)
sorted_arr=counting_sort(arr)
print("Sıralı dizi:", sorted_arr)
arr2=[4,2,2,8,8,3,3,1]
sorted_arr2=counting_sort_trace(arr2)
print(sorted_arr2)
arr3=[4,2,2,8,8,3,3,1]
counting_sort_visual(arr3)

arr4 = [4, -1, 2, -3, 3, -1, 0]
print("Orijinal dizi:", arr4)
sorted_arr4 = counting_sort_with_negatives(arr4)
