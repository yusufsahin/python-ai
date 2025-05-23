def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if pos >= len(arr):
            return -1
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

arr = [10, 20, 30, 40, 50]
print(interpolation_search(arr, 10))
print(interpolation_search(arr, 30))
print(interpolation_search(arr, 50))
print(interpolation_search(arr, 60))
