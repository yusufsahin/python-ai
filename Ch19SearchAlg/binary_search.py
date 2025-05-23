def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def binary_search_trace(arr, target):
    print(f"\n📥 Sıralı Dizi: {arr}")
    print(f"🎯 Aranan: {target}\n")

    low, high = 0, len(arr) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2
        print(f"🔎 Adım {step}: low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target:
            print(f"✅ Bulundu! arr[{mid}] = {target}")
            return mid
        elif arr[mid] < target:
            print(f"➡️ {arr[mid]} < {target} → Sağ yarıya git\n")
            low = mid + 1
        else:
            print(f"⬅️ {arr[mid]} > {target} → Sol yarıya git\n")
            high = mid - 1
        step += 1

    print("❗ Eleman bulunamadı.")
    return -1

arr= [1, 3, 5, 7, 9]
print(binary_search(arr, 5))  # Output: 2
print(binary_search(arr, 7))  # Output: 3
print(binary_search(arr, 2))  # Output: -1
print(binary_search_trace(arr, 5))  # Output: 2
print(binary_search_trace(arr, 7))  # Output: 3
print(binary_search_trace(arr, 2))  # Output: -1