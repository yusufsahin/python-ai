def lineer_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1



def linear_search_trace(arr, target):
    print(f"\n📥 Dizi: {arr}")
    print(f"🎯 Aranan: {target}\n")

    for i in range(len(arr)):
        print(f"🔎 arr[{i}] = {arr[i]} → ", end="")
        if arr[i] == target:
            print(f"✅ EŞLEŞME! {arr[i]} == {target}")
            print(f"➡️ Sonuç: Eleman bulundu. Index = {i}")
            return i
        else:
            print(f"❌ Değil ({arr[i]} ≠ {target})")

    print("❗ Eleman bulunamadı.")
    return -1
arr = [5, 3, 9, 1, 6]
print(lineer_search(arr,9))
print(lineer_search(arr,7))
print(lineer_search(arr,6))

print(linear_search_trace(arr,9))
print(linear_search_trace(arr,7))
print(linear_search_trace(arr,6))