def ternary_search(arr, target, left, right):
    if left > right:
        return -1
    third = (right - left) // 3
    mid1 = left + third
    mid2 = right - third
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)

arr = [2, 4, 6, 8, 10, 12, 14]
print(ternary_search(arr, 10, 0, len(arr)-1))  # ➜ 4
print(ternary_search(arr, 5, 0, len(arr)-1))   # ➜ -1

